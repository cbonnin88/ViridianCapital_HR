-- The ratio of the CEO's salary to the average employee's salary.

SELECT
    ROUND((SELECT
        base_salary_eur
    FROM viridian_capital.dbt_viridian_hr.fct_compensation_summary
    WHERE job_title ='CEO') / (SELECT AVG(base_salary_eur) FROM viridian_capital.dbt_viridian_hr.fct_compensation_summary),1) AS ceo_pay_ration;