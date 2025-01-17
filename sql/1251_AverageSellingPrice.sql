-- 1251. Average Selling Price
SELECT
    P.product_id,
    COALESCE(
        ROUND(SUM(P.price * S.units) * 1.0 / SUM(S.units), 2),
        0
    ) AS average_price
FROM
    UnitsSold AS S
    RIGHT JOIN Prices as P ON P.product_id = S.product_id
    AND S.purchase_date >= P.start_date
    AND S.purchase_date <= P.end_date
GROUP BY
    P.product_id