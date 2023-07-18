import time
import random
import sys
import mysql.connector as connection
myconn = connection.connect(host="127.0.0.1", user="root", passwd="", database="Coop_society")
cursor = myconn.cursor()
def welcome():
    time.sleep(1)

    print("Redirecting to POPSON Coop_society User page... ")
    time.sleep(2)
    print("""You are welcome to POPSON Coop_society User page
      Enter 1 to login 
      Enter 2 to create new account
      """)
    choice = input(">>> ")
    if choice =="1":
        login()
    elif choice == "2":
         registration()
    else:
        print("You have made a wrong choice")
        welcome()
def registration():
        print("Kindly proceed with your registration by providing your details below ")
        val= []
        User_info= ("First_name", "Middle_name", "Last_name", "Gender", "Age","Email_address","Interest", "Pass_word", "User_ID","Loan_Amount","Refund", "Pin")
        querry= "INSERT INTO User(First_name, Middle_name, Last_name, Gender, Age, Email_address,Interest, Pass_word, User_ID, Loan_Amount,Refund, Pin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s,%s, %s)"
        for holder in range(12):
            if User_info[holder] == "User_ID":
                user= "COOP/USER/"+ str(random.randint (37054,39999)) 
            elif User_info[holder]=="Interest":
                user= 0
            elif User_info[holder]== "Loan_Amount":
                user=0
            elif User_info[holder]=="Refund":
                user=0               
            else:    
                user= input(f"Enter your {User_info[holder]}: ")
            val.append(user)
            time.sleep(2)
        print("Thank you for registering with us ")
        cursor.execute(querry, val)
        myconn.commit()
        time.sleep(2)
        print(f"Dear {val[0]} {val[1]} {val[2]} your User_ID is {val[8]} \n Your username is {val[5]}, password is {val[7]} and your transaction pin is {val[11]}")
        time.sleep(2)
        print("""
        Enter 1 to login
        Enter 2 logout
        """)
        step= input(">>> ")
        if step == "1":      
           login()
        else:
            sys.exit()
def login():
    username = input("Enter your Email address: ")
    Pass_word = input("Enter your password: ")
    val = (username, Pass_word)
    querry = "select * from User where Email_address=%s and Pass_word=%s "
    cursor.execute(querry, val)
    global result
    result = cursor.fetchone()
    if result:
        print("You have successfully login \n Kindly proceed by selecting the operation you will like to perform")
        time.sleep(2)
        operation()
    else:
        print("Invalid username or password")
        time.sleep(1)
        login() 

def operation():
    print("""
    These are the operations you can perform:
    1. Check Eligibility for Loan     
    2. Request for Loan    
    3. Repay-Loan
    4. check interest on loan charged
    5. Status
    6. Logout
    """)
    task = input("What transaction will you like to perform: ")
    if task == "1":
        time.sleep(2)
        Eligibility()
    elif task == "2":
        time.sleep(2)
        loan()  
    elif task == "3":
        Repay_Loan() 
    elif task== "4":
        loan_interest()  
    elif task=="5":
        status()
    elif task == "6":
        sys.exit()    
    else:
        print("Invalid input")
        time.sleep(2)
        operation() 
      

def loan():     
    print("Redirecting to the Loan page ...")
    time.sleep(3)
    print("Accessing Loan page....")
    time.sleep(2)
    loan_user()
    
    
