-- Employees with a high target bonus percentage but an ESG score below 50.

SELECT
    e.first_name,
    e.last_name,
    e.department,
    c.bonus_percent,
    esg.esg_score
FROM viridian_capital.public.raw_employees AS e
JOIN viridian_capital.public.raw_compensation AS c
    ON e.employee_id = c.employee_id
JOIN viridian_capital.public.raw_esg_metrics AS esg 
    ON c.employee_id = esg.employee_id
WHERE 
    c.bonus_percent >= 0.20 AND esg.esg_score < 50;