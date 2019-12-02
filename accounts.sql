
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
	'date'	DATETIME NOT NULL,

	FOREIGN KEY (accountID) REFERENCES accounts(userID)
);

INSERT INTO 'accounts'('email_addr','name', 'password', 'access')VALUES('Alan@rickman','Alan','davetheMAN1','User');

INSERT INTO 'accounts'('email_addr','name', 'password', 'access')VALUES('nick@nick','Nick','Ineedabreak22','Nick');


INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,1,'Local authority',5, '2019-11-01');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,2,'Third sector',3, '2019-11-02');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,5,'Social',8, '2019-11-03');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,8,'Health',7, '2019-11-04');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,9,'Social',7, '2019-11-05');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,9,'Health',5, '2019-11-06');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,4,'Social Care',2, '2019-11-07');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Health',6, '2019-11-08');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Third sector',2, '2019-11-09');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,5,'Health',5, '2019-11-10');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,6,'Health',6, '2019-11-11');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,2,'Social',7, '2019-11-12');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,2,'Local authority',1, '2019-11-13');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,1,'Social',4, '2019-11-14');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,5,'Third sector',2, '2019-11-15');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,6,'Health',6, '2019-11-16');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,7,'Health',7, '2019-11-17');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,7,'Health',8, '2019-11-18');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,7,'Third sector',9, '2019-11-19');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,7,'Social',2, '2019-11-20');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,6,'Social care',4, '2019-11-21');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,6,'Health',4, '2019-11-22');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,4,'Health',3, '2019-11-23');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Health',4, '2019-11-24');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,4,'Own activities',2, '2019-11-25');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Social care',4, '2019-11-26');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,2,'Third sector',9, '2019-11-27');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,5,'Health',5, '2019-11-28');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,7,'Social care',6, '2019-11-29');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(2,7,'Social care',6, '2019-11-30');




SELECT surveyID, email_addr, happiness_q, date FROM surveyData
INNER JOIN accounts
ON surveyData.accountID=accounts.userID
WHERE userID = '1';
--SELECT surveyID, email_addr, happiness_q, date FROM surveyData
