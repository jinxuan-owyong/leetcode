-- 1141. User Activity for the Past 30 Days I
SELECT
    activity_date AS day,
    COUNT(DISTINCT (user_id)) AS active_users
FROM
    Activity
WHERE
    -- >= 2019-06-28
    activity_date > DATE_SUB('2019-07-27', INTERVAL 30 DAY) AND activity_date <= DATE('2019-07-27')
GROUP BY
    day