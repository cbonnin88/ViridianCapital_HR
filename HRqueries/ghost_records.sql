-- Identify if there are any employees in the HR system who do not have a corresponding record in the Compensation table.

SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    e.office,
    c.base_salary_eur
FROM viridian_capital.public.raw_employees AS e
LEFT JOIN viridian_capital.public.raw_compensation AS c
    ON e.employee_id = c.employee_id
WHERE c.employee_id IS NULL;