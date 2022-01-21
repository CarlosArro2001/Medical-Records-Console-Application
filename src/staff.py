import sqlite3
class staff:
    
    def getStaff(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        query = ''' SELECT * FROM staff;'''
        staff_li = list(cur.execute(query))
        for i in staff_li:
            print(' Staff Number : {0} \n Forename : {1} \n Surname : {2} \n Occupation : {3} \n \n  '.format(i[0],i[1],i[2],i[3]))
    
    def setStaff(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        fname = input('Enter forename: ')
        sname = input('Enter Surname: ')
        occupation = input('Enter Occupation: ')
        cur.execute("INSERT INTO Staff(Forename,Surname,Occupation) VALUES (?,?,?)",(fname,sname,occupation))
        con.commit()
        print('New entry added')
