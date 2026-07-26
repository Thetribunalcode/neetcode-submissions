-- Write your query below
with highest_score as 
(
    select student_id, max(score) as score
    from exam_results
    group by student_id
)
select er.student_id, min(er.exam_id) as exam_id, max(hs.score) as score
from
exam_results er
inner join
highest_score hs
on er.student_id = hs.student_id and er.score = hs.score
group by er.student_id
order by er.student_id asc