-- 176. Second Highest Salary
SELECT
    (
        SELECT DISTINCT
            salary AS "SecondHighestSalary"
        FROM
            Employee
        ORDER BY
            salary DESC
        LIMIT
            1
        OFFSET
            1
    )