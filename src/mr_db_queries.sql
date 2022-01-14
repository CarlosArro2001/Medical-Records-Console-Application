CREATE TABLE staff(
    Staff_ID int(4) PRIMARY KEY,
    Forename varchar(50),
    Surname varchar(50),
    Department varchar(20),
    Occupation varchar(20)
);

DROP TABLE drug_inv;
CREATE TABLE drug_inv(
    Drug_ID int(6) PRIMARY KEY,
    Drug_Name varchar(50),
    Drug_Route varchar(50),
    Expiration_Date date, /* Date is in this format:' YYYY/MM/DD' */
    Stock int
);

INSERT INTO staff VALUES('2835','Carlos','Arro','I.T','I.T Support')
INSERT INTO staff VALUES('1432','Ryan','Bryson','Nurse','Junior Nurse')
INSERT INTO staff VALUES('12','Ryan','Bryson','Nurse','Junior Nurse')
SELECT * FROM staff;

INSERT INTO drug_inv VALUES(1,'Panadol , pain reliver','Oral Capsule (325mg;500mg)','2022/10/12',250)
SELECT * FROM drug_inv


CREATE TABLE patients(
    Patient_ID int(6) AUTOINCREMENT PRIMARY KEY ,
    Name varchar(50),
    Age int(3),
    Height float,
    Weight DECIMAL(8,2),
    Medical_History Text
);

DROP table patients
INSERT INTO patients(Name,Age,Height,Weight,Medical_History)
VALUES('William Gate',1.62,60.2,'Has type 2 diabetes');

