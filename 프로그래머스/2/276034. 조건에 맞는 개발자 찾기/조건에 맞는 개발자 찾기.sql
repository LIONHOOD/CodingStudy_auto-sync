select id, email, first_name, last_name
from developers
where skill_code&1280>=256
order by id