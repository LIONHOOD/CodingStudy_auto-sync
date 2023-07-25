select animal_id
from animal_ins
where not isnull(name)
order by animal_id