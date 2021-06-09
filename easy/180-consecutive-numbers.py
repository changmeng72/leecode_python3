# Write your MySQL query statement below

select distinct a.num as ConsecutiveNums from logs a 
join logs b on b.id = a.id +1  
join logs c on c.id = b.id +1  
where a.num=b.num and a.num=c.num