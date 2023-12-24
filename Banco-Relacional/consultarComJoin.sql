select 
    e.nome as Estado,
    c.nome as Cidade, 
    e.regiao as Região 
from estados e, cidade c
where e.id = c.estado_id;

select 
    e.nome as Estado,
    c.nome as Cidade, 
    e.regiao as Região 
from estados e
inner join cidade c
    on e.id = c.estado_id