select count(*) as fish_count
from fish_info as fi join fish_name_info as fn on fi.fish_type=fn.fish_type
where fn.fish_name in ('BASS','SNAPPER')