select ed.id id, ed.genotype genotype, pd.genotype parent_genotype
from ecoli_data as ed join ecoli_data as pd on ed.parent_id=pd.id
where ed.genotype&pd.genotype=pd.genotype
order by id
