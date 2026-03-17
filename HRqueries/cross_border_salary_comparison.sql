-- Is our London office significantly more expensive than Paris for the same roles?

SELECT
    e.job_title,
    ROUND(AVG(CASE WHEN e.office = 'Paris' THEN c.base_salary_eur END),2) AS avg_paris_eur,
    ROUND(AVG(CASE WHEN e.office = 'London' THEN c.base_salary_eur END),2) AS avg_london_eur
FROM viridian_capital.public.raw_employees AS e
JOIN viridian_capital.public.raw_compensation AS c
    ON e.employee_id = c.employee_id
WHERE e.job_title IN ('Analytics Engineer','Product Manager')
GROUP BY 1;