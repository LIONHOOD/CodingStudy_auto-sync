select *
from (select c2.car_id, c2.car_type, floor(daily_fee*30*(1-p.discount_rate/100))fee
from car_rental_company_car c2
join car_rental_company_discount_plan p
where c2.car_type=p.car_type and c2.car_id not in (select c.car_id
from car_rental_company_rental_history h
join car_rental_company_car c
where h.car_id=c.car_id and ((h.start_date between '2022-11-01' and '2022-11-30') or (h.end_date between '2022-11-01' and '2022-11-30') or '2022-11-01' between h.start_date and h.end_date)) and p.duration_type='30일 이상') t
where 500000<=t.fee and t.fee<2000000
order by t.fee desc, car_type, car_id desc