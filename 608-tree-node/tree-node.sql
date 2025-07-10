# Write your MySQL query statement below
Select id, (Case when p_id is null then 'Root' when id in (Select p_id From Tree) then 'Inner' else 'Leaf' End) type
From Tree