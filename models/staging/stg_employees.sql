-- stg_employees.sql our staging model

SELECT
    EMPLOYEE_ID,
    FIRST_NAME,
    LAST_NAME,
    -- Combining names for easier reporting
    FIRST_NAME || ' ' || LAST_NAME AS FULL_NAME,
    OFFICE,
    DEPARTMENT,
    JOB_TITLE,
    CONTRACT_TYPE,
    HIRE_DATE,
    AGE,
    GENDER
FROM {{source('viridian_capital_raw','RAW_EMPLOYEES')}}