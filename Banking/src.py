'''Module to perform basic Banking operations '''

import time,pickle

path0 = "Data\\"


class Customer :
    no_of_customers = 0

    def __init__(self):

        Customer.no_of_customers +=1

        self.CustomerData = None 
        self.Name  = None
        self.Password = None
        self.Address = None
        self.DOB = None
        self.Email = None
        self.Phno = None
        self.info = None
        self.amt = 0
    
    def InputData(self,lst) :
        
        self.Name  = lst[0]
        self.Password = lst[1]
        self.Address = lst[2]
        self.DOB = lst[3]
        self.Email = lst[4]
        self.Phno = lst[5]        

    def Withdraw(self,amount):
        if self.amt  > amount  :
            
            self.amt = self.amt - amount

            print "Capital left after Withdrawing is - " , self.amt

        else  :
            print "Sorry, your account does not have enough credit to withdraw the given amount"

    def Deposit(self,amount):
        self.amt =  self.amt + amount
        print "Updated amount - " , self.amt

    def ViewData(self):
        print "Name :  " , self.Name
        print "Address : " ,self.Address
        print "Date of Birth : " ,self.DOB
        print "Email ID  :  " , self.Email
        print "Phone number :  " , self.Phno
        
        
#contains mostly static methods        
class Bank :
    def __init__(self):
        self.txt  = "Banking Operations  \n  1.View Details \n  2.Deposit \n 3.Withdraw "
        self.prompt1 = "Enter Amount to be Withdrawn : "
        self.prompt2 = "Enter Amount to be Deposited : "

    @staticmethod
    def menu(instance) :
        print self.txt
        prompt = int(raw_input("Enter Option : "))
        if prompt ==1 :
            instance.ViewDetails()
        elif prompt == 2 :
            amt = float(raw_input(self.prompt1))
            instance.Withdraw(amt)
        elif prompt == 3 :
            amt1 = float(raw_input(self.prompt2))
            instance.Depsoit(amt1)
    
                
def LoginPage():

    print ' Welcome to our Bank - We care '
    print '' 
    txt =  '''Select 1 - Existing account,
Select 2 - Create new account : '''

    x = int(raw_input(txt))
    if x not in range(1,3):
        print 'Invalid Option '
        LoginPage()

    if x == 1 :
        SignIn()
    if x == 2 :
        SignUp()

def transferData(obj):
    path = 'Data\\' + obj.Name
    f = file(path, 'wb')
    
    pickle.dump(obj,f)
    f.close()
    
def SignUp() :
    
    print "\\ Create New Account //"
    Data = []
    obj = Customer()
    
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

        obj.InputData(Data)
        transferData(obj)
        print ""

        print " SignUp complete " 
        
    
    else :
        print " Passwords do not match \n "
        Sign_Up()


def SignIn():

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
        custObj = pickle.load(f)

        if Username == custObj.Name and Password == custObj.Password:
            print "Logged in "
            
        else :
            print " Inavlid Username/Password "
            SignIn()
    
    except :
        print " Inavlid Username/Password "
        SignIn()

    
    time.sleep(1)

    opt = raw_input("Enter 1 to enter menu or 0 to exit")
    if opt == 1 :
        Bank.menu(custObj)
    elif opt == 2 :
        exit
    

        
