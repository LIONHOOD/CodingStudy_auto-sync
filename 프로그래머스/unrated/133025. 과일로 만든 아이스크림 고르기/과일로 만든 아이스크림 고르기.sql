select f.flavor
from first_half as f
left join icecream_info as i
on f.flavor=i.flavor
where 3000<f.total_order and i.ingredient_type like 'fruit%'
order by f.total_order desc