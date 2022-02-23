'''
M.R Application (Medical Records)

Follows a multiple inheritance structure, such that the mrapp.py file is the parent class of the:
- staff.py
- drugs.py
- prescriptions.py 
- appointments.py
- patients.py
classes

'''

from staff import staff
from appointments import appointments
from drugs import drugs
from prescriptions import prescriptions
from patients import patients
from authentication import authentication
import sys

class mrapp(staff,appointments,drugs,prescriptions,patients):
    def getMenu():
        #LOGIN SECTION:
        auth = authentication()
        print('-------------- Medical Records Console App LOGIN --------------')
        counter = 3
        while(auth.login() == False):
            auth.login()
            if(auth.login() == True):
                break
            else: 
                counter -= 1
                print('Login attempts left : {0}/3 .'.format(counter))
            if(counter <= 0):
                print('Used all login attempts.')
                sys.exit('Closing application')
            
        # Displaying the main menu 
        choice = 0
        while choice!= 11:
            try:
                print('\t \t \t \t \t Medical Records  Application')
                print('\t \t \t To view staff list enter : 1')
                print('\t \t \t To view drug inventory enter : 2')
                print('\t \t \t To appointment lists enter : 3')
                print('\t \t \t To view prescriptions enter : 4')
                print('\t \t \t To view patient listing enter : 5')
                print('\t \t \t To add a staff enter : 6')
                print('\t \t \t To add a drug to inventory enter : 7')
                print('\t \t \t To add a prescription enter : 8')
                print('\t \t \t To add a patient enter : 9')
                print('\t \t \t To add an appointment enter : 10')
                print('\t \t \t To exit/close the application enter : 11')
                st = staff()
                dr = drugs()
                ap = appointments()
                pr = prescriptions()
                pt = patients()
                choice = int(input(''))
                if choice == 1 : st.getStaff()
                if choice == 2 : dr.getdrugs()
                if choice == 3 : ap.getAppointments()
                if choice == 4 : pr.getPrescriptions()
                if choice == 5 : pt.getPatients()
                if choice == 6 : st.setStaff()
                if choice == 7 : dr.setDrugs()
                if choice == 8 : pr.setPrescriptions()
                if choice == 9 : pt.setPatients()
                if choice == 10 : ap.setAppointments()
                if choice == 11 : sys.exit('Closing the application')
                if choice < 0 : 
                    raise ValueError
                if choice > 10 : 
                    raise ValueError
            except ValueError:
                print('Only Integer numbers between 1 - 10 should be entered in the main menu.')
            

    getMenu()






