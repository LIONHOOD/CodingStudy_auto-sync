select b.book_id, a.author_name, date_format(b.published_date, '%Y-%m-%d') published_date
from book b join author a where b.author_id=a.author_id and b.category='경제'
order by b.published_date