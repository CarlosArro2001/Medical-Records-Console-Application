'''
Date : 23/02/2022
Author: Carlos Raniel Ariate Arro 
Changes : 
    1. Implemented the getpass module and function for the password input in register and login methods 

Note: 
username = Carlos 
password = solrac2001
'''
import getpass
import sqlite3 
from cryptography.fernet import Fernet 
import getpass
class authentication:

    def register(self):
        conn = sqlite3.connect('mrdb.db')
        cur = conn.cursor()
        user =  input('Enter username: ')
        passw = bytes(getpass.getpass('Enter a password: '),'utf-8')
        role = ''
        flag = False
        while(flag == False):
            role = input('Enter role: ')
            if(role in ['Admin','Senior Staff','IT'] == False):print('Invalid Role, enter either : Admin , Senior Staff or IT ')
            else: flag = True
        key = Fernet.generate_key()
        cur.execute("INSERT INTO users (user_name,user_pass,user_role,pass_key) VALUES (?,?,?,?)",(user,Fernet(key).encrypt(passw),role,key))
        conn.commit()
        conn.close()
        print("User added")

    def login(self):
        conn = sqlite3.connect('mrdb.db')
        cur = conn.cursor()
        user = input('Enter username : ')
        passw = bytes(getpass.getpass('Enter password : '),'utf-8')
        key = None
        temp_li = list(cur.execute('SELECT * FROM users'))
        for i in temp_li:
            key = i[4]
            if((user == i[1]) and (Fernet(key).decrypt(i[2])==passw)):
                print("Successful login")
                return True
            else:
                print('Invalid username or password')
                return False

# auth = authentication()
# auth.register()