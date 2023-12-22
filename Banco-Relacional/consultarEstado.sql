SELECT * FROM estados

SELECT nome, sigla from estados
WHERE regiao='Sul'

SELECT nome, sigla from estados
where populacao >= 10
order by populacao desc