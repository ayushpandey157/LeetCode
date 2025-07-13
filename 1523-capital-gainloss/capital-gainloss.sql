# Write your MySQL query statement below
# Write your MySQL query statement below
-- group by 每支股票，sum (price) (operation = 'sell') - sum (price) (operation = 'buy')，用邏輯的1 ,0 特性來做乘除
SELECT 
    stock_name,
    SUM((operation = 'Sell')* price) - SUM((operation = 'Buy')* price)
    AS capital_gain_loss
FROM Stocks 
GROUP BY stock_name
;