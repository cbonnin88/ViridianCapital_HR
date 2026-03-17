import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Get the current Snowflake Session
session = get_active_session()

# Title and Introduction
st.title('🌿 Viridian Capital Talent Explorer')
@st.cache_data
def load_data():
    return session.table("fct_compensation_summary").to_pandas()

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Filter Criteria")

offices = sorted(df['OFFICE'].unique().tolist())
depts = sorted(df['DEPARTMENT'].unique().tolist())

selected_office = st.sidebar.multiselect("Select Office(s)", options=offices, default=offices)
selected_dept = st.sidebar.multiselect("Select Department(s)", options=depts, default=depts)
min_esg = st.sidebar.slider("Minimum ESG Score", 0, 100, 75)

# 4. Filter Logic (Using Pandas)
mask = (
    df['OFFICE'].isin(selected_office) & 
    df['DEPARTMENT'].isin(selected_dept) & 
    (df['ESG_SCORE'] >= min_esg)
)
filtered_df = df[mask]

# 5. Display Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Found Employees", len(filtered_df))

if len(filtered_df) > 0:
    col2.metric("Avg. Salary", f"€{filtered_df['BASE_SALARY_EUR'].mean():,.0f}")
    col3.metric("Avg. ESG Score", round(filtered_df['ESG_SCORE'].mean(), 1))
    
    st.subheader("Filtered Talent List")
    st.dataframe(filtered_df, use_container_width=True)

    # --- NEW: DOWNLOAD TO CSV SECTION ---
    st.divider()
    
    # Helper function to convert dataframe to CSV
    @st.cache_data
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv_data = convert_df_to_csv(filtered_df)

    st.download_button(
        label="📥 Download Results as CSV",
        data=csv_data,
        file_name='ecopay_filtered_talent.csv',
        mime='text/csv',
    )
else:
    st.warning("No employees match these filters. Try lowering the ESG Score threshold.")