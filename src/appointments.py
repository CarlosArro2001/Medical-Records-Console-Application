import sqlite3
class appointments:

    #Calling the the appointments from the appointments table and storing them into a list to output 
    def getAppointments(self,records):
        for i in records:
            print(' Appointment ID : {0} \n Date : {1} \n Time : {2} \n Doctor Name : {3} \n Patient Name : {4} \n Status {5} \n\n'.format(i[0],i[3],i[4],i[1],i[2],i[5]))


    def setAppointments(self):
        doctor = input(' Enter dooctor name: ')
        patient = input(' Enter patient name: ')
        date = input(' Enter date (YYYY/MM/DD): ')
        time = input(' Enter time (HH:MM am/pm): ')
        status = input('Enter the status of this appointment (Pending/current/completed): ')
        self.doctor,self.patient,self.date,self.time,self.status=doctor,patient,date,time,status
        return [self.doctor,self.patient,self.date,self.time,self.status]