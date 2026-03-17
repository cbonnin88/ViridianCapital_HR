-- HQ needs to identify the highest-paid individuals in the Paris office for a talent retention review.

SELECT
    e.first_name,
    e.last_name,
    e.job_title,
    c.base_salary_eur
FROM viridian_capital.public.raw_employees AS e
JOIN viridian_capital.public.raw_compensation AS c 
    ON e.employee_id = c.employee_id
WHERE e.office = 'Paris' AND e.department != 'Leadership'
ORDER BY c.base_salary_eur DESC
LIMIT 10;
