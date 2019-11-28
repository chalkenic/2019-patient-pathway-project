
DROP TABLE IF EXISTS surveyData;
DROP TABLE IF EXISTS accounts;

CREATE TABLE IF NOT EXISTS 'accounts' (
'userID'		   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
'email_addr'		TEXT NOT NULL,
'name'	            TEXT NOT NULL,
'password'	   TEXT NOT NULL,
'access'	        TEXT NOT NULL
);

SELECT userID, email_addr FROM accounts WHERE Access = 'Admin';

--SELECT date ('now');

CREATE TABLE IF NOT EXISTS 'surveyData' (
	'surveyID'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'accountID'	INTEGER,
	'happiness_q' INTEGER,
	'contact_q'  TEXT,
	'contact_op_q' INTEGER,
	'date'	DATETIME DEFAULT current_timestamp NOT NULL,
	FOREIGN KEY (accountID) REFERENCES accounts(userID)
);

INSERT INTO 'accounts'('email_addr','name', 'password', 'access')VALUES('Alan@rickman','Alan','davetheMAN1','User');

INSERT INTO 'accounts'('email_addr','name', 'password', 'access')VALUES('nick@nick','Nick','Ineedabreak22','Nick');


INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,1,'Local authority',5);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,2,'3rd sector',3);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,5,'Social',8);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,8,'Health',7);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,9,'Social',7);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,9,'Health',5);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,4,'Social Care',2);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,3,'Health',6);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,3,'3rdSector',2);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,5,'Health',5);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,6,'Health',6);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,2,'Social',7);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,2,'Local authority',1);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,1,'Social',4);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,5,'3rd sector',2);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,6,'Health',6);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,7,'Health',7);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,7,'Health',8);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,7,'3rd sector',9);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,7,'Social',2);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,6,'Social care',4);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,6,'Health',4);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,4,'Health',3);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,3,'Health',4);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,4,'Own activities',2);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,3,'Social care',4);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,2,'3rdSector',9);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,5,'Health',5);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(1,7,'Social care',6);
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q')VALUES(2,7,'Social care',6);




SELECT surveyID, email_addr, happiness_q, date FROM surveyData
INNER JOIN accounts
ON surveyData.accountID=accounts.userID
