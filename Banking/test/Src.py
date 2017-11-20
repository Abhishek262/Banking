'''
Module to perform basic Banking operations.


CustomerData List:

    0 - Name
    1 - Password
    2 - Address
    3 - DOB
    4 - Email
    5 - Phone no.
    
method order :
    Initialize class
    obj.InputData
    obj.save


                     '''

import math, time , pickle


Customers = {}
path0 = 'Data\\'

class Bank():
    def __init__(self):
        pass

class Customer():
    no_of_customers = 0

    def __init__(self):
        self.CustomerData = None 
        Customer.no_of_customers +=1
        self.File = None
        self.Name  = None
        self.Password = None
        self.Address = None
        self.DOB = None
        self.Email = None
        self.Phno = None
        self.info = None
        self.path = None
        self.File = None
        self.amt = 0
    
    def InputData(self) :
        
        self.CustomerData = Sign_Up()
        self.Name  = self.CustomerData[0]
        self.Password = self.CustomerData[1]
        self.Address = self.CustomerData[2]
        self.DOB = self.CustomerData[3]
        self.Email = self.CustomerData[4]
        self.Phno = self.CustomerData[5]
        


    def save(self):
        self.path = 'Data\\' + self.Name
        self.file = file(self.path, 'wb')
        
        pickle.dump(self.CustomerData , self.file,2)
        self.file.close()
            

    def Withdraw(self,amount):
        if self.amt  > amount  :
            
            self.amt = self.amt - amount

    def Deposit(self,amount):
        self.amt =  self.amt + amount

                
def LoginPage():
    y =  '''Select 1 - Existing account,
Select 2 - Create new account : '''

    x = int(raw_input(y))
    if x not in range(1,3):
        print 'Invalid Option '
        LoginPage()


    if x == 1 :
        Sign_In()
    if x == 2 :
        Sign_Up()
        
def Sign_Up(): #creating new account

    print "\\ Create New Account //"
    Data = []
    Username  = raw_input("Enter your Username : ")
    Password = raw_input("Enter your Password : ")
    RePassword = raw_input("Re-Enter your Password : ")
    Address = raw_input("Enter your current address : ")
    DOB = raw_input("Enter Date of Birth (DD/MM/YYYY) : ")
    Email = raw_input("Enter a valid Email ID : ")
    Phno = raw_input("Enter your Phone number : ")

    if Password == RePassword :
        Data.append(Username)
        Data.append(Password)
        Data.append(Address)
        Data.append(DOB)
        Data.append(Email)
        Data.append(Phno)

        return Data
    else :
        print " Passwords do not match \n "
        Sign_Up()

def Sign_In():

    print "Sign in to your account "
    print ""
    Username = raw_input("Enter your username  : ")
    Password = raw_input("Enter your Password : ")
    print " Logging in .  "
    print ""
##    time.sleep(1)
##    print ".",
##    time.sleep(1)
##    print ".",


    try : 
     
        path = "Data\\" + Username
        f = open(path,'rb')
        tmpdata = pickle.load(f)

        if Username == tmpdata[0] and Password == tmpdata[1]:
            print "Logged in "
            
        else :
            print " Inavlid Username/Password " 
    
    except :
        print " Inavlid Username/Password "

    
    time.sleep(1)

    opt = raw_input("Enter 1 to enter menu or 0 to exit")
    if opt == 1 :
        Bank.menu()

    
x =  Customer()    



