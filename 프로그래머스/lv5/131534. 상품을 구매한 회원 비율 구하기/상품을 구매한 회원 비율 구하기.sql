select year(o.sales_date) year, month(o.sales_date) month, count(distinct u.user_id) puchased_users, round(count(distinct u.user_id)/(select count(distinct user_id)
from user_info
where joined like '2021%'), 1) puchased_ratio
from user_info u
join online_sale o
where o.user_id=u.user_id and u.joined like '2021%'
group by year(o.sales_date), month(o.sales_date)
order by year, month