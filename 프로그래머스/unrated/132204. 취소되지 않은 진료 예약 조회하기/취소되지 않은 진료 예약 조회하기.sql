select a.apnt_no, p.pt_name, p.pt_no, d.mcdp_cd, dr_name, apnt_ymd
from appointment a
join patient p, doctor d
where a.pt_no=p.pt_no and a.mddr_id=d.dr_id and a.apnt_ymd like '2022-04-13%' and a.apnt_cncl_yn='N'
order by a.apnt_ymd