'''
M.R Application (Medical Records)

Follows a multiple inheritance structure, such that the mrapp.py file is the parent class of the:
- staff.py
- drugs.py
- prescriptions.py 
-appointments.py
classes

'''

from staff import staff
from appointments import appointments
from drugs import drugs
from prescriptions import prescriptions
import sys
import os  

class mrapp(staff,appointments,drugs,prescriptions):
    def getMenu():
        choice = 0
        while choice!= 5 :
            try:
                print('\t \t \t \t \t M.R Application')
                print('\t \t \t To view staff list enter : 1')
                print('\t \t \t To view drug inventory enter : 2')
                print('\t \t \t To appointment lists enter : 3')
                print('\t \t \t To view prescriptions enter : 4')
                print('\t \t \t To exit/close the application enter : 5')
                print('\t \t \t \t Enter : ')
                st = staff()
                dr = drugs()
                ap = appointments()
                pr = prescriptions()
                choice = int(input(''))
                if choice == 1 : st.getStaff()
                if choice == 2 : dr.getdrugs()
                if choice == 3 : ap.getAppointments()
                if choice == 4 : pr.getPrescriptions()
                if choice == 5 : sys.exit('Closing the Application.')
                if choice < 0 : 
                    raise ValueError
                if choice > 5 : 
                    raise ValueError
            except ValueError:
                print('Only Integer numbers between 1 - 5 should be entered in the main menu.')
            

    getMenu()






