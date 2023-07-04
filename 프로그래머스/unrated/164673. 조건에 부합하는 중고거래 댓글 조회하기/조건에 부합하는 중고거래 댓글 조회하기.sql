select b.title, b.board_id, r.reply_id, r.writer_id, r.contents, date_format(r.created_date,'%Y-%m-%d')created_date
from used_goods_board as b, used_goods_reply as r
where b.board_id=r.board_id and b.created_date like '2022-10%'
order by r.created_date, b.title