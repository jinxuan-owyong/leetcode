-- 1280. Students and Examinations
SELECT
    ST.student_id,
    ST.student_name,
    S.subject_name,
    COUNT(E.subject_name) AS attended_exams
FROM
    -- take cartesian product since not all students took exam for every subject
    Students AS ST
    CROSS JOIN Subjects AS S
    LEFT JOIN Examinations AS E ON ST.student_id = E.student_id
    AND S.subject_name = E.subject_name
GROUP BY
    ST.student_id,
    ST.student_name,
    S.subject_name
ORDER BY
    ST.student_id ASC,
    S.subject_name ASC;