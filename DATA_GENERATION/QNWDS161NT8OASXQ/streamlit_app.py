import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Get the current Snowflake Session
session = get_active_session()

# Title and Introduction
st.title('🌿 Viridian Capital Talent Explorer')
st.write('Use the filter below to find high-performing employees for the 2026 Green Bonus')

@st.cache_data
def get_base_data():
    return session.table("fct_compensation_summary").to_pandas()

raw_df = get_base_data()

# Sidebar Filters
st.sidebar.header('Filter Criteria')

# Get unique values for the dropdowns
offices = raw_df['OFFICE'].unique().tolist()
depts = raw_df['DEPARTMENT'].unique().tolist()

selected_office = st.sidebar.multiselect("Select Office(s)", options=offices, default=offices)
selected_dept = st.sidebar.multiselect("Select Department(s)", options=depts, default=depts)

# ESG Score Slider
min_esg = st.sidebar.slider("Minimum ESG Score", min_value=0, max_value=100, value=75)

# Data Query
filtered_df = raw_df[
    (raw_df['OFFICE'].isin(selected_office)) & 
    (raw_df['DEPARTMENT'].isin(selected_dept)) & 
    (raw_df['ESG_SCORE'] >= min_esg)
]
# Convert to Pandas for Streamlit Display
pd_df = filtered_df.to_pandas()

# Display Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Found Employees", len(filtered_df))
# Data Table
st.subheader('Results')
st.dataframe(pd_df[['FULL_NAME','JOB_TITLE','OFFICE','SALARY_BAND','ESG_SCORE','TOTAL_COMPENSATION_EUR']], use_container_width=True)

if not filtered_df.empty:
    col2.metric("Avg. Salary", f"€{filtered_df['BASE_SALARY_EUR'].mean():,.0f}")
    col3.metric("Avg. ESG Score", round(filtered_df['ESG_SCORE'].mean(), 1))
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.warning("No employees match these filters. Try adjusting the ESG slider!")

# Download Button
csv = pd_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label='Download Filtered Results as CSV',
    data=csv,
    file_name='viridiancapital_filtered_talent.csv',
    mime='text/csv'
)

