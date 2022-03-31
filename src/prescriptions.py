import sqlite3
class prescriptions:
    #Returning the prescriptions from prescriptions table and storing them into a list
    def getPrescriptions(self,records):
        for i in records:
            print(' Prescript_ID : {0} \n Drug Name : {1} \n Doctor : {2} \n Patient Name : {3} \n Note : {4} \n Date : {5} '.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    
    #Entering a prescription entry into the prescription table 
    def setPrescriptions(self):
        Drug_Name = input('Enter drug name: ')
        Doctor_Name = input('Enter Doctor : ')
        Patient_Name = input('Patient Name : ')
        Note = input('Enter notes : ')
        Date = input('Enter date (YYYY/MM/DD)')
        self.drug,self.doctor,self.patient,self.note,self.date = Drug_Name,Doctor_Name,Patient_Name,Note,Date
        return [self.drug,self.doctor,self.patient,self.note,self.date]