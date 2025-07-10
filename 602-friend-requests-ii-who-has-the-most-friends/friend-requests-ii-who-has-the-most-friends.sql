# Write your MySQL query statement below
with n1 as(
    select requester_id, accepter_id from requestaccepted
    union all
    select accepter_id,requester_id from requestaccepted
)
select requester_id id, count(requester_id) num from n1
group by 1
order by 2 desc
limit 1