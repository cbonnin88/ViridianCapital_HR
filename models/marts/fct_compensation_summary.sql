-- My fact table, I will calculate the Total Target Compensation

WITH employees AS (
    SELECT * FROM {{ref('stg_employees')}}
),
comp AS (
    SELECT * FROM {{source('viridian_capital_raw','RAW_COMPENSATION')}}
),
esg AS (
    SELECT * FROM {{source('viridian_capital_raw','RAW_ESG_METRICS')}}
)

SELECT
    e.EMPLOYEE_ID,
    e.FULL_NAME,
    e.AGE,
    e.JOB_TITLE,
    e.OFFICE,
    e.DEPARTMENT,
    c.SALARY_BAND,
    c.BASE_SALARY_EUR,
    c.BONUS_PERCENT,
    esg.ESG_SCORE,
    -- Bonus is weighted by ESG Score
    (c.BASE_SALARY_EUR * c.BONUS_PERCENT * (esg.ESG_SCORE / 100)) AS esg_weighted,
    (c.BASE_SALARY_EUR + (c.BASE_SALARY_EUR * c.BONUS_PERCENT * (esg.ESG_SCORE / 100))) AS total_compensation_eur
FROM employees AS e
JOIN comp AS c
    ON e.EMPLOYEE_ID = c.EMPLOYEE_ID
JOIN esg AS esg
    ON e.EMPLOYEE_ID = esg.EMPLOYEE_ID
