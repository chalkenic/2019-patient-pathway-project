CREATE TABLE IF NOT EXISTS 'contactFormUsers' (
    'ID' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'firstName' TEXT NOT NULL,
    'lastName' TEXT NOT NULL,
    'email' TEXT NOT NULL,
    'query' TEXT NOT NULL
);