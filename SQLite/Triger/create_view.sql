CREATE TABLE IF NOT EXISTS tblStorageCostsXX
            -- таблица для % Заготовительно-складских расходов (%ЗСР)
            (
                ID_tblStorageCosts      INTEGER PRIMARY KEY NOT NULL,
                percent_storage_costs   REAL NOT NULL DEFAULT 0.0 CHECK(percent_storage_costs >= 0 AND percent_storage_costs <= 100), -- Процент ЗСР
                name                    TEXT NOT NULL,  -- Наименование		
                description             TEXT NOT NULL,  -- подробное описание
                last_update             INTEGER NOT NULL DEFAULT (UNIXEPOCH('now')),	
                UNIQUE (name)
            );

DROP VIEW IF EXISTS viewTest;            
CREATE VIEW viewTest AS
    SELECT
        m.storage_costs AS [ЗСР],
        (m.storage_costs * 2) AS [2*ЗСР],
        m.name,
        m.last_update
    FROM tblPropertiesMachines AS m;


SELECT * FROM tblPropertiesMachines AS m;


