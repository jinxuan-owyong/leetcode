-- 1211. Queries Quality and Percentage
WITH
    PoorCount AS (
        SELECT
            query_name,
            COUNT(*) AS poor_count
        FROM
            queries
        WHERE
            rating < 3
        GROUP BY
            query_name
    )
SELECT
    Q.query_name,
    ROUND(AVG(Q.rating / position), 2) AS quality,
    COALESCE(ROUND(P.poor_count / COUNT(*) * 100, 2), 0) AS poor_query_percentage
FROM
    queries AS Q
    LEFT JOIN PoorCount AS P ON Q.query_name = P.query_name
GROUP BY
    query_name;
-- SELECT
--     query_name,
--     ROUND(AVG(rating / position), 2) AS quality,
--     ROUND(
--         SUM(
--             CASE
--                 WHEN rating < 3 THEN 1
--                 ELSE 0
--             END
--         ) / COUNT(*) * 100,
--         2
--     ) AS poor_query_percentage
-- FROM
--     queries
-- GROUP BY
--     query_name;