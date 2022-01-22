'''
M.R Application (Medical Records)

Follows a multiple inheritance structure, such that the mrapp.py file is the parent class of the:
- staff.py
- drugs.py
- prescriptions.py 
-appointments.py
- patients
classes

'''

from staff import staff
from appointments import appointments
from drugs import drugs
from prescriptions import prescriptions
from patients import patients
import sys
import os  

class mrapp(staff,appointments,drugs,prescriptions,patients):
    def getMenu():
        choice = 0
        while choice!= 10 :
            try:
                print('\t \t \t \t \t M.R Application')
                print('\t \t \t To view staff list enter : 1')
                print('\t \t \t To view drug inventory enter : 2')
                print('\t \t \t To appointment lists enter : 3')
                print('\t \t \t To view prescriptions enter : 4')
                print('\t \t \t To view patient listing enter : 5')
                print('\t \t \t To add a staff enter : 6')
                print('\t \t \t To add a drug to inventory enter : 7')
                print('\t \t \t To add a prescription enter : 8')
                print('\t \t \t To add a patient enter : 9')
                print('\t \t \t To exit/close the application enter : 10')
                print('\t \t \t \t Enter : ')
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
                if choice == 10 : sys.exit('Closing the Application.')
                if choice < 0 : 
                    raise ValueError
                if choice > 10 : 
                    raise ValueError
            except ValueError:
                print('Only Integer numbers between 1 - 10 should be entered in the main menu.')
            

    getMenu()






