import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Get the current Snowflake Session
session = get_active_session()

# Title and Introduction
st.title('🌿 Viridian Capital Talent Explorer')
st.write('Use the filter below to find high-performing employees for the 2026 Green Bonus')

# Sidebar Filters
st.sidebar.header('Filter Criteria')

# Get unique values for the dropdowns
offices_df = session.sql("SELECT DISTINCT OFFICE FROM fct_compensation_summary").to_pandas()
offices = offices_df['OFFICE'].tolist()

depts_df = session.sql("SELECT DISTINCT DEPARTMENT FROM fct_compensation_summary").to_pandas()
depts = depts_df['DEPARTMENT'].tolist()

selected_office = st.sidebar.multiselect('Select Office(s)', offices, default=offices)
selected_dept = st.sidebar.multiselect("Select Department(s)", depts, default=depts)

# ESG Score Slider
min_esg = st.sidebar.slider('Minimum ESG Score',0,100,75)

# Data Query
df = session.table('fct_compensation_summary').filter(
    (col('OFFICE').in_(selected_office)) &
    (col('DEPARTMENT').in_(selected_dept)) &
    (col('ESG_SCORE') >= min_esg)
)

# Convert to Pandas for Streamlit Display
pd_df = df.to_pandas()

# Display Metrics
col1,col2,col3 = st.columns(3)
col1.metric('Found Employees', len(pd_df))
col2.metric("Avg. Salary", f"€{pd_df['BASE_SALARY_EUR'].mean():,.0f}")
col3.metric('Avg. ESG Score',round(pd_df['ESG_SCORE'].mean(),1))

# Data Table
st.subheader('Results')
st.dataframe(pd_df[['FULL_NAME','JOB_TITLE','OFFICE','SALARY_BAND','ESG_SCORE','TOTAL_COMPENSATION_EUR']], use_container_width=True)

# Download Button
csv = pd_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label='Download Filtered Results as CSV',
    data=csv,
    file_name='viridiancapital_filtered_talent.csv',
    mime='text/csv'
)

