-- Write your query below
with product_a_buys as 
(
select customer_id, customer_name 
from customers c
where exists (
    select 1
    from orders o
    where c.customer_id = o.customer_id
    and o.product_name = 'A' 
)
),
product_b_buys as 
(
select customer_id, customer_name 
from customers c
where exists (
    select 1
    from orders o
    where c.customer_id = o.customer_id
    and o.product_name = 'B' 
)
),
product_c_buys as
(
select customer_id, customer_name 
from customers c
where exists (
    select 1
    from orders o
    where c.customer_id = o.customer_id
    and o.product_name = 'C' 
)
)
(select customer_id, customer_name
from product_a_buys
intersect
select customer_id, customer_name
from product_b_buys
)
except
select customer_id, customer_name
from product_c_buys
order by customer_name
