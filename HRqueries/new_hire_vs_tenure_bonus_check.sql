-- Did employees hired in the last year (2025/2026) receive higher ESG scores than veterans?

SELECT
    CASE
        WHEN TO_TIMESTAMP(e.hire_date / 1000000000) >= '2025-01-01' THEN 'New Hire'
        ELSE 'Veteran'
    END AS hire_group,
    AVG(esg.esg_score) AS avg_esg
FROM viridian_capital.public.raw_employees AS e
JOIN viridian_capital.public.raw_esg_metrics AS esg
    ON e.employee_id = esg.employee_id
JOIN viridian_capital.public.raw_compensation AS c
    ON e.employee_id = c.employee_id
GROUP BY 1;

