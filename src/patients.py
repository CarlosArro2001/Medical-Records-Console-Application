import sqlite3
class patients():
    def getPatients(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        query = ''' SELECT * FROM patients;'''
        staff_li = list(cur.execute(query))
        for i in staff_li:
            print(' Patient ID : {0} \n Name : {1} \n Age : {2} \n Sex : {3} \n Height : {4} \n Weight : {5} \n Medical History : {6}  \n'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

    def setPatients(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        name = input('Enter patient name :')
        age = int(input('Enter patient age :'))
        sex = input('Enter sex of patient (M/F) : ')
        height = float(input('Enter height (meters) :'))
        weight = float(input('Enter weight (kg) :'))
        medical_history = input('Enter medical history : ')
        cur.execute('INSERT INTO patients(name,age,sex,height,weight,medical_history) VALUES(?,?,?,?,?,?)',(name,age,sex,height,weight,medical_history))
        con.commit()
        print('New entry added')