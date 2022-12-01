import Create_Acc

class Main(Create_Acc.Account):
   

    def welcome(self):
        print("\t\t\t\t\tWelcome to Bank ")
  

Create_account_file = Main()
Create_account_file.intro()
Create_account_file.generating_acc()

while True:
    Create_account_file.asking_service()
    respone = int(input())
    if respone == 1:
        Create_account_file.show_account()
    elif respone == 2:
        Create_account_file.generating_acc()
    elif respone == 3:
        Create_account_file.modify_account()
    elif respone == 4:
        Create_account_file.deposite_amount()
    elif respone == 5:
        Create_account_file.withdrwal_amount()
    else:
        break

