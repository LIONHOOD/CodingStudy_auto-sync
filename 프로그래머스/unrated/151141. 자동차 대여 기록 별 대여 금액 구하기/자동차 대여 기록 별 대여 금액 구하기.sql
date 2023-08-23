select x.history_id, round(x.duration*x.daily_fee*(1-ifnull(d.discount_rate,0)*0.01)) fee
    from (select h.history_id, c.car_type, c.daily_fee, datediff(h.end_date, h.start_date)+1 duration,
    case when datediff(h.end_date, h.start_date)+1>=90 then '90일 이상'
    when datediff(h.end_date, h.start_date)+1>=30 then '30일 이상'
    when datediff(h.end_date, h.start_date)+1>=7 then '7일 이상'
    else '-' end duration_type
    from car_rental_company_rental_history h
    join car_rental_company_car c on h.car_id=c.car_id
    where c.car_type='트럭') x
left join car_rental_company_discount_plan d on (x.duration_type,x.car_type)=(d.duration_type,d.car_type)
order by fee desc, history_id desc
