-- 1633. Percentage of Users Attended a Contest
SELECT
    contest_id,
    ROUND(
        COUNT(user_id) / (
            SELECT
                COUNT(user_id) * 1.0
            FROM
                Users
        ) * 100,
        2
    ) AS percentage
FROM
    Register
GROUP BY
    contest_id
ORDER BY
    percentage DESC,
    contest_id ASC