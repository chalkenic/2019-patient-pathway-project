CREATE TABLE IF NOT EXISTS 'contactFormUsers' (
    'ID' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'query' TEXT NOT NULL
);

INSERT INTO 'contactFormUsers'('query') VALUES ('How do I save my diary entry?');
INSERT INTO 'contactFormUsers'('query') VALUES ('How can I go about changing my password?');
INSERT INTO 'contactFormUsers'('query') VALUES ('Do I have to do the survey everyday?');
INSERT INTO 'contactFormUsers'('query') VALUES ('How do I change a previous diary entry?');
INSERT INTO 'contactFormUsers'('query') VALUES ('What do I do if I miss a day?');