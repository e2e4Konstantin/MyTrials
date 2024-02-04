CREATE TABLE users (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	age INTEGER NOT NULL,
	address TEXT NOT NULL,
	mydate TEXT NOT NULL
);

CREATE TABLE user_log (
	Id_u INTEGER NOT NULL,
	u_date TEXT NOT NULL
);

CREATE TABLE user_log_stor (	
	Id_u INTEGER NOT NULL,
	u_date TEXT NOT NULL,
	name TEXT NOT NULL,
	operation TEXT NOT NULL
);


CREATE TRIGGER my_u_log_before BEFORE INSERT
	ON users
	BEGIN 
		INSERT INTO user_log (id_u, u_date) VALUES (NEW.id, datetime ('now')); 
	END;

INSERT INTO users (name, age, address, mydate)
	VALUES ('Пупкин', 27, 'Адрес', datetime ('now'));	

CREATE TRIGGER my_u_log_after AFTER INSERT
	ON users
	BEGIN
		INSERT INTO user_log (id_u, u_date) VALUES (NEW.id, datetime ('now'));
	END;	
	
INSERT INTO users (name, age, address, mydate)
	VALUES ('Смирнов', 33, 'Рязань', datetime ('now'));		
	

DROP TRIGGER after_update;
CREATE TRIGGER after_update AFTER UPDATE
	ON users
	BEGIN
		INSERT INTO user_log_stor (id_u, u_date, operation) VALUES (OLD.id, datetime ('now'), 'update');
	END;	