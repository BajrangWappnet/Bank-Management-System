from abc import ABC , abstractmethod

import pickle
import sys
sys.path.append(".")
import os


class Account(ABC):
    __account_serial_no = 0  # protected 

    @abstractmethod
    def welcome(self):
        pass
    
    def generating_acc(self):

        self.acc_no = int(input("Enter the account no: ")) # account Number of user
        self.name = input("Enter Name of Account Holder: ") # account user name
        self.mobile = int(input("Enter Name of Mobile Number : ")) # Mobile no of user
        self.balance = int(input("Enter the ammount more than 5000: ")) # Amount stored as amount

        self.__account_serial_no += 1 # unique serial account numbers in system protected

        print(f"\t\t\t\t\tAccount Created!! \nHello {self.name} Welcome to Aditya Bank")

    # for displaying account details
    def show_account(self):

        print("Account Name: {}\nAccount Number: {}".format(self.name,self.acc_no)) #return account holder name
        print("Mobile Number :{}\nBalance: {}".format(self.mobile,self.balance)) #return mobile number of account holder
    
    #for modifying account 

    def modify_account(self):

        self.name = input("Modilfy Account Holder Name: ") #manual modify of account holder name
        self.mobile = int(input("Modify Mobile Number: ")) # manual modify of mobile number
        self.balance = int(input("Modify Account Balance: ")) #manual modify of account value
    
    # for deposite of ammount, argument is amount 
    def deposite_amount(self):
        amount = int(input("Enter amount you want to deposite: "))
        self.balance += amount
    
    # for withdrwal of amount, argumnet amount

    def withdrwal_amount(self):
        amount = int(input("Enter amount you want to withdrwal: "))
        self.balance -= amount

    # for report of details

    def report(self):
        print(self.acc_no,"",self.name,"",self.balance)
    
    # For getting account number
    def get_account_number(self):
        return self.acc_no

    
    # For getting mobile number
    def get_mobile_number(self):
        return self.mobile
    
    
    # For getting account Holder name
    def get_account_holder_name(self):
        return self.name
    
    
    # For getting account balance
    def get_account_balance(self):
        return self.balance

    def intro(self):
        print("\t\t\t\t***********************")
        print("\t\t\t\tState Bank Of India")
        print("\t\t\t\t***********************")
        print("\t\t\t\t Made by Bajrang")
        

    def asking_service(self):
        print("\n\n\nChoose Your Service \n"
                "1. Account Details:\n"
                "2. Generating New Account:\n"
                "3. Modify Account Details:\n"
                "4. Deposite Money:\n"
                "5. Withdrawl Money:\n"
                "6. Exit:" )

        
        



