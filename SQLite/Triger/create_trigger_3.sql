DROP TABLE IF EXISTS datausage;

Create table if not exists datausage (
	Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
	mainentry text, 
	stime integer , 
	endtime integer, 
	usedtime integer
);

CREATE TRIGGER IF NOT EXISTS datausage_timedifference AFTER INSERT ON datausage
    BEGIN
        UPDATE datausage SET usedtime = endtime - stime WHERE id = new.id;
    END;

CREATE TRIGGER IF NOT EXISTS datausage_update AFTER UPDATE ON datausage
    BEGIN
        UPDATE datausage SET usedtime = endtime - stime WHERE id = new.id;
    END;
	
	
	
	

INSERT INTO datausage VALUES 
	(null,'mainentry1',10,30,0),
	(null,'mainentry2',50,75,0);

INSERT INTO datausage VALUES (null,'mainentry 3', 88,99,0);

SELECT * FROM datausage;	
	
SELECT *, endtime - stime AS alternative_usedtime FROM datausage;