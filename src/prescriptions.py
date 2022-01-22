import sqlite3
class prescriptions:
    def getPrescriptions(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        query = ''' SELECT * FROM Prescriptions;'''
        li = list(cur.execute(query))
        for i in li:
            print(' Prescript_ID : {0} \n Drug Name : {1} \n Doctor : {2} \n Patient Name : {3} \n Note : {4} \n Date : {5} '.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    
    def setPrescriptions(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        Drug_Name = input('Enter drug name: ')
        Doctor_Name = input('Enter Doctor : ')
        Patient_Name = input('Patient Name : ')
        Note = input('Enter notes : ')
        Date = input('Enter date (YYYY/MM/DD)')
        con.execute('INSERT INTO Prescriptions(Drug_Name,Doctor_Name,Patient_Name,Note,Date) VALUES(?,?,?,?,?)',(Drug_Name,Doctor_Name,Patient_Name,Note,Date))
        con.commit()
        print('New entry added.')