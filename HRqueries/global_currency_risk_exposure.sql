-- How much of our total payroll is paid in non-EUR currencies?

SELECT
    local_currency,
    COUNT(*) AS num_employees,
    SUM(base_salary_eur) AS total_eur_value
FROM viridian_capital.public.raw_compensation
GROUP BY 1