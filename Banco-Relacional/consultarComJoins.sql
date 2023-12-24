select * from prefeito;
select * from cidade;

select * from cidade c inner join prefeito p on c.id = p.cidade_id;
select * from cidade c left join prefeito p on c.id = p.cidade_id;
select * from cidade c right join prefeito p on c.id = p.cidade_id;

-- Forma de usar o full join porque essa função n é suportada no sql;

select * from cidade c left join prefeito p on c.id = p.cidade_id
union
select * from cidade c right join prefeito p on c.id = p.cidade_id;