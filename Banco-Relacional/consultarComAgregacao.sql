-- Soma da populacao por região
select
    regiao as 'Região',
    sum(populacao) as Total
from `estados`
GROUP BY regiao
order by Total desc


-- Média da populacao por estado
select
    avg(populacao) as Total
from `estados`