select a.author_id, a.author_name, b.category, sum(s.sales*b.price) total_sales
from book_sales s
join author a, book b
where s.book_id=b.book_id and b.author_id=a.author_id and s.sales_date like '2022-01%'
group by a.author_id, b.category
order by a.author_id, b.category desc