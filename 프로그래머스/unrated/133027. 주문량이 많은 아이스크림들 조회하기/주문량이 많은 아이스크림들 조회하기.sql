select f.flavor
from first_half f
join (select flavor, sum(total_order) j_order
from july
group by flavor) as j
where f.flavor=j.flavor
order by f.total_order+j.j_order desc
limit 3