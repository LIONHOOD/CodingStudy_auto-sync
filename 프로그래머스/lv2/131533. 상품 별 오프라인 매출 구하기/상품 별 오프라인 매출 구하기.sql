select p.product_code, sum(o.sales_amount*p.price) as sales
from offline_sale o join product p
where o.product_id=p.product_id
group by p.product_code
order by sales desc, p.product_code