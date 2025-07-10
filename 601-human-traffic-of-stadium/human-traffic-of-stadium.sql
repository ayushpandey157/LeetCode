# Write your MySQL query statement below
with n1 as (
    select s1.id as one,s2.id as two,s3.id as three from stadium s1
    join stadium s2
    join stadium s3
    on s1.id = s2.id - 1
    and s2.id = s3.id - 1
    and s1.people >= 100
    and s2.people >= 100
    and s3.people >= 100
),
n2 as (
    select one as id from n1
    union
    select two from n1
    union
    select three from n1
)
select * from stadium
where id in (
    select * from n2
)
order by visit_date