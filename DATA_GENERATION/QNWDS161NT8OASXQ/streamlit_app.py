import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Get the current Snowflake Session
session = get_active_session()

# Title and Introduction
st.title('🌿 Viridian Capital Talent Explorer')
