-- Ranking employees by salary within their own department.

SELECT
    e.first_name,
    e.last_name,
    e.department,
    c.base_salary_eur,
    PERCENT_RANK() OVER(PARTITION BY e.department ORDER BY c.base_salary_eur) AS salary_percentile
FROM viridian_capital.public.raw_employees AS e
JOIN viridian_capital.public.raw_compensation AS c
    ON e.employee_id = c.employee_id;