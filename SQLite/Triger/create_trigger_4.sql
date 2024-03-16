DROP TABLE IF EXISTS tblStorageCosts;
CREATE TABLE IF NOT EXISTS tblStorageCosts
	-- таблица для % Заготовительно-складских расходов (%ЗСР)
	(
		ID_tblStorageCosts      INTEGER PRIMARY KEY NOT NULL,
		percent_storage_costs   REAL NOT NULL DEFAULT 0.0, -- Процент ЗСР
		name                    TEXT NOT NULL,  -- Наименование		
		description             TEXT NOT NULL, -- Комментарий
		last_update             TEXT NOT NULL DEFAULT (datetime('now')),	
		UNIQUE (name)
	);
	
INSERT INTO tblStorageCosts (percent_storage_costs, name, description) VALUES 
	( 0,'по умолчанию', 'Значение по умолчанию, используется если не установлено действительное значение'),
	( 2,'Строй_мат', 'к строительным материалам, кроме металлических конструкций'),
	( 0.75,'Метал_констр', 'к металлическим конструкциям'),
	( 1.2,'Оборудование', 'к оборудованию');	
	
CREATE TABLE IF NOT EXISTS tblPropertiesMachines
	-- таблица для свойств Машин Глава 1.
	-- поля tr_storage_costs и tr_transportation_cost вычисляются по триггеру
	(
		ID_tblPropertiesMachine             	INTEGER PRIMARY KEY NOT NULL,
		FK_tblPropertiesMachine_tblStorageCosts INTEGER NOT NULL,
		name TEXT,	
		tr_storage_costs           	REAL NOT NULL DEFAULT 0.0,       -- id ЗСР%, Заготовительно-складские расходы (Purchasing and storage costs)                          
		last_update 				TEXT NOT NULL DEFAULT (datetime('now')),	
		FOREIGN KEY (FK_tblPropertiesMachine_tblStorageCosts) REFERENCES tblStorageCosts (ID_tblStorageCosts)
	);
	
DROP TRIGGER IF EXISTS tgrPropertiesMachinesInsert;
CREATE TRIGGER tgrPropertiesMachinesInsert AFTER INSERT
	ON tblPropertiesMachines
	BEGIN
		UPDATE tblPropertiesMachines SET tr_storage_costs=(SELECT percent_storage_costs FROM tblStorageCosts WHERE ID_tblStorageCosts = new.FK_tblPropertiesMachine_tblStorageCosts);
	END;

	
DROP TRIGGER IF EXISTS tgrPropertiesMachinesUpdate;
CREATE TRIGGER tgrPropertiesMachinesUpdate AFTER UPDATE
	ON tblPropertiesMachines
	BEGIN
		UPDATE tblPropertiesMachines SET tr_storage_costs=(SELECT percent_storage_costs FROM tblStorageCosts WHERE ID_tblStorageCosts = new.FK_tblPropertiesMachine_tblStorageCosts);
	END;	


	
	
	
	
	