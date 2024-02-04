DROP TABLE tblUsers;
CREATE TABLE tblUsers (
	id 		INTEGER PRIMARY KEY NOT NULL,
	name 	TEXT NOT NULL,
	age 	INTEGER NOT NULL,
	address TEXT NOT NULL,
	last_apdate	TEXT DEFAULT (datetime('now')),
    UNIQUE (name)
);

DROP TABLE tblUsersLog;
CREATE TABLE tblUsersLog (	
	Id_tblUserLog INTEGER NOT NULL,
	name TEXT NOT NULL,
	operation TEXT NOT NULL,
	operation_date TEXT DEFAULT (datetime('now'))
);


DROP TABLE tblCalc;
CREATE TABLE tblCalc (	
	id INTEGER PRIMARY KEY NOT NULL,
	FK_tblCalc_tblUsers INTEGER NOT NULL,
	name TEXT DEFAULT NULL,
	initials TEXT,
	dage INTEGER,
	FOREIGN KEY (FK_tblCalc_tblUsers) REFERENCES tblUsers (id)
);

DROP TRIGGER IF EXISTS tgrCalcInsert;
CREATE TRIGGER tgrCalcInsert AFTER INSERT
	ON tblCalc
	BEGIN
		UPDATE tblCalc SET dage=(SELECT u.age*3 FROM tblUsers as u WHERE u.id = new.FK_tblCalc_tblUsers );
	END;



DROP TRIGGER IF EXISTS after_update;
CREATE TRIGGER after_update AFTER UPDATE
	ON tblUsers
	BEGIN
		INSERT INTO tblUsersLog (Id_tblUserLog, name, operation) VALUES (old.id, old.name, 'update');
	END;

INSERT INTO tblUsers (name, age, address) VALUES ('Смирнов', 25, 'Иваново');
INSERT INTO tblUsers (name, age, address) VALUES ('Муромец Илья', 33, 'Муром');
UPDATE tblUsers SET age = 24 WHERE name = 'Смирнов';
UPDATE tblUsers SET name = 'Смирнов Иван' WHERE name = 'Смирнов';

DELETE FROM tblCalc;
INSERT INTO tblCalc (FK_tblCalc_tblUsers, name) VALUES (2, 'xxx');
INSERT INTO tblCalc (FK_tblCalc_tblUsers, name) VALUES (1, 'aaa');


