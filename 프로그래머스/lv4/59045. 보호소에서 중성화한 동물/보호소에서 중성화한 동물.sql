select o.animal_id, o.animal_type, o.name
from animal_outs o
join animal_ins i
where o.animal_id=i.animal_id and i.sex_upon_intake like 'Intact%' and (o.sex_upon_outcome like 'Spayed%' or o.sex_upon_outcome like 'Neutered%')
