# Write your MySQL query statement below
SELECT id,
MAX(CASE WHEN month = 'Jan' THEN revenue ELSE null END) as Jan_Revenue,
MAX(CASE WHEN month = 'Feb' THEN revenue ELSE null END) as Feb_Revenue,
MAX(CASE WHEN month = 'Mar' THEN revenue ELSE null END) as Mar_Revenue,
MAX(CASE WHEN month = 'Apr' THEN revenue ELSE null END) as Apr_Revenue,
MAX(CASE WHEN month = 'May' THEN revenue ELSE null END) as May_Revenue,
MAX(CASE WHEN month = 'Jun' THEN revenue ELSE null END) as Jun_Revenue,
MAX(CASE WHEN month = 'Jul' THEN revenue ELSE null END) as Jul_Revenue,
MAX(CASE WHEN month = 'Aug' THEN revenue ELSE null END) as Aug_Revenue,
MAX(CASE WHEN month = 'Sep' THEN revenue ELSE null END) as Sep_Revenue,
MAX(CASE WHEN month = 'Oct' THEN revenue ELSE null END) as Oct_Revenue,
MAX(CASE WHEN month = 'Nov' THEN revenue ELSE null END) as Nov_Revenue,
MAX(CASE WHEN month = 'Dec' THEN revenue ELSE null END) as Dec_Revenue
FROM Department
GROUP BY id;