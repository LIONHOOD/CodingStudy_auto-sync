select u.user_id, u.nickname, concat(u.city,' ',u.street_address1,' ',u.street_address2) 전체주소,
concat(left(u.tlno,3),'-',right(left(u.tlno,7),4),'-',right(u.tlno,4)) 전화번호
from used_goods_board b
join used_goods_user u
where b.writer_id=u.user_id
group by b.writer_id
having count(b.writer_id)>2
order by b.writer_id desc