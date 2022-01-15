CREATE TABLE staff(
    Staff_ID INTEGER PRIMARY KEY,
    Forename varchar(50),
    Surname varchar(50),
    Department varchar(20),
    Occupation varchar(20)
);

DROP TABLE staff;
CREATE TABLE drug_inv(
    Drug_ID INTEGER PRIMARY KEY,
    Drug_Name varchar(50),
    Drug_Route varchar(50),
    Expiration_Date date, /* Date is in this format:' YYYY/MM/DD' */
    Stock int
);

INSERT INTO staff VALUES('2835','Carlos','Arro','I.T','I.T Support')
INSERT INTO staff(Forename,Surname,Department,Occupation) VALUES('Ray','Johnson','Doctor','General Practioner Doctor')
INSERT INTO staff VALUES('1432','Ryan','Bryson','Nurse','Junior Nurse')
INSERT INTO staff VALUES('12','Ryan','Bryson','Nurse','Junior Nurse')
SELECT * FROM staff;
SELECT * FROM patients;
INSERT INTO drug_inv(Drug_Name,Drug_Route,Expiration_Date,Stock)  VALUES('Panadol , pain reliver','Oral Capsule (325mg;500mg)','2022/10/12',250)
SELECT * FROM drug_inv
DROP TABLE drug_inv


CREATE TABLE patients(
    Patient_ID INTEGER  PRIMARY KEY,
    Name varchar(50),
    Age int(3),
    Height float,
    Weight DECIMAL(8,2),
    Medical_History Text
);

DROP TABLE patients
SELECT * FROM patients
INSERT INTO patients(Name,Age,Height,Weight,Medical_History) VALUES('Mary Lay',40,1.50,54.0,'N/A');
DELETE FROM patients WHERE Patient_ID = 2
PRAGMA foreign_keys=ON;
CREATE TABLE Prescriptions(
    Prescript_ID INTEGER PRIMARY KEY,
    Drug_ID INTEGER NOT NULL REFERENCES drug_inv(Drug_ID), 
    Doctor_ID INTEGER NOT NULL REFERENCES staff(Staff_ID),
    Patient_ID INTEGER NOT NULL REFERENCES patients(Patient_ID),
    Note TEXT, 
    Date date
);



/* Prescription Data test */
DROP TABLE Prescriptions
INSERT INTO Prescriptions(DRUG_ID,Doctor_ID,Patient_ID,Note,Date) VALUES(1,2836,1,'Take 2 every 6 hours','2022/01/15');
COMMIT;
INSERT INTO Prescriptions(DRUG_ID,Doctor_ID,Patient_ID,Note,Date) VALUES(1,2837,2,'Take 2 every 6 hours','2022/01/15');
COMMIT;

SELECT * FROM Prescriptions


/* CREATING Appointments table */ 

CREATE TABLE Appointments(
    Appoint_ID INTEGER PRIMARY KEY,
    Doctor_ID INTEGER,
    Patient_ID INTEGER, 
);