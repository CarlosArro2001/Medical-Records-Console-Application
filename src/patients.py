import sqlite3
class patients():
    def getPatients(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        query = ''' SELECT * FROM patients;'''
        staff_li = list(cur.execute(query))
        for i in staff_li:
            print(' Patient ID : {0} \n Name : {1} \n Age : {2} \n Sex : {3} \n Height : {4} \n Weight : {5} \n Medical History : {6}  '.format(i[0],i[1],i[2],i[3]))
