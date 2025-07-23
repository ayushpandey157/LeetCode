# Write your MySQL query statement below
# Write your MySQL query statement below
select "High Salary" as category , count(account_id) as accounts_count from accounts where income>50000 
union
select "Average Salary" as category , count(account_id) as accounts_count from accounts where income>=20000 and income<=50000
union
select "Low Salary" as category , count(account_id) as accounts_count from accounts where income<20000 