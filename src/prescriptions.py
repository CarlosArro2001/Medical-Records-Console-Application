import sqlite3
class prescriptions:
    def getPatients(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        query = ''' SELECT * FROM Prescriptions;'''
        li = list(cur.execute(query))
        for i in li:
            print(' Prescript_ID : {0} \n Drug_ID : {1} \n Doctor_ID : {2} \n Patient_ID : {3} \n Note : {4} \n Date : {5} '.format(i[0],i[1],i[2],i[3],i[4],i[5]))
