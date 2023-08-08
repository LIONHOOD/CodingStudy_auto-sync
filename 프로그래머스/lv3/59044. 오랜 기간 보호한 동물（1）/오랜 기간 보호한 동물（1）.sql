select name, datetime
from animal_ins
where animal_id not in (select i.animal_id
from animal_outs o join animal_ins i
where o.animal_id=i.animal_id)
order by datetime
limit 3