CREATE TABLE IF NOT EXISTS 'adminContact' (
    'ID' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'query' TEXT NOT NULL
);

INSERT INTO 'adminContact'('query') VALUES ('Some user data needs updating, how can we go about ammending this?');
INSERT INTO 'adminContact'('query') VALUES ('I need to export data, is this possible currently?');
INSERT INTO 'adminContact'('query') VALUES ('Some suggested inprovements, can we schedule a meeting?');
INSERT INTO 'adminContact'('query') VALUES ('Is there a way to recover lost data?');
INSERT INTO 'adminContact'('query') VALUES ('Can we go and push some new improvements or do they need to be approved?');