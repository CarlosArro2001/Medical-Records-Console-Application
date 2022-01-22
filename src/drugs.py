import sqlite3
class drugs:
    def getdrugs(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        query = ''' SELECT * FROM drug_inv'''
        drugs_li = list(cur.execute(query))
        for i in drugs_li:
            print(' Drug ID : {0} \n Name : {1} \n Route : {2} \n Expiration Date : {3} \n Stock : {4} \n \n  '.format(i[0],i[1],i[2],i[3],i[4]))
    
    def setDrugs(self):
        con = sqlite3.connect('mrdb.db')
        cur = con.cursor()
        drug_name  = input(' Enter drug name : ')
        route = input('Enter route : ')
        expire = input('Enter Expiration date (YYYY/MM/DD) : ')
        stock = int(input('Enter stock'))
        cur.execute('INSERT INTO drug_inv(Drug_Name,Drug_Route,Expiration_Date,Stock) VALUES(?,?,?,?)',(drug_name,route,expire,stock))
        con.commit()
        print('New entry added')