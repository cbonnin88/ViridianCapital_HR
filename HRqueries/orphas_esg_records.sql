-- Records that exist in the ESG metrics table but might not be linked to a valid employee

SELECT
    e.employee_id AS emp_table_id,
    m.employee_id AS esg_table_id,
    COALESCE(e.first_name,e.last_name,'DELETED/UNKNOWN EMPLOYEE') AS name_check
FROM viridian_capital.public.raw_employees AS e
FULL OUTER JOIN viridian_capital.public.raw_esg_metrics AS m
        ON e.employee_id = m.employee_id
WHERE e.employee_id IS NULL OR m.employee_id IS NULL;