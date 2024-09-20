-- 1683. Invalid Tweets
SELECT
    tweet_id
FROM
    Tweets
WHERE
    LENGTH (content) > 15;