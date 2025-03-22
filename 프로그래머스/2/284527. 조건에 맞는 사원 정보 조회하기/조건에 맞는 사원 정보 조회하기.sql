select sum(hg.score) as score, hg.emp_no, he.emp_name, he.position, he.email
from hr_employees as he join hr_grade as hg on he.emp_no=hg.emp_no
where hg.year=2022
group by hg.emp_no
order by 1 desc
limit 1