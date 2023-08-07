select animal_id, name
from animal_outs
where animal_id not in (select o.animal_id
from animal_outs o join animal_ins i
where o.animal_id=i.animal_id)
