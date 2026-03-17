-- Finance needs to know which department is the most "expensive" per head.

SELECT
    department,
    COUNT(employee_id) AS headcount,
    ROUND(SUM(total_compensation_eur),2) AS total_budget,
    ROUND(AVG(total_compensation_eur),2) AS avg_comp_per_head
FROM viridian_capital.dbt_viridian_hr.fct_compensation_summary
GROUP BY 1
ORDER BY 4 DESC;