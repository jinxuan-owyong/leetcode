-- 184. Department Highest Salary
WITH
    DeptMax AS (
        SELECT
            MAX(salary),
            departmentId
        FROM
            Employee
        GROUP BY
            departmentId
    )
SELECT
    D.name AS "Department",
    E.name AS "Employee",
    E.salary AS "Salary"
FROM
    Employee AS E
    LEFT JOIN Department AS D ON E.departmentId = D.id
    LEFT JOIN DeptMax AS M ON E.departmentId = M.departmentId
WHERE
    E.salary = M.MAX