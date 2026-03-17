import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Get the current Snowflake Session
session = get_active_session()

# Title and Introduction
st.title('🌿 Viridian Capital Talent Explorer')

@st.cache_data
def load_data():
    # Force conversion to ensure we are working with a clean Pandas DF
    return session.table("fct_compensation_summary").to_pandas()

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Filter Criteria")

# Ensure these are native Python lists of strings
offices = sorted([str(x) for x in df['OFFICE'].unique()])
depts = sorted([str(x) for x in df['DEPARTMENT'].unique()])

selected_office = st.sidebar.multiselect("Select Office(s)", options=offices, default=offices)
selected_dept = st.sidebar.multiselect("Select Department(s)", options=depts, default=depts)

# FORCE min_esg to be a native Python int
min_esg = int(st.sidebar.slider("Minimum ESG Score", 0, 100, 75))

# 4. Filter Logic (Using Pandas)
mask = (
    df['OFFICE'].isin(selected_office) & 
    df['DEPARTMENT'].isin(selected_dept) & 
    (df['ESG_SCORE'] >= min_esg)
)
filtered_df = df[mask].copy() # Use .copy() to avoid SettingWithCopy warnings

# 5. Display Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Found Employees", int(len(filtered_df))) # Force int

if len(filtered_df) > 0:
    # FORCE these metrics to native Python floats/strings
    avg_sal = float(filtered_df['BASE_SALARY_EUR'].mean())
    avg_esg = float(filtered_df['ESG_SCORE'].mean())
    
    col2.metric("Avg. Salary", f"€{avg_sal:,.0f}")
    col3.metric("Avg. ESG Score", round(avg_esg, 1))
    
    st.subheader("Filtered Talent List")
    st.dataframe(filtered_df, use_container_width=True)

    # --- DOWNLOAD TO CSV SECTION ---
    st.divider()
    
    # We use an 'id' or unique key to ensure the button doesn't conflict
    # and convert the data to a standard string
    csv_string = filtered_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Results as CSV",
        data=str(csv_string), # Force cast to string
        file_name='viridian_capital_filtered_talent.csv',
        mime='text/csv',
        key='download-btn' # Unique key helps prevent built-in operation errors
    )
else:
    st.warning("No employees match these filters. Try lowering the ESG Score threshold.")