def loan_user():
    global loan_am
    global Amount_payable
    print("Dear User you are about to request for a loan from POPSON Coop_society, Kindly Enter your User_ID to continue")
    time.sleep(2)
    wait= input("Kindly enter your User_ID: ")
    val_= (wait,)
    query = "select * from User where User_ID = %s"
    cursor.execute(query, val_)
    waitr= cursor.fetchone()
    if waitr:
        print(f"Dear {waitr[1]} {waitr[3]} you are about to request for a loan with Coop_society")
        time.sleep(2)
        loan_am=int(input("Enter loan amount: "))
        val=(1, )
        querry= "select * from coop_society.coop_account where ID=%s" 
        cursor.execute(querry, val)
        global upload
        upload = cursor.fetchone()
        if upload:
                if upload[3] > loan_am or upload[3]== loan_am:
                    print("Verifying ....")
                    time.sleep(2)
                    print("Accessing Data Page...")
                    time.sleep(2)
                    if waitr[10] == 0:
                        #This line of code checkes the database to confirm if the user has made any contribution 
                        print(f"Dear {waitr[1]} {waitr[3]} you are about to be loaned out the sum of #{loan_am} with an interest rate of 10%") 
                        time.sleep(2)
                        print(f"Amount_payable=(110% of {loan_am}")  
                        time.sleep(2) 
                        Amount_payable = int((loan_am*0.1)+(loan_am)) 
                        time.sleep(2)
                        trea= upload[1] - upload[2]
                        val_k_ = (trea, 1)
                        querry_= "UPDATE coop_society.coop_account SET Treasure_Balance = %s where ID = %s"
                        cursor.execute( querry_, val_k_)
                        myconn.commit()
                        #You are expected to update it to thr treasure account 
                        # print(Amount_payable)
                        time.sleep(2)
                        print(f"Dear {waitr[1]} {waitr[3]} you have requested for a laon of {loan_am} at an interest rate of 10% \n Amount payable is {Amount_payable} after a period of 24 working days")
                        time.sleep(2)
                        print("Proceed by entering your 4 digit passcode")
                        time.sleep(1)
                        request0=int(input("Enter your four digit pin: "))
                        pin = waitr[12]
                        if request0 == pin:
                            Loan_Amount = int(waitr[10] + loan_am)
                            val3 = (Loan_Amount, pin)
                            querry= "UPDATE User SET Loan_Amount = %s where pin = %s"
                            cursor.execute( querry, val3)
                            myconn.commit()
                            # query = "SELECT SUM(Loan_Amount) from User"
                            # val = (4,)
                            # cursor.execute(query)
                            # result_p = cursor.fetchone()
                            # val_k = (result_p[0], 1)
                            acnt= upload[2]+ loan_am
                            val_c= (acnt, 1)
                            querry_= "UPDATE coop_society.coop_account SET Disbursement= %s where ID = %s"
                            cursor.execute( querry_, val_c)
                            myconn.commit()
                            val=(1, )
                            querry= "select * from coop_society.coop_account where ID=%s" 
                            cursor.execute(querry, val)
                            upload = cursor.fetchone()
                            treasure= upload[1] - upload[2]
                            val_k_ = (treasure, 1)
                            querry_= "UPDATE coop_society.coop_account SET Treasure_Balance = %s where ID = %s"
                            cursor.execute( querry_, val_k_)
                            myconn.commit()
                            time.sleep(2)
                            print("Your loan request has been granted ")
                            ask= input("would you like to perform another operation: ")
                            if ask== "yes":
                                operation()
                            elif ask=="no":
                                sys.exit()

                        else:
                            print("You have entered a wrong pin")
                            loan()
                    elif waitr[10] != 0:
                        print(f"Dear {waitr[1]} {waitr[3]} you have an existing loan with Coop_society, You can't be granted a new loan \n Until the exixting loan has been paid back to the Coop Society")
                        time.sleep(2)
                        print("""
                            Enter 1 to Repay your existing loan
                            Enter 2 to perform another Operation
                        """)
                        qwer=input(">>>  ")
                        if qwer=="1":
                            Repay_Loan()
                        elif qwer=="2":
                            operation()  
                elif (loan_am > upload[3] ) :
                    print("You cannot be granted the requested Amount, Kindly request for a lower Amount, Try Again !!!")
                    loan_user() 
        else:
            print("Your Datails cannot be found, kindly Try again !!!")
            loan_user()                       
    else:
        print("You are not a User of the society")
        loan_user()
        # query = "SELECT SUM (Loan_Amount) from User"
        # val = (4,)
        # cursor.execute(query)
        # result = cursor.fetchone()
        # val_k = (result[0], 1)
        # querry_= "UPDATE Coop_Account SET Disbursement= %s where ID = %s"
        # cursor.execute( querry_, val_k)
        # myconn.commit()             

def Eligibility():
    print("Accessing Data page....")
    time.sleep(2)
    print("Fetching your information") 
    time.sleep(2)
    data= input("Enter your User_ID: ")
    time.sleep(1)
    data1=input("Enter your Email_Address: ")      
    val=(data1, data)
    querry= "select * from User where Email_address=%s and User_ID=%s" 
    cursor.execute(querry, val)
    resu = cursor.fetchone()
    if resu[10]== 0:
        time.sleep(2)
        print(f"Dear {resu[1]} {resu[3]} you are Eligible for a loan")
        time.sleep(3)
        seek=input("Would you like to Request for a loan? ").lower().strip()
        time.sleep(2)
        if seek=="yes":
            time.sleep(2)
            loan()
        elif seek == "no":
            time.sleep(2)
            operation()
    else:
        print(f" Dear {resu[1]} {resu[3]} you have an outstanding loan of {resu[10]} \n Kindly pay up !!!")
        time.sleep(2)
        print("""
            Enter 1 to pay Existing Loan
            Enter 2 to perform Another Operation 
        """)
        time.sleep(1)
        use=input(">>> ")
        time.sleep(2)
        if use== "1":
            time.sleep(2)
            Repay_Loan()
        elif use =="2":
            time.sleep(2)
            operation()  
        else:
            print("You have entered a wrong input, Kindly Try Again !!! ")
            time.sleep(2)
            Eligibility()   


