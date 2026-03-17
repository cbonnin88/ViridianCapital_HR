import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

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
bands = sorted([str(x) for x in df['SALARY_BAND'].unique()])

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


st.divider()

# 8. PHASE 6: MACHINE LEARNING PREDICTOR
st.header("🔮 ESG Leadership Propensity Model")
st.write("Train an AI model to predict if a future candidate will become an ESG Leader.")

# Training Toggle
if st.button("🚀 Train Model on Current Workforce"):
    # Feature Engineering
    ml_df = df.copy()
    ml_df['DEPT_CODE'] = ml_df['DEPARTMENT'].astype('category').cat.codes
    ml_df['BAND_CODE'] = ml_df['SALARY_BAND'].astype('category').cat.codes
    ml_df['IS_LEADER'] = (ml_df['ESG_SCORE'] > 70).astype(int)
    
    X = ml_df[['DEPT_CODE', 'BAND_CODE', 'AGE']]
    y = ml_df['IS_LEADER']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Model Fit
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Save to Session State
    st.session_state['trained_model'] = clf
    st.session_state['accuracy'] = float(clf.score(X_test, y_test))
    st.success(f"Model trained successfully! Accuracy: {st.session_state['accuracy']:.2%}")

# 9. Prediction UI (Only shows if model is trained)
if 'trained_model' in st.session_state:
    st.subheader("Candidate Simulation")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        in_dept = st.selectbox("Department", depts)
        dept_idx = depts.index(in_dept)
    with c2:
        in_band = st.selectbox("Salary Band", bands)
        band_idx = bands.index(in_band)
    with c3:
        in_age = st.number_input("Age", 18, 70, 30)
    
    # Prediction Calculation
    pred = st.session_state['trained_model'].predict([[dept_idx, band_idx, in_age]])
    prob = st.session_state['trained_model'].predict_proba([[dept_idx, band_idx, in_age]])
    
    st.write("---")
    if pred[0] == 1:
        st.success(f"### Prediction: **ESG LEADER** 🌟")
        st.write(f"Confidence Level: **{float(prob[0][1]):.1%}**")
    else:
        st.error(f"### Prediction: **MEMBER** 👤")
        st.write(f"Confidence Level: **{float(prob[0][0]):.1%}**")