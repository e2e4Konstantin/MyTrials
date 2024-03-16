DROP TABLE IF EXISTS tblStorageCosts;

CREATE TABLE IF NOT EXISTS tblStorageCosts (
    ID_tblStorageCosts    INTEGER PRIMARY KEY NOT NULL,
    percent_storage_costs REAL    NOT NULL DEFAULT 0.0,-- Процент ЗСР
    name                  TEXT    NOT NULL,-- Наименование
    description           TEXT    NOT NULL,-- Комментарий
    last_update           INTEGER NOT NULL DEFAULT (UNIXEPOCH('now') ),
    UNIQUE (name)
);

	
INSERT INTO tblStorageCosts (percent_storage_costs, name, description) VALUES 
	( 1.3,'По умолчанию', 'Значение по умолчанию, используется если не установлено действительное значение'),
	( 2,'Строй_мат', 'к строительным материалам, кроме металлических конструкций'),
	( 0.75,'Метал_констр', 'к металлическим конструкциям'),
	( 1.2,'Оборудование', 'к оборудованию');
INSERT INTO tblStorageCosts (percent_storage_costs, name, description) VALUES 
	( 200, 'по ...', 'Значение по ...');
 
DROP TABLE IF EXISTS tblPropertiesMachines;	
CREATE TABLE IF NOT EXISTS tblPropertiesMachines (
        ID_tblPropertiesMachine    INTEGER PRIMARY KEY NOT NULL,
        FK_tblPropertiesMachine_tblStorageCosts INTEGER NOT NULL,
        name TEXT,	
        storage_costs REAL NOT NULL DEFAULT 0.0,       -- id ЗСР%, Заготовительно-складские расходы (Purchasing and storage costs)                          
        last_update INTEGER NOT NULL DEFAULT (UNIXEPOCH('now')),	
        FOREIGN KEY (FK_tblPropertiesMachine_tblStorageCosts) REFERENCES tblStorageCosts (ID_tblStorageCosts),
        UNIQUE (name)
);		

DELETE FROM tblPropertiesMachines;

INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES (2,'машина 1');
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES (4,'машина 4');
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name) VALUES (3,'машина 33');

INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name, storage_costs) 
    SELECT 2,'машина 1', percent_storage_costs FROM tblStorageCosts WHERE ID_tblStorageCosts = 2;
    

     
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name, storage_costs) 
    SELECT 3,'машина 2', percent_storage_costs FROM tblStorageCosts WHERE ID_tblStorageCosts = 3;
    
INSERT INTO tblPropertiesMachines (FK_tblPropertiesMachine_tblStorageCosts, name, storage_costs) 
    SELECT 4,'машина 3', percent_storage_costs FROM tblStorageCosts WHERE ID_tblStorageCosts = 4;


DROP TABLE IF EXISTS tblHistoryMachines;
CREATE TABLE IF NOT EXISTS tblHistoryMachines
    (
        ID_HistoryMachine INTEGER PRIMARY KEY NOT NULL,
        _rowid INTEGER,
        name TEXT,	
        val  REAL,
        last_update    INTEGER NOT NULL DEFAULT (UNIXEPOCH('now'))
    );

DROP TRIGGER IF EXISTS tgrCheckInsert;
CREATE TRIGGER tgrCheckInsert before INSERT 
on tblStorageCosts
    begin
        select case when new.percent_storage_costs > 100 THEN
            RAISE(Abort, 'Слишком много %. Число должно быть меньше 100.')
        END; 
    end;

-- ID_tblPropertiesMachine, FK_tblPropertiesMachine_tblStorageCosts, name, storage_costs

DROP TRIGGER IF EXISTS tgrPropertiesMachinesIU;
CREATE TRIGGER tgrPropertiesMachinesIU 
    AFTER INSERT ON tblPropertiesMachines
    BEGIN       
        UPDATE tblPropertiesMachines SET 
            storage_costs = (
                SELECT percent_storage_costs 
                FROM tblStorageCosts 
                WHERE ID_tblStorageCosts = new.FK_tblPropertiesMachine_tblStorageCosts
            )
                 
        WHERE ID_tblPropertiesMachine=new.ID_tblPropertiesMachine;              
    END;

DROP TRIGGER IF EXISTS tgrPropertiesMachinesUpdate;
CREATE TRIGGER tgrPropertiesMachinesUpdate AFTER UPDATE 
    OF FK_tblPropertiesMachine_tblStorageCosts ON tblPropertiesMachines
    WHEN new.FK_tblPropertiesMachine_tblStorageCosts <> old.FK_tblPropertiesMachine_tblStorageCosts
    BEGIN            
        UPDATE tblPropertiesMachines SET 
            storage_costs = (SELECT percent_storage_costs FROM tblStorageCosts 
        WHERE ID_tblStorageCosts = new.FK_tblPropertiesMachine_tblStorageCosts) 
        WHERE ID_tblPropertiesMachine=new.ID_tblPropertiesMachine;              
    END;

DROP TRIGGER IF EXISTS tgrStorageCostsUpdate;
CREATE TRIGGER tgrStorageCostsUpdate AFTER UPDATE 
    OF percent_storage_costs ON tblStorageCosts 
    FOR EACH ROW
    BEGIN
        UPDATE tblPropertiesMachines SET storage_costs = new.percent_storage_costs
        WHERE FK_tblPropertiesMachine_tblStorageCosts = new.ID_tblStorageCosts;
    END;    

    






