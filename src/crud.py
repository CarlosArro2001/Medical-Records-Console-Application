import sqlite3
class crud:
    def createStaff(self,details):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        cur.execute("INSERT INTO Staff(Forename,Surname,Occupation) VALUES(?,?,?)",(details[0],details[1],details[2]))
        con.commit()
        print("Entry added")
        con.close() 

    def returnStaff(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        staff_records = list(cur.execute(''' SELECT * from staff'''))
        return staff_records
        
    
    def createDrug(self,drug):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        cur.execute('INSERT INTO drug_inv(Drug_Name,Drug_Route,Expiration_Date,Stock) VALUES(?,?,?,?)',(drug[0],drug[1],drug[2],drug[3]))
        con.commit()
        print('New entry added')
        con.close()
    
    def returnDrugs(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        drug_records = list(cur.execute('''SELECT * from drug_inv'''))
        return drug_records
    
    def createAppointment(self,appointment):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        cur.execute("INSERT INTO Appointments(Doctor_name,Patient_name,Date,Time,Status) VALUES(?,?,?,?,?)",(appointment[0],appointment[1],appointment[2],appointment[3],appointment[4]))
        con.commit()
        print("Entry added")
        con.close()

    def returnAppointment(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        appointment_records = list(cur.execute('''SELECT * from Appointments'''))
        return appointment_records

    def createPatient(self,patient):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        cur.execute('INSERT INTO patients(name,age,sex,height,weight,medical_history) VALUES(?,?,?,?,?,?)',(patient[0],patient[1],patient[2],patient[3],patient[4],patient[5]))
        con.commit()
        print('New entry added')

    def returnPatients(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        patient_records = list(cur.execute('''SELECT * from patients'''))
        return patient_records
    
    def createPrescription(self,prescription):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        con.execute('INSERT INTO Prescriptions(Drug_Name,Doctor_Name,Patient_Name,Note,Date) VALUES(?,?,?,?,?)',(prescription[0],prescription[1],prescription[2],prescription[3],prescription[4]))
        con.commit()
        print('New entry added')

    def returnPrescriptions(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        query = ''' SELECT * FROM Prescriptions;'''
        prescriptions_records = list(cur.execute(query))
        return prescriptions_records
    
    
