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
    Doctor_name varchar(50),
    Patient_name varchar(50),
    Date date, /* Date is in this format:' YYYY/MM/DD' */
    Time varchar(7),
    Status varchar(9),
    CHECK(Status == 'pending' OR Status = 'Pending' OR Status == 'current' OR Status =='Current' OR Status =='completed' OR Status =='Completed')
);

DROP Table Appointments;

SELECT * FROM Appointments;
SELECT * FROM Staff;
SELECT * FROM patients;
SELECT * FROM Prescriptions;
SELECT * FROM drug_inv;
