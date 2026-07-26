-- Write your query below
select name 
from customers as cust
left join orders as ord
on cust.id = ord.customer_id
where ord.customer_id is null