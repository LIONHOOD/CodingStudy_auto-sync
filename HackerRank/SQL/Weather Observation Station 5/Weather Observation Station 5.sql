(select city, length(city) len
from station
order by len, city
limit 1)
union
(select city, length(city) len
from station
order by len desc, city
limit 1); 
