select o.product_id, p.product_name, sum(p.price*o.amount)total_sales
from food_order o
join food_product p
where o.product_id=p.product_id and o.produce_date like '2022-05%'
group by o.product_id
order by total_sales desc, product_id 