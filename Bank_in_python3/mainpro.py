# -*- coding: utf-8 -*-


class Accout():
    ac_n=0;
    name='';
    deposit=0
    type="";
    
    def CreateAccount(self):
        self.ac_no=int(input("Enter the account number:"))
        self.name=input("Enter your name:")
        self.type=input("enter the type of account you are making(C/S):")
       
        
        if(self.type=='C'):
            while(self.deposit<10000):
                 self.deposit=int(input("Enter the amount you want to deposit(min 5000 for savings and 10000 for current):"))
        if(self.type=='S'):
            while(self.deposit<5000):
                self.deposit=int(input("Enter the amount you want to deposit(min 5000 for savings and 10000 for current):"))
        print("\n\n\nNew account created")
    
    def showaccount(self):
        print("Account number:",self.ac_no)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)
    
    def modifyaccount(self):
        print("Account number:",self.ac_no)
        self.name=input("Modify Account holder's name:")
        self.type=input("Modify account type:")
        
    def depositAmount(self,amount):
        self.deposit += amount
        
    def withdrawAmount(self,amount):
        self.deposit -= amount
        
    def report(self):
        print(self.ac_no, " ",self.name ," ",self.type," ", self.deposit)
        
        
    def getAccountNo(self):
        return self.ac_no
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    
        
        
            
        
        
def intro():
    print("\t\t\t\t***************************")
    print("\t\t\t\t Your favourite Goda bank")
    print("\t\t\t\t brought to you by Nabajyoti")
    print("\t\t\t\t***************************")
    print ("Press enter")
    input()
  
    
    
def writeAccount():
    account=Account()
    account.CreateAccount()
    writeAccountsFile(account)
    
    
def displayAll():
    with open("Accounts.txt","r") as file:
        lines=file.readlines()
        header=lines[0]
        field_names=header.strip().split(",")
        print(field_names)
        for row in lines[1:]:
            vals=row.strip().split(',')
            print("{};{};{};{}".format(vals[0],vals[1],vals[2],vals[3]))
            
            
        
      
            
            
def displaySp(num):
    file=open("Accounts.txt","r")
    lines=file.readlines()
    found=0
    for row in lines[1:]:
        
        vals=row.strip().split(',')
        if (vals[0]==num):
            found=1
            print ("your bank deposit is :",vals[2])
            
            
    file.close()

        
    if (found==0):
        print("No account exists with this number")
        
##hashu hashu


        
def depositAndWithdraw(num1,num2):
    filename='Accounts.txt'
    tempfile=NamedTemporaryFile(mode='w',delete=False)
    fields=['Account_number','Name','Deposit','Type']
    with open(filename,'r') as csvfile,tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if(row['Account_number']==num1):
                if(num2==1):
                    amount = int(input("Enter the amount to deposit : "))
                    row['Deposit']+=amount
                    print("your account has been UPDATED")
                elif num2==2:
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= row['Deposit'] :
                        row['Deposit']-=amount
                    else:
                        print("ITNA PAISA NHI HAI!")
            row = {'Account_number': row['Account_number'], 'Name': row['Name'], 'Deposit': row['Deposit'], 'Type': row['Type']}
            writer.writerow(row)
    shutil.move(tempfile.name, filename)
    
    
    
    


                
    
    
           
                    
            
        
        
        
    


#start of the program
ch=''
num=0
intro()

while ch!=8:
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    ch = input()
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num =int(input("\tEnter The account No. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tThanks for using GODA bank")
        break
    else :
        print("Invalid choice")
    
    ch = input("Enter your choice : ")
    
    
        
       


