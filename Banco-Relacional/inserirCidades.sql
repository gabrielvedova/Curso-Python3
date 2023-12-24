SELECT * FROM cidade

INSERT INTO cidade(nome, area, estado_id)
VALUES
    ('Campinas', 795, 24),
    ('Niterói', 133.9, 24),
    ('Caruaru', 920.6, (select id from estados where sigla = 'PE'))

INSERT INTO cidade(nome, area, estado_id)
VALUES (
    'Juazeiro do Norte',
    248.2,
    (select id from estados where sigla = 'CE')
)
