select year(o.sales_date) year, month(o.sales_date) month, u.gender, count(distinct o.user_id) users
from online_sale o
join user_info u
where o.user_id=u.user_id and u.gender is not null
group by year(o.sales_date), month(o.sales_date), u.gender
order by year, month, gender