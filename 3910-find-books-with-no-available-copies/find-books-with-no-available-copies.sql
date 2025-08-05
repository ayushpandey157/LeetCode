# Write your MySQL query statement below
with list as (select LB.*, count(*) as current_borrowers
from borrowing_records BR
left join library_books LB on BR.book_id = LB.book_id
where return_date is null
group by book_id, title, author, genre, publication_year)

select book_id, title, author, genre, publication_year, current_borrowers
from list where current_borrowers = total_copies
order by current_borrowers desc, title asc