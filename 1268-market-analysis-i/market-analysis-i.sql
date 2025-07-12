# Write your MySQL query statement below
# users is fact table so, include in from bcoz we need all data from it
# we want both Null and not null so, double check handling Nulls
#so, simple Left Join and And will preserve all nulls 
#if it is where conditions null get skipped.
# Now Lets Goahead.....
select user_id  buyer_id ,join_date,count(order_date)orders_in_2019 
from users
left join Orders
on user_id=buyer_id
and year(order_date)=2019
group by 1,2