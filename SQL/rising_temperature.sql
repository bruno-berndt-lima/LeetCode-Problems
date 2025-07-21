-- Write your PostgreSQL query statement below
SELECT day.id
FROM Weather day
JOIN Weather day_before
    ON day.recordDate = day_before.recordDate + INTERVAL '1 day'
WHERE day.temperature > day_before.temperature;
