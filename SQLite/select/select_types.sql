CREATE TEMP TABLE Numbers(Val INTEGER);
INSERT INTO Numbers VALUES (1), (-3), (3), (0), (-5), (6);

select * from Numbers;

SELECT Val, 
    CASE 
        WHEN Val>0 THEN 'positive'
        WHEN Val < 0 THEN 'negative'
        ELSE 'zero' END FROM Numbers;
        

select cast(Val*5 as integer) as [v5] from Numbers;

CREATE TABLE tab1 (id INTEGER PRIMARY KEY NOT NULL, a INTEGER, b INTEGER);
insert into tab1 (a, b) values (5, 3), (10, 2), (11, 5);

select * from tab1;
select CAST(t1.a + t1.b AS integer) as [x] from tab1 as t1;
select CAST(t1.a + t1.b AS integer) as [x] from tab1 as t1 where rowid = 2;




CREATE TABLE tab2 (c int, b int REAL GENERATED ALWAYS AS (c*5));
insert into tab2 (c) values (5), (10), (11);
select * from tab2;

