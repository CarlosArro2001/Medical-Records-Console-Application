import sqlite3
class appointments:

    #Calling the the appointments from the appointments table and storing them into a list to output 
    def getAppointments(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        query = ''' SELECT * from Appointments'''
        app_list = list(cur.execute(query))
        for i in app_list:
            print(' Appointment ID : {0} \n Date : {1} \n Time : {2} \n Doctor Name : {3} \n Patient Name : {4} \n Status {5} \n\n'.format(i[0],i[3],i[4],i[1],i[2],i[5]))
        con.close()

    def setAppointments(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        #The user will enter: Doctor_name, Patient_Name, Date, Time, Status.
        doctor = input(' Enter dooctor name: ')
        patient = input(' Enter patient name: ')
        date = input(' Enter date (YYYY/MM/DD): ')
        time = input(' Enter time (HH:MM am/pm): ')
        status = input('Enter the status of this appointment (Pending/current/completed): ')
        cur.execute('INSERT INTO Appointments(Doctor_Name,Patient_Name,Date,Time,Status) VALUES(?,?,?,?,?)',(doctor,patient,date,time,status))        
        con.commit()
        print('New entry added')
        con.close()