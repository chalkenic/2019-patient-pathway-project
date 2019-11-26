

CREATE TABLE IF NOT EXISTS 'contact_unassigned' (
'queryID'		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
'firstName'		TEXT NOT NULL,
'lastName'	    TEXT NOT NULL,
'emailAddress'  TEXT NOT NULL,
'query'	    TEXT NOT NULL
);
