-- Find employees whose ESG score was so high (>90) that it significantly boosted their bonus.

SELECT
    full_name,
    department,
    esg_score,
    bonus_percent,
    esg_weighted
FROM viridian_capital.dbt_viridian_hr.fct_compensation_summary
WHERE esg_score >= 90
ORDER BY 5 DESC;