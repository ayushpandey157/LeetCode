# Write your MySQL query statement below
with cte as(
    select employee_id ,review_date,rating fd,
    lead(rating) over(partition by employee_id order by review_date )sd,
    lead(rating,2) over(partition by employee_id order by review_date )td,
    row_number() over(partition by employee_id order by review_date desc )rnk
    from performance_reviews
)
select employee_id,name, td-fd improvement_score 
from cte
left join employees
using(employee_id)
where rnk=3
and fd<sd
and fd<td

order by improvement_score desc,name