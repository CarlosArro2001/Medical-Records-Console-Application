import sqlite3
class staff:
    
    def getStaff(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        query = ''' SELECT * FROM staff;'''
        staff_li = list(cur.execute(query))
        for i in staff_li:
            print(' Staff Number : {0} \n Forename : {1} \n Surname : {2} \n Department : {3} \n Occupation : {4} \n \n  '.format(i[0],i[1],i[2],i[3],i[4]))
        