# Write your MySQL query statement below
with store_price as(
    select store_id ,store_name , location,
    max(price)maxprice,min(price)minprice
    from stores
    join inventory 
    using(store_id)
    group by 1,2,3
    having count(distinct product_name)>2
),
expense as(
    select s.store_id ,store_name , location,
    product_name,quantity,price
    from store_price s
    join inventory  i
    using (store_id)
    where price in(maxprice,minprice)
)
select c.store_id,c.store_name,c.location,ex.product_name  most_exp_product ,
c.product_name cheapest_product   ,
round(c.quantity /ex.quantity  ,2)imbalance_ratio 
from  expense c
join expense ex
on c.store_id=ex.store_id
and c.price<ex.price
and c.quantity>ex.quantity
order by imbalance_ratio  desc,c.store_name