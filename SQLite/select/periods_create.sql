DROP TABLE IF EXISTS tblPeriods;

CREATE TABLE tblPeriods (
    ID_tblPeriod INTEGER PRIMARY KEY NOT NULL,
    ID_parent  INTEGER REFERENCES tblPeriods (ID_tblPeriod), 
    start_date text collate nocase not null check(date(start_date, '+0 days') == start_date),
    end_date text collate nocase check(date(end_date, '+0 days') == end_date), 
    additive_num INTEGER NOT NULL,
    index_num INTEGER NOT NULL,
    type TEXT NOT NULL CHECK(type = 'Дополнение' OR type = 'Индекс'),
    description TEXT,
    holder TEXT CHECK(holder = 'main' OR holder = 'equipments' OR holder = 'monitoring'),
    UNIQUE (additive_num, index_num)
);

SELECT ID_parent, start_date, end_date, additive_num, index_num, type, description, holder FROM tblTest;
update tblTest set type='Индекс'  where type='Индекс';
update tblTest set type='Дополнение'  where type='Дополнение ';


INSERT INTO tblPeriods (ID_parent, start_date, end_date, additive_num, index_num, type, description, holder)
SELECT ID_parent, start_date, end_date, additive_num, index_num, type, description, holder FROM tblTest;


select * from pragma_table_info('tblPeriods') as tblInfo;  

INSERT INTO tblPeriods (ID_parent, start_date, end_date, additive_num, index_num, type, description, holder) VALUES 
(null, '2019-01-10', Null, 51, 147, 'Дополнение', Null, 'main'),
(null, '2018-12-24', Null, 50, 147, 'Индекс', Null, 'main');

INSERT INTO tblPeriods (ID_parent, start_date, end_date, additive_num, index_num, type, description, holder) VALUES 
(null, '2019-01-25', Null, 51, 148, 'Индекс', Null, 'main'),
(null, '2019-02-22', Null, 51, 149, 'Индекс', Null, 'main'),
(null, '2019-03-25', Null, 51, 150, 'Индекс', Null, 'main'),
(null, '2019-04-01', Null, 52, 150, 'Дополнение', Null, 'main'),

(null, '2019-04-25', Null, 52, 151, 'Индекс', Null, 'main'),
(null, '2019-05-27', Null, 52, 152, 'Индекс', Null, 'main'),
(null, '2019-06-25', Null, 52, 153, 'Индекс', Null, 'main'),
(null, '2019-07-02', Null, 53, 153, 'Дополнение', Null, 'main'),

(null, '2019-07-22', Null, 53, 154, 'Индекс', Null, 'main'),
(null, '2019-07-23', Null, 53, 155, 'Индекс', Null, 'main'),
(null, '2019-08-02', Null, 53, 156, 'Индекс', Null, 'main'),
(null, '2019-09-10', Null, 54, 156, 'Дополнение', Null, 'main'),

(null, '2019-10-01', Null, 54, 157, 'Индекс', Null, 'main'),
(null, '2019-11-11', Null, 55, 157, 'Дополнение', Null, 'main'),

(null, '2019-11-25', Null, 55, 158, 'Индекс', Null, 'main'),
(null, '2019-12-02', Null, 55, 159, 'Индекс', Null, 'main'),
(null, '2020-01-21', Null, 55, 160, 'Индекс', Null, 'main'),
(null, '2020-02-03', Null, 56, 160, 'Дополнение', Null, 'main'),

(null, '2020-02-20', Null, 56, 161, 'Индекс', Null, 'main'),
(null, '2020-03-04', Null, 56, 162, 'Индекс', Null, 'main'),
(null, '2020-04-15', Null, 56, 163, 'Индекс', Null, 'main'),
(null, '2020-05-15', Null, 56, 164, 'Индекс', Null, 'main'),
(null, '2020-06-08', Null, 57, 164, 'Дополнение', Null, 'main'),

(null, '2020-06-15', Null, 57, 165, 'Индекс', Null, 'main'),
(null, '2020-07-17', Null, 57, 166, 'Индекс', Null, 'main'),
(null, '2020-08-12', Null, 57, 167, 'Индекс', Null, 'main'),
(null, '2020-09-14', Null, 57, 168, 'Индекс', Null, 'main'),
(null, '2020-09-17', Null, 58, 168, 'Дополнение', Null, 'main'),

