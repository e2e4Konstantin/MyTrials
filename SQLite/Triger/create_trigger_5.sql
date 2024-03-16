DROP TABLE IF EXISTS tblStorageCosts;
CREATE TABLE IF NOT EXISTS tblStorageCosts
	-- таблица для % Заготовительно-складских расходов (%ЗСР)
	(
		ID_tblStorageCosts      INTEGER PRIMARY KEY NOT NULL,
		percent_storage_costs   REAL NOT NULL DEFAULT 0.0, -- Процент ЗСР
		name                    TEXT NOT NULL,  -- Наименование		
		description             TEXT NOT NULL, -- Комментарий
		--last_update             INTEGER NOT NULL DEFAULT (UNIXEPOCH('now')),	
		UNIQUE (name)
	);
	
INSERT INTO tblStorageCosts (percent_storage_costs, name, description) VALUES 
	( 1.3,'по умолчанию', 'Значение по умолчанию, используется если не установлено действительное значение'),
	( 2,'Строй_мат', 'к строительным материалам, кроме металлических конструкций'),
	( 0.75,'Метал_констр', 'к металлическим конструкциям'),
	( 1.2,'Оборудование', 'к оборудованию');	

DROP TABLE IF EXISTS tblPropertiesMachines;	
CREATE TABLE IF NOT EXISTS tblPropertiesMachines
    (
        ID_tblPropertiesMachine    INTEGER PRIMARY KEY NOT NULL,
        FK_tblPropertiesMachine_tblStorageCosts INTEGER NOT NULL,
        name TEXT,	
        tr_storage_costs    REAL NOT NULL DEFAULT 0.0,       -- id ЗСР%, Заготовительно-складские расходы (Purchasing and storage costs)                          
--        last_update    INTEGER NOT NULL DEFAULT (UNIXEPOCH('now')),	
        FOREIGN KEY (FK_tblPropertiesMachine_tblStorageCosts) REFERENCES tblStorageCosts (ID_tblStorageCosts),
        UNIQUE (name)
    );	
    

DROP TABLE IF EXISTS tblHistoryMachines;
CREATE TABLE IF NOT EXISTS tblHistoryMachines
    (
        ID_HistoryMachine INTEGER PRIMARY KEY NOT NULL,
        _rowid INTEGER,
        name TEXT,	
        val  REAL
--        last_update    INTEGER NOT NULL DEFAULT (UNIXEPOCH('now'))
    );

 
DROP TRIGGER IF EXISTS tgrPropertiesMachinesInsert;

CREATE TRIGGER tgrPropertiesMachinesInsert AFTER INSERT
    ON tblPropertiesMachines
    BEGIN
        UPDATE tblPropertiesMachines SET tr_storage_costs=
            (SELECT percent_storage_costs FROM tblStorageCosts WHERE ID_tblStorageCosts = new.FK_tblPropertiesMachine_tblStorageCosts)
        where ID_tblPropertiesMachine=new.ID_tblPropertiesMachine;
        
        INSERT INTO tblHistoryMachines (_rowid, name, val) 
            VALUES (new.rowid, new.name, (SELECT percent_storage_costs FROM tblStorageCosts WHERE ID_tblStorageCosts = new.FK_tblPropertiesMachine_tblStorageCosts));
    END;

DROP TRIGGER IF EXISTS tgrPropertiesMachinesUpdate;

CREATE TRIGGER tgrPropertiesMachinesUpdate AFTER UPDATE 
    ON tblPropertiesMachines
    FOR EACH ROW        
    BEGIN            
        UPDATE tblPropertiesMachines SET tr_storage_costs = 55.5 WHERE ID_tblPropertiesMachine=new.ID_tblPropertiesMachine;    
    END;





INSERT OR IGNORE INTO tblHistoryMachines (_rowid, name, val) 
            SELECT old.rowid, old.name, old.tr_storage_costs 
            WHERE EXISTS(SELECT 1 FROM tblHistoryMachines WHERE name = old.name);












SELECT EXISTS(SELECT 1 FROM tblHistoryMachines WHERE name = 'машина 11_');


/*
CREATE TRIGGER tgrPropertiesMachinesUpdate AFTER UPDATE 
    ON tblPropertiesMachines 
    --WHEN  (0 < (SELECT Count() FROM tblHistoryMachines WHERE name = old.name))
         
    BEGIN
        select old.name;
        INSERT INTO tblHistoryMachines (_rowid, name, val) VALUES (old.rowid, old.name, old.tr_storage_costs);
    END;
*/
--SELECT COUNT() AS nameCount FROM (SELECT * FROM tblHistoryMachines as cc WHERE  cc.name = old.name) 
--SELECT COUNT() AS r FROM (SELECT name FROM tblHistoryMachines WHERE name = 'машина 11');

--(SELECT Count() FROM tblHistoryMachines WHERE name = 'машина 11');


DROP TRIGGER IF EXISTS tgrStorageCosts;
CREATE TRIGGER tgrStorageCosts
    AFTER UPDATE OF percent_storage_costs ON tblStorageCosts 
    FOR EACH ROW
    BEGIN
        UPDATE tblPropertiesMachines SET tr_storage_costs=NEW.percent_storage_costs
        WHERE FK_tblPropertiesMachine_tblStorageCosts=NEW.ID_tblStorageCosts;
    END;
    
 
SELECT percent_storage_costs FROM tblStorageCosts WHERE ID_tblStorageCosts = 2 LIMIT 1;
SELECT * FROM tblPropertiesMachines where ID_tblPropertiesMachine=2;
UPDATE tblPropertiesMachines SET name='машина new' where ID_tblPropertiesMachine=2;



delete from tblPropertiesMachines;

INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES ( 2,'машина 1');
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES ( 3,'машина 2');
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES ( 1, 'машина 99');   
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES ( 1, 'машина 11');  
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES ( 4, 'машина 77');  
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES ( 1, 'машина 33');    
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES ( 3,'машина 595');
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES ( 2,'машина 45987');
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES ( 4,'машина 44');

INSERT INTO dogs (name, shots) SELECT 'Brutus', 'true'
   WHERE NOT EXISTS(SELECT 1 FROM dogs WHERE name='Brutus');




select name || '--XX' from tblPropertiesMachines;



SELECT c.ID_tblStorageCosts, c.percent_storage_costs, m.FK_tblPropertiesMachine_tblStorageCosts, m.tr_storage_costs, m.name FROM tblPropertiesMachines as m
join tblStorageCosts as c ON c.ID_tblStorageCosts = m.FK_tblPropertiesMachine_tblStorageCosts;



INSERT OR REPLACE INTO `table` (`unique_col`, `some_col`)
  VALUES ('unique_val', COALESCE((
    SELECT 'some_col_new_val' FROM `table`
    WHERE `unique_col` = 'unique_val'
  ), 'some_column_default_val'));