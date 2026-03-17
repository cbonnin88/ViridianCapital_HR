-- Identify if anyone in an entry-level band (L5) is earning more than the average of a mid-level band (L3).

WITH band_avgs AS (
    SELECT
        salary_band,
        AVG(base_salary_eur) AS band_avg
    FROM viridian_capital.dbt_viridian_hr.fct_compensation_summary
    GROUP BY 1
)
SELECT
    f.full_name,
    f.salary_band,
    f.base_salary_eur,
    b.band_avg AS l3_avg
FROM viridian_capital.dbt_viridian_hr.fct_compensation_summary AS f
JOIN band_avgs AS b
    ON b.salary_band = 'L3'
WHERE f.salary_band = 'L5'
      AND f.base_salary_eur > b.band_avg;