def Repay_Loan():
    print("Dear User kindly proceed with the repayment process")
    time.sleep(2)
    req= input("Kindly provide your User_ID: ")
    time.sleep(1)
    val_r=(req, )
    querry= "select * from User where User_ID=%s "
    cursor.execute(querry, val_r)
    global resut
    resut = cursor.fetchone()
    if resut:
        Amount_payable = int((resut[10]*0.1)+(resut[10]))
        requ=input("Kindly enter your Email_Address: ")
        val=(requ, req)
        querry= "select * from User where Email_address=%s and User_ID=%s"
        cursor.execute(querry,val)
        grade=cursor.fetchone()
        if grade:
            print("Confirming Details provided...")
            time.sleep(2)
            print("Details confirmed")
            while grade[10] != grade[11]:
                time.sleep(2) 
                print(f"Dear {grade[1]} {grade[3]} you are Entitled to repay { Amount_payable } for a loan of {resut[10]} at an interest rate of 10%")
                time.sleep(2)
                pay= int(input("Enter Repayment Amount: "))
                if pay == Amount_payable:
                    print(f"Dear{grade[1]} {grade[3]} kindly confirm the Refund transaction, ")
                    time.sleep(1)
                    print("Kindly provide your Transaction pin ")
                    quest= int(input("Enter your transaction pin: "))
                    time.sleep(2)
                    if grade[12]==quest:
                        print("Wait, While the transaction is been confirmed.... ")
                        time.sleep(2)
                        val_id=(resut[10], req)
                        querry= "UPDATE User SET Refund= %s where User_ID = %s"
                        cursor.execute( querry, val_id)
                        myconn.commit()
                        print("Transaction comfirmed.....")
                        time.sleep(2)
                        print("Thank you")
                        # lkay=int(loan_am - resut[10])
                        # val_is=(lkay, req)
                        # querry= "UPDATE User SET Loan_Amount= %s where User_ID = %s"
                        # cursor.execute( querry, val_is)
                        # myconn.commit()
                        Interest= Amount_payable - result[10]
                        val_c=(Interest, req)
                        querry="UPDATE User SET Interest=%s where User_ID=%s "
                        cursor.execute(querry, val_c)
                        myconn.commit()
                        time.sleep(3)
                        ask= input("will you like to perform another transaction?: ")
                        if ask== "yes":
                            operation()
                        elif ask== "no":
                            sys.exit()   
                else:
                    print(f"Dear {grade[1]} {grade[3]} you have entered a contradictory amount that varies from the expected amount")  
                    time.sleep(2)
                    Repay_Loan()
            else:        
                    time.sleep(2)
                    print("Acessing Data ... !!!")
                    time.sleep(2)
                    print("You do not have any existing loan !!!")
                    time.sleep(2)
                    ask= input("will you like to perform another transaction? ")
                    if ask== "yes":
                        operation()
                    elif ask== "no":
                        sys.exit()        
        else:
            print("You have entered a wrong input")   
            Repay_Loan()
def status():
    print("Dear User you are about to verify your payment status") 
    time.sleep(1) 
    emaii=input("Dear User kindly Enter your Email_Address: ")
    time.sleep(1)    
    user= input("Dear User Kindly Enter your User_ID: ")   
    val_P=(emaii, user)   
    querry="select * from User where Email_address=%s and User_ID=%s"  
    cursor.execute( querry, val_P)  
    date= cursor.fetchone()   
    if date:
        print("Accessing User data page.... ")
        time.sleep(2)
        if date[10]== date[11]:
            time.sleep(3)
            print("Paid")
            hull= input("Will you like to perform another operation?: ")
            if hull =="yes":
                operation()
            elif hull =="no":
                sys.exit()      
        elif date[10] != date[11]:   
            time.sleep(2)
            print("Not Paid") 
            time.sleep(2)
            hot=input("Will you like to pay now?: ").lower().strip()
            if hot=="yes":
                Repay_Loan() 
            elif hot=="no":
                operation()  
            else:
                print("You have entered a wrong input")
                status()      
    else:
        print("You have entered a wrong input ")
        status()

def loan_interest():
    time.sleep(2)
    print('Accessing data page... ')
    time.sleep(2)
    print("Dear User you are about to verify the interest amount on the loan incured ")
    time.sleep(2)
    print("Dear User do kindly note that you are charged 10% of your Loan amount as Interest")
    time.sleep(2)
    client= input("Kindly input your User_ID: ")
    val_p= (client, )
    querry=" select * from User where User_ID = %s "
    cursor.execute(querry,val_p )
    d_client=cursor.fetchone()
    if d_client:
        ques= input("Have you paid your loan?: ")
        if ques=="yes":
            if d_client[11] == d_client[10]:
                print("Fetching Data ...")
                time.sleep(2)
                print("Acessing Data page")
                time.sleep(3)
                print(f" Dear {d_client[1]} {d_client[2]} the interest charged on your loan insured is {d_client[7]}")
            elif d_client[11] != d_client[10]:
                print("That's a wrong claim !!, you haven't paid your loan yet,") 
                time.sleep(2) 
                quest=input("Will you like to pay now?: ")  
                time.sleep(2)
                if quest== "yes":
                    time.sleep(3)
                    Repay_Loan()  
                elif quest== "no":
                    time.sleep(3)
                    operation()  
        elif ques=="no":
            time.sleep(2)
            quest=input("Will you like to pay now?: ")  
            time.sleep(2)
            if quest== "yes":
                time.sleep(2)
                Repay_Loan()  
            elif quest== "no":
                time.sleep(2)
                operation()    
    else:
        print("Dear User kindly check as you have entered a wrong input ")
        time.sleep(2)
        loan_interest()
welcome()