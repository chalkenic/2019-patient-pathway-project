CREATE TABLE IF NOT EXISTS 'contactForm' (
    'ID' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'firstName' TEXT NOT NULL,
    'lastName' TEXT NOT NULL,
    'email' TEXT NOT NULL,
    'query' TEXT NOT NULL
);

INSERT INTO 'contactForm'('firstName','lastName', 'email', 'query' ) VALUES ('Ian','Cooper','IanC@cardiff.ac.uk', 'What does the diary do?');
INSERT INTO 'contactForm'('firstName','lastName', 'email', 'query' ) VALUES ('Dan','Cooper','DanC@cardiff.ac.uk', 'How can I register for this service?');
INSERT INTO 'contactForm'('firstName','lastName', 'email', 'query' ) VALUES ('Mike','Halloway','MikeH@cardiff.ac.uk', 'I need to update my personal infomation but I dont have login details');
INSERT INTO 'contactForm'('firstName','lastName', 'email', 'query' ) VALUES ('Abdi','Omar','AbdiO@cardiff.ac.uk', 'Can you tell me more about the partnership?');
INSERT INTO 'contactForm'('firstName','lastName', 'email', 'query' ) VALUES ('Tom','Rowbotham','TomR@cardiff.ac.uk', 'Where are you located?');
INSERT INTO 'contactForm'('firstName','lastName', 'email', 'query' ) VALUES ('Osama','Ilays','OsamaI@cardiff.ac.uk', 'How can I contact you?');