(null, '2020-10-19', Null, 58, 169, 'Индекс', Null, 'main'),
(null, '2020-11-12', Null, 59, 169, 'Дополнение', Null, 'main'),

(null, '2020-11-19', Null, 59, 170, 'Индекс', Null, 'main'),
(null, '2020-12-17', Null, 59, 171, 'Индекс', Null, 'main'),
(null, '2021-01-18', Null, 59, 172, 'Индекс', Null, 'main'),
(null, '2021-02-15', Null, 59, 173, 'Индекс', Null, 'main'),
(null, '2021-02-16', Null, 60, 173, 'Дополнение', Null, 'main'),

(null, '2021-03-16', Null, 60, 174, 'Индекс', Null, 'main'),
(null, '2021-04-15', Null, 60, 175, 'Индекс', Null, 'main'),
(null, '2021-05-17', Null, 60, 176, 'Индекс', Null, 'main'),
(null, '2021-05-24', Null, 61, 176, 'Дополнение', Null, 'main'),

(null, '2021-06-17', Null, 61, 177, 'Индекс', Null, 'main'),
(null, '2021-07-17', Null, 61, 178, 'Индекс', Null, 'main'),
(null, '2021-07-17', Null, 61, 179, 'Индекс', Null, 'main'),
(null, '2021-08-25', Null, 62, 179, 'Дополнение', Null, 'main'),

(null, '2021-09-16', Null, 62, 180, 'Индекс', Null, 'main'),
(null, '2021-10-18', Null, 62, 181, 'Индекс', Null, 'main'),
(null, '2021-11-18', Null, 62, 182, 'Индекс', Null, 'main'),
(null, '2021-11-23', Null, 63, 182, 'Дополнение', Null, 'main'),

(null, '2021-12-15', Null, 63, 183, 'Индекс', Null, 'main'),
(null, '2022-01-18', Null, 63, 184, 'Индекс', Null, 'main'),
(null, '2022-02-16', Null, 63, 185, 'Индекс', Null, 'main'),
(null, '2022-03-03', Null, 64, 185, 'Дополнение', Null, 'main'),

(null, '2022-03-17', Null, 64, 186, 'Индекс', Null, 'main'),
(null, '2022-04-18', Null, 64, 187, 'Индекс', Null, 'main'),
(null, '2022-05-19', Null, 64, 188, 'Индекс', Null, 'main'),
(null, '2022-05-30', Null, 65, 188, 'Дополнение', Null, 'main'),

(null, '2022-06-20', Null, 65, 189, 'Индекс', Null, 'main'),
(null, '2022-07-20', Null, 65, 190, 'Индекс', Null, 'main'),
(null, '2022-08-17', Null, 65, 191, 'Индекс', Null, 'main'),
(null, '2022-09-05', Null, 66, 191, 'Дополнение', Null, 'main'),

(null, '2022-09-20', Null, 66, 192, 'Индекс', Null, 'main'),
(null, '2022-10-19', Null, 66, 193, 'Индекс', Null, 'main'),
(null, '2022-11-17', Null, 66, 194, 'Индекс', Null, 'main'),
(null, '2022-12-15', Null, 66, 195, 'Индекс', Null, 'main'),
(null, '2022-11-21', Null, 67, 195, 'Дополнение', Null, 'main'),

(null, '2023-01-19', Null, 67, 196, 'Индекс', Null, 'main'),
(null, '2023-02-13', Null, 68, 196, 'Дополнение', Null, 'main'),

(null, '2023-02-17', Null, 68, 197, 'Индекс', Null, 'main'),
(null, '2023-03-17', Null, 68, 198, 'Индекс', Null, 'main'),
(null, '2023-04-14', Null, 68, 199, 'Индекс', Null, 'main'),
(null, '2023-05-16', Null, 68, 200, 'Индекс', Null, 'main'),
(null, '2023-05-22', Null, 69, 200, 'Дополнение', Null, 'main'),

(null, '2023-06-15', Null, 69, 201, 'Индекс', Null, 'main'),
(null, '2023-07-18', Null, 69, 202, 'Индекс', Null, 'main'),
(null, '2023-08-11', Null, 69, 203, 'Индекс', Null, 'main'),
(null, '2023-09-18', Null, 69, 204, 'Индекс', Null, 'main'),
(null, '2023-10-31', Null, 69, 205, 'Индекс', Null, 'main'),
(null, '2023-10-31', Null, 70, 205, 'Дополнение', Null, 'main'),

(null, '2023-11-15', Null, 70, 206, 'Индекс', Null, 'main'),
(null, '2023-12-14', Null, 70, 207, 'Индекс', Null, 'main'),
(null, '2024-01-11', Null, 71, 207, 'Дополнение', Null, 'main'),

(null, '2024-01-19', Null, 71, 208, 'Индекс', Null, 'main');

INSERT INTO tblPeriods (ID_parent, start_date, end_date, additive_num, index_num, type, description, holder) VALUES 
(null, '2019-01-10', Null, 51, 147, 'Дополнение', Null, 'main'),
(null, '2018-12-24', Null, 50, 147, 'Индекс', Null, 'main');


SELECT * FROM tblPeriods;
SELECT * FROM tblPeriods AS m WHERE (m.additive_num = 51 OR m.additive_num = 50) AND (m.index_num = 148 OR m.index_num = 147);
SELECT * FROM tblPeriods AS m WHERE (m.additive_num = 50 AND m.index_num = 147) OR (m.additive_num = 51 AND m.index_num = 146);

SELECT * FROM tblPeriods;

SELECT ID_tblPeriod FROM tblPeriods as p WHERE p.additive_num = 51 AND p.index_num = 147;
SELECT ID_tblPeriod FROM tblPeriods as p WHERE 
        ((p.additive_num = 51-1 AND p.index_num = 147) OR
        (p.additive_num = 51 AND p.index_num = 147-1));

UPDATE software
SET purchprice = c.purchprice
FROM (SELECT purchprice, id FROM softwarecost) AS c
WHERE c.id = software.id;

UPDATE software
SET purchprice = (SELECT purchprice
                  FROM softwarecost
                  WHERE id = software.id) 
where EXISTS (SELECT purchprice
                  FROM softwarecost
                  WHERE id = software.id);


UPDATE tblPeriods SET ID_parent = NULL;

UPDATE tblPeriods 
SET ID_parent = p.ID_tblPeriod, end_date = p.start_date
FROM (SELECT * FROM tblPeriods) as p
WHERE 
    (
        (p.additive_num = tblPeriods.additive_num-1 AND p.index_num = tblPeriods.index_num ) OR
        (p.additive_num = tblPeriods.additive_num AND p.index_num = tblPeriods.index_num-1)
    );    

DROP VIEW IF EXISTS viewPeriods;
CREATE VIEW viewPeriods AS
    SELECT 
    m.start_date AS [Start], m.end_date AS [End],
    m.additive_num AS [Add], m.index_num AS [Idx],
    m.type AS [Type], m.description AS [Remark], m.holder AS [Part],
    s.additive_num AS [prev.Add],  s.index_num  AS [prev.Idx]
    
    FROM tblPeriods AS m
    LEFT JOIN tblPeriods AS s ON s.ID_tblPeriod = m.ID_parent
    ORDER BY m.additive_num DESC, m.index_num DESC; 

SELECT * FROM viewPeriods;

SELECT 
    m.start_date AS [Start], m.end_date AS [End],
    m.additive_num AS [Add], m.index_num AS [Idx],
    m.type AS [Type], m.description AS [Remark], m.holder AS [Part],
    s.additive_num AS [prev.Add],  s.index_num  AS [prev.Idx]
    
FROM tblPeriods AS m
LEFT JOIN tblPeriods AS s ON s.ID_tblPeriod = m.ID_parent
ORDER BY m.additive_num DESC, m.index_num DESC;     --,   







select date('now', '+5 days');
---- year
--where date between '2019' and '2019x'
---- month of year
--where date between '2019-03'  and '2019-03x'
---- day of month of year
--where date between '2019-03-14' and '2019=03-14x'
---- or just
--where date = '2019-03-14'
