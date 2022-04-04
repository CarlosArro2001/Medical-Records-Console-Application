# Medical Records Console Application
 

### Installation

#### Prequisites

- Install python from https://www.python.org/.

- Use the following command to clone this repo : <br/>
 > git clone https://github.com/CarlosArro2001/Medical-Records-Console-Application.git
 > or simply download as a zip file:<br> 
  code -> 'Download ZIP'


### Overview
This is a medical records console application, this allows to the authenticated user to : 
1. C.R.U.D operations for records such as : 
    - Patients
    - Drug Inventory
    - Staff
    - Prescriptions 
    - users 

2. Login and Register of users 
    - Where registering users is limited to only specifc authenticated users 

#### Flowchart
![Flowchart:](https://github.com/CarlosArro2001/Medical-Records-Console-Application/blob/main/models/FlowChartDiagram.jpg?raw=true)

#### Functions and classes explained

1. mrapp class :  This class is used to navigate through the app and contains one function.
    -  getMenu(self) - Displays the login screen, and the main menu right after a succesfully login

2. crud class : This class is used to communicate with the sqlite database (mrdb.db) and contains 10 function, to put it simply, each function will either enter data into the database or return data from the database, for each of the following categories : staff, drugs, appointments, patients & prescriptions.
    
    - createStaff(self,details) : takes an details array as an arguement and elements from details will be stored in 'Staff' in the database.

    - returnStaff(self) : returns all records from the "Staff" table in the form of an array.

    - createDrug(self,drug) : takes a drug array as an arguement and elements from details will be stored in 'drug_inv' table in the database.

    - returnDrugs(self) : returns all records from the "drug_inv" table in the form of an array.

    - createAppointment(self,appointment) : takes a appointment array as an arguement and elements from details will be stored in 'Appointments' table in the database.

    - returnAppointment(self) : returns all records from the "Appointments" table in the form of an array.
    
    - createPatients(self,patient) : takes a patient array as an arguement and elements from details will be stored in 'patients' table in the database.

    - returnPatients(self) : returns all records from the "patients" table in the form of an array.

    - createPrescriptions(self,prescription) : takes a prescription array as an arguement and elements from details will be stored in 'Prescriptions' table in the database.

    - returnPrescriptions(self) : returns all records from the "Prescriptions" table in the form of an array.

3. drugs class : Class used to handle data pertaining to drug records from the 'drug_inv' table and contains two functions.
    
    - getDrugs(self,records): prints the drug records from the records arguement using a loop, the records arguement is expected to be a return array value from the returnDrug() function.

    - setDrugs(self): Asks the user to input details of the drug which will be stored as its property and all those properties will be returned as an array for the createDrug() function.

4. patients class : Class used to handle data pertaining to patient records from the 'patients' table and contains two functions.
    
    - getPatients(self,records): prints the patient records from the records arguement using a loop, the records arguement is expected to be a return array value from the returnPatients() function.

    - setPatients(self): Asks the user to input details of the patient which will be stored as its property and all those properties will be returned as an array for the createPatient() function.

5. prescriptions class : Class used to handle data pertaining to prescription records from the prescription table and contains two functions.
    
    - getPrescriptions(self,records): prints the prescription records from the records arguement using a loop, the records arguement is expected to be a return array value from the returnPrescriptions() function.

    - setPrescription(self): Asks the user to input details of the prescription which will be stored as its property and all those properties will be returned as an array for the createPrescription() function.

6. appointments class : Class used to handle data pertaining to appointment records from the appointments table and contains two functions.
    
    - getAppointment(self,records): prints the appointment records from the records arguement using a loop, the records arguement is expected to be a return array value from the returnAppointment() function.

    - setAppointment(self): Asks the user to input details of the appointment which will be stored as it's property and all those properties will be returned as an array for the createAppointment() function.

7. staff class : Class used to handle data pertaining to staff records from the staff table and contains two functions.
    
    - getStaff(self,records): prints the staff records from the records arguement using a loop, the records arguement is expected to be a return array value from the returnStaff() function.

    - setStaff(self): Asks the user to input details of the staff which will be stored as it's property and all those properties will be returned as an array for the createStaff() function.

#### Note from the author : 

> This project will never be fully completed as the code will change as I learn more coding practices and improve on my skills, so updates will be expected.














