-- 1075. Project Employees I
SELECT
    P.project_id,
    ROUND(AVG(E.experience_years), 2) AS average_years
FROM
    Employee AS E
    LEFT JOIN Project AS P ON E.employee_id = P.employee_id
GROUP BY
    P.project_id
HAVING
    NOT P.project_id IS NULL;