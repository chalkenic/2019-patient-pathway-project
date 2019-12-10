
DROP TABLE IF EXISTS surveyData;
DROP TABLE IF EXISTS contactFormUsers;
DROP TABLE IF EXISTS accounts;



CREATE TABLE IF NOT EXISTS 'accounts' (
'userID'		   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
'email_addr'		TEXT NOT NULL,
'name'	            TEXT NOT NULL,
'password'	   TEXT NOT NULL,
'access'	        TEXT NOT NULL,
'volunteerID'	INTEGER NOT NULL UNIQUE
);

SELECT userID, email_addr FROM accounts WHERE Access = 'Admin';


CREATE TABLE IF NOT EXISTS 'surveyData' (
	'surveyID'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'accountID'	INTEGER,
	'happiness_q' INTEGER,
	'contact_q'  TEXT,
	'contact_op_q' INTEGER,
	'date'	DATETIME NOT NULL,

	FOREIGN KEY (accountID) REFERENCES accounts(userID)
);

CREATE TABLE IF NOT EXISTS 'contactFormUsers' (
    'messageID' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'accountID' INTEGER,
		'volunteer' INTEGER,
    'query' TEXT NOT NULL,
    'date' DATETIME NOT NULL,

		FOREIGN KEY (volunteer) REFERENCES accounts(volunteerID),
    FOREIGN KEY (accountID) REFERENCES accounts(userID)
);

INSERT INTO 'accounts'('email_addr','name', 'password', 'access', 'volunteerID')VALUES('Alan@rickman','Alan','davetheMAN1','User', 311267);

INSERT INTO 'accounts'('email_addr','name', 'password', 'access',  'volunteerID')VALUES('Nick@white','Nick','Ineedabreak22','Admin', 000001);

INSERT INTO 'accounts'('email_addr','name', 'password', 'access', 'volunteerID')VALUES('George@marks','George','iLOVEcomsoc2','User', 193692);

INSERT INTO 'accounts'('email_addr','name', 'password', 'access', 'volunteerID')VALUES('Harry@potter','Harry','iLOVEGinny<3','User', 145218);

INSERT INTO 'accounts'('email_addr','name', 'password', 'access', 'volunteerID')VALUES('Admin@admin','Admin','adminsAREtheb1','Admin', 000002);


INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,1,'Local authority',5, '2019-11-01');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,2,'Third sector',3, '2019-11-02');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,5,'Social',8, '2019-11-03');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Health',7, '2019-11-04');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,5,'Social',7, '2019-11-05');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,5,'Health',5, '2019-11-06');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,4,'Social Care',2, '2019-11-07');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Health',6, '2019-11-08');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Third sector',2, '2019-11-09');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,2,'Health',5, '2019-11-10');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,1,'Health',6, '2019-11-11');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,1,'Social',7, '2019-11-12');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,2,'Local authority',1, '2019-11-13');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,1,'Social',4, '2019-11-14');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Third sector',2, '2019-11-15');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Health',6, '2019-11-16');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,4,'Health',7, '2019-11-17');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Health',8, '2019-11-18');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Third sector',9, '2019-11-19');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Social',2, '2019-11-20');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,4,'Social care',4, '2019-11-21');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Health',4, '2019-11-22');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,4,'Health',3, '2019-11-23');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,2,'Health',4, '2019-11-24');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,2,'Own activities',2, '2019-11-25');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,2,'Social care',4, '2019-11-26');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,3,'Third sector',9, '2019-11-27');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,5,'Health',5, '2019-11-28');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,4,'Social care',6, '2019-11-29');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(1,5,'Social care',6, '2019-11-30');

INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Third sector',5, '2019-11-01');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Third sector',3, '2019-11-02');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Social',8, '2019-11-03');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Third sector',7, '2019-11-04');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,4,'Social',7, '2019-11-05');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Social',5, '2019-11-06');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Social Care',2, '2019-11-07');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,2,'Health',6, '2019-11-08');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,2,'Third sector',2, '2019-11-09');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,1,'Third sector',5, '2019-11-10');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,1,'Health',6, '2019-11-11');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,1,'Social',7, '2019-11-12');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Own activities',1, '2019-11-13');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,4,'Own activities',4, '2019-11-14');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,5,'Third sector',2, '2019-11-15');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,4,'Own activities',6, '2019-11-16');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,4,'Health',7, '2019-11-17');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,4,'Health',8, '2019-11-18');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Third sector',9, '2019-11-19');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,4,'Social',2, '2019-11-20');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,5,'Social care',4, '2019-11-21');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,5,'Health',4, '2019-11-22');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,4,'Social care',3, '2019-11-23');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Social care',4, '2019-11-24');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Own activities',2, '2019-11-25');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Social care',4, '2019-11-26');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,4,'Third sector',9, '2019-11-27');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,5,'Health',5, '2019-11-28');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,4,'Social care',6, '2019-11-29');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(3,3,'Social',6, '2019-11-30');

INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Third sector',5, '2019-11-01');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Third sector',3, '2019-11-02');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Social',8, '2019-11-03');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Third sector',7, '2019-11-04');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,4,'Social',7, '2019-11-05');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Social',5, '2019-11-06');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Social Care',2, '2019-11-07');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,2,'Health',6, '2019-11-08');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,2,'Third sector',2, '2019-11-09');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,1,'Third sector',5, '2019-11-10');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,1,'Health',6, '2019-11-11');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,1,'Social',7, '2019-11-12');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Own activities',1, '2019-11-13');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,4,'Own activities',4, '2019-11-14');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,5,'Third sector',2, '2019-11-15');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,4,'Own activities',6, '2019-11-16');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,4,'Health',7, '2019-11-17');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,4,'Health',8, '2019-11-18');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Third sector',9, '2019-11-19');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,4,'Social',2, '2019-11-20');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,5,'Social care',4, '2019-11-21');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,5,'Health',4, '2019-11-22');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,4,'Social care',3, '2019-11-23');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Social care',4, '2019-11-24');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Own activities',2, '2019-11-25');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Social care',4, '2019-11-26');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,4,'Third sector',9, '2019-11-27');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,5,'Health',5, '2019-11-28');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,4,'Social care',6, '2019-11-29');
INSERT INTO 'surveyData'('accountID','happiness_q','contact_q', 'contact_op_q', 'date')VALUES(4,3,'Social',6, '2019-11-30');

INSERT INTO 'contactFormUsers'('accountID', 'Volunteer','date', 'query') VALUES (1,311267, '2019-11-01','How do I save my diary entry?');
INSERT INTO 'contactFormUsers'('accountID', 'Volunteer','date','query') VALUES (3,193692,'2019-11-04','Do I have to do the survey everyday?');
INSERT INTO 'contactFormUsers'('accountID','Volunteer','date','query') VALUES (4,145218,'2019-11-06','How do I change a previous diary entry?');
INSERT INTO 'contactFormUsers'('accountID','Volunteer','date','query') VALUES (1,311267,'2019-11-07','What do I do if I miss a day?');
INSERT INTO 'contactFormUsers'('accountID','Volunteer','date','query') VALUES (1,311267,'2019-11-10','How do i cease my involvement in this project?');
INSERT INTO 'contactFormUsers'('accountID','Volunteer','date','query') VALUES (4,145218,'2019-11-18','Can i change a previous survey entry?');
INSERT INTO 'contactFormUsers'('accountID','Volunteer','date','query') VALUES (3,193692,'2019-11-24','Who are your affiliates?');


SELECT surveyID, email_addr, happiness_q, date FROM surveyData
INNER JOIN accounts
ON surveyData.accountID=accounts.userID
WHERE userID = '1';
--SELECT surveyID, email_addr, happiness_q, date FROM surveyData

SELECT count(userID) from accounts;
