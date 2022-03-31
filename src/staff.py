import sqlite3
class staff:
    def newStaff(self):
        fname = input("Enter forename: ")
        sname = input("Enter surname: ")
        occupation = input("Enter occupation: ")
        self.fname,self.sname,self.occupation = fname,sname,occupation
        return [self.fname,self.sname,self.occupation]
    
    def getStaff(self,records):
        for i in records:
            print(' Staff Number : {0} \n Forename : {1} \n Surname : {2} \n Occupation : {3} \n \n  '.format(i[0],i[1],i[2],i[3]))
