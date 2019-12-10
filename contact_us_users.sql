DROP TABLE IF EXISTS contactFormUsers;

CREATE TABLE IF NOT EXISTS 'contactFormUsers' (
    'ID' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'accountID' INTEGER,
    'query' TEXT NOT NULL,
    'date' DATETIME NOT NULL,

    FOREIGN KEY (accountID) REFERENCES accounts(userID)
);

INSERT INTO 'contactFormUsers'('accountID', 'date', 'query') VALUES (1,'2019-11-01','How do I save my diary entry?');
INSERT INTO 'contactFormUsers'('accountID', 'date','query') VALUES (3,'2019-11-04','Do I have to do the survey everyday?');
INSERT INTO 'contactFormUsers'('accountID','date','query') VALUES (4,'2019-11-06','How do I change a previous diary entry?');
INSERT INTO 'contactFormUsers'('accountID','date','query') VALUES (1,'2019-11-07','What do I do if I miss a day?');
INSERT INTO 'contactFormUsers'('accountID','date','query') VALUES (1,'2019-11-10','How do i cease my involvement in this project?');
INSERT INTO 'contactFormUsers'('accountID','date','query') VALUES (4,'2019-11-18','Can i edit my previous survey entry?');
INSERT INTO 'contactFormUsers'('accountID','date','query') VALUES (3,'2019-11-24','Who are your affiliates?');
