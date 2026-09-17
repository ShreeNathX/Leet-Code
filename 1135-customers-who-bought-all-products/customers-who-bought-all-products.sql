# Write your MySQL query statement below
select c.customer_id from customer c join product p
using(product_key)
group by c.customer_id
having count(distinct p.product_key) =
 (select count(distinct product_key) from product)