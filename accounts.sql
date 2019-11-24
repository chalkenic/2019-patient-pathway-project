

CREATE TABLE IF NOT EXISTS 'accounts' (
'AccountID'		   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
'email_addr'		TEXT NOT NULL,
'Name'	            TEXT NOT NULL,
'Password'	   TEXT NOT NULL,
'Access'	        TEXT NOT NULL
);

SELECT AccountID, email_addr FROM accounts WHERE Access = 'Admin';

SELECT date ('now');

CREATE TABLE IF NOT EXISTS 'surveyData' (
	'SurveyID'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'AccountID'	INTEGER,
	'Date'	DATETIME DEFAULT current_timestamp NOT NULL,
	FOREIGN KEY (AccountID) REFERENCES accounts(AccountID)
);

SELECT * FROM surveyData

