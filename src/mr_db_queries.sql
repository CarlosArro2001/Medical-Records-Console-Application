CREATE TABLE staff(
    Staff_ID INTEGER PRIMARY KEY,
    Forename varchar(50),
    Surname varchar(50),
    Occupation varchar(20)
);

CREATE TABLE drug_inv(
    Drug_ID INTEGER PRIMARY KEY,
    Drug_Name varchar(50),
    Drug_Route varchar(50),
    Expiration_Date date, /* Date is in this format:' YYYY/MM/DD' */
    Stock int
);


CREATE TABLE patients(
    Patient_ID INTEGER  PRIMARY KEY,
    Name varchar(50),
    Age int(3),
    sex varchar(1),
    Height float,
    Weight DECIMAL(8,2),
    Medical_History Text,
    CHECK(sex == 'M' or sex == 'm' or sex == 'F' or sex == 'f')
);

CREATE TABLE Prescriptions(
    Prescript_ID INTEGER PRIMARY KEY,
    Drug_Name varchar(50), 
    Doctor_Name varchar(50),
    Patient_Name varchar(50),
    Note TEXT, 
    Date date /* Date is in this format:' YYYY/MM/DD' */
);
/* CREATING Appointments table */ 

CREATE TABLE Appointments(
    Appoint_ID INTEGER PRIMARY KEY,
    Doctor_ID INTEGER REFERENCES staff(Staff_ID),
    Patient_ID INTEGER REFERENCES patients(Patient_ID),
    Prescript_ID INTEGER REFERENCES Prescriptions(Prescript_ID),
    Date date,
    Time varchar(7),
    Status varchar(9),
    CHECK(Status == 'pending' OR Status =='Current' OR Status =='Completed')
);

DROP Table Prescriptions

SELECT * FROM Appointments;
SELECT * FROM Staff;
SELECT * FROM Prescriptions;
SELECT * FROM patients;
SELECT * FROM drug_inv;
