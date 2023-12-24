INSERT INTO empresas
    (nome, cnpj)
VALUES
    ('Bradesco', 95469722819828),
    ('Vale', 93480138174620),
    ('Cielo', 39013789257137);

select * from prefeito;
select * from empresas;
select * from cidade;

INSERT INTO empresas_unidades
    (empresa_id, cidade_id, sede)
VALUES
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1);
