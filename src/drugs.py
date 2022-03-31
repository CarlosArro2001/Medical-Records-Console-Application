import sqlite3
class drugs:
    #Calling the the drugs from the drug_inv table 
    def getdrugs(self,records):
        for i in records:
            print(' Drug ID : {0} \n Name : {1} \n Route : {2} \n Expiration Date : {3} \n Stock : {4} \n \n  '.format(i[0],i[1],i[2],i[3],i[4]))
        
    #Entering a new drug entry into the drug_inv table 
    def setDrugs(self):
        drug_name  = input(' Enter drug name : ')
        route = input('Enter route : ')
        expire = input('Enter Expiration date (YYYY/MM/DD) : ')
        stock = int(input('Enter stock'))
        self.name,self.route,self.expire,self.stock = drug_name,route,expire,stock
        return [self.name,self.route,self.expire,self.stock]
