select o.animal_id, o.name
from animal_outs o join animal_ins i
where o.animal_id=i.animal_id and o.datetime<i.datetime
order by i.datetime