-- 570. Managers with at Least 5 Direct Reports
SELECT
    name
FROM
    Employee
WHERE
    id IN (
        SELECT
            managerId
        FROM
            Employee
        WHERE
            NOT managerId IS NULL
        GROUP BY
            managerId
        HAVING
            COUNT(*) >= 5
    );