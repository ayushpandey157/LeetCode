# Write your MySQL query statement below
WITH UserCategories AS (
  SELECT DISTINCT pp.user_id, pi.category
  FROM ProductPurchases AS pp
  JOIN ProductInfo AS pi
    ON pp.product_id = pi.product_id
),

CategoryPairs AS (
  SELECT 
    uc1.user_id,
    LEAST(uc1.category, uc2.category) AS category1,
    GREATEST(uc1.category, uc2.category) AS category2
  FROM UserCategories AS uc1
  JOIN UserCategories AS uc2
    ON uc1.user_id = uc2.user_id
   AND uc1.category < uc2.category
),

PairCounts AS (
  SELECT
    category1,
    category2,
    COUNT(DISTINCT user_id) AS customer_count
  FROM CategoryPairs
  GROUP BY category1, category2
)

SELECT
  category1,
  category2,
  customer_count
FROM PairCounts
WHERE customer_count >= 3
ORDER BY 
  customer_count DESC,
  category1 ASC,
  category2 ASC;