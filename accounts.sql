
CREATE TABLE IF NOT EXISTS 'Accounts' (
'AccountID'		   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
'Username'	   TEXT NOT NULL,
'Password'	   TEXT NOT NULL,
'Access'	   TEXT NOT NULL
);

SELECT AccountID, Username FROM Accounts WHERE Access = 'ADMIN';

SELECT date ('now');

CREATE TABLE IF NOT EXISTS 'surveyData' (
	'SurveyID'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'AccountID'	INTEGER,
	'Date'	DATETIME DEFAULT current_timestamp NOT NULL,
	FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);

SELECT * FROM surveyData

