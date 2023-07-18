import time
import random
import sys
import mysql.connector as connection
myconn = connection.connect(host="127.0.0.1", user="root", passwd="", database="Coop_society")
cursor = myconn.cursor()
def welcome():
    time.sleep(1)
    print("Redirecting to POPSON Coop_society Membership page... ")
    time.sleep(2)
    print("""You are welcome to POPSON Coop_society Membership page
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
        members_info= ("First_name", "Middle_name", "Last_name", "Gender", "Age","Email_address","Refund", "Pass_word","Membership_ID","Loan_Amount","Loan_Interest","Contribution","Profit", "Pin")
        querry= "INSERT INTO members (First_name, Middle_name, Last_name, Gender, Age, Email_address,Refund, Pass_word, Membership_ID, Loan_Amount, Loan_Interest, Contribution, Profit, Pin) VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s,%s, %s)"
        for holder in range(14):
            if members_info[holder] == "Membership_ID":
               user= "COOP/MEM/"+ str(random.randint (57054,59999))  
            elif members_info[holder]=="Refund":
                user= 0
            elif members_info[holder]=="Loan_Interest":
                user= 0
            elif members_info[holder]== "Loan_Amount":
                user=0
            elif members_info[holder]=="Contribution":
                user=0 
            elif members_info[holder]=="Profit":
                user=0                   
            else:    
                user= input(f"Enter your {members_info[holder]}: ").capitalize()
            val.append(user)
            time.sleep(2)
        print("Thank you for registering with us ")
        cursor.execute(querry, val)
        myconn.commit()
        time.sleep(2)
        print(f"Dear {val[0]} {val[1]} {val[2]} your Membership_ID is {val[8]} \n Your username is {val[5]}, password is {val[7]} pin is {val[13]}")
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
        # val_a=(1,0, 0, 0)
        # treasure=("Revenue_Generated, Disbursement, Treasure_Balance") 
        # querry_e = "INSERT into Coop_Account (Revenue_Generated, Disbursement, Treasure_Balance ) VALUES(%s, %s, %s) " 
        # cursor.execute(querry_e, val_a)
        # myconn.commit()    


def login():
    username = input("Enter your Email address: ")
    Pass_word = input("Enter your password ")
    val = (username, Pass_word)
    querry = "select * from members where Email_address=%s and Pass_word=%s "
    cursor.execute(querry, val)
    global result
    result = cursor.fetchone()
    if result:
        print("You have successfully login \n Kindly proceed by selecting the operation you will like to perform ")
        time.sleep(2)
        operation()
    else:
        print("Invalid username or password")
        time.sleep(1)
        login() 
def operation():
    print("""
    These are the operations you can perform:
    1. Make Contribution
    2. Check Eligibility for Loan
    3. Request for Loan    
    4.Repay-Loan
    5. Status
    6. check loan Interest charged
    7.Logout
    """)
    task = input("What transaction will you like to perform: ")
    if task == "1":
        time.sleep(2)
        Contribution()
    elif task == "3":
        time.sleep(2)
        loan()  
    elif task == "6":
        loan_interest()
    elif task=="7":
        sys.exit()
    elif task=="4":
        Repay_Loan()  
    elif task=="2":
        Eligibility()
    elif task=="5":
        status()
    else:
        print("Invalid input")
        time.sleep(2)
        operation() 
def loan():
    print("Will you like to take a loan now? ")
    pop= input(">>> ").lower().strip()
    if pop=="yes":
        loan_member()
    elif pop=="no":
        operation()  
    else:
        print("You have entered a wrong input")
        loan()   
def Contribution():
    print("Will you like to make a contribution? ") 
    time.sleep(2) 
    ans=input(">>> ").strip().lower()
    if ans=="yes":
        print("Redirecting to POPSON Coop_society Contribution page....")
        time.sleep(2)
        Contribution_member()
    elif ans== "no":
        operation()
    else:
        print("You have Entered a wrong input")
        Contribution()            
def Contribution_member():
    print("Dear Member you are about to make contribution to POPSON Coop Society, Kindly Enter your Membership ID to continue ")
    time.sleep(2)
    cont= input("Kindly enter your Membership ID: ")
    val1=(cont, )
    querry= "select * from members where Membership_ID = %s "
    cursor.execute(querry, val1)
    contd=cursor.fetchone()
    if contd:
        print(f"Dear {contd[1]} {contd[3]} kindly proceed with your contribution into Coop Society")
        time.sleep(2)
        top=int(input("Enter the Contribution Amount: "))
        time.sleep(2)
        print(f"Dear {contd[1]} {contd[3]} kindly confirm the transaction into POPSON Coop Society the sum of #{top} ")
        time.sleep(2)
        access=int(input("Kindly Enter your Four Digit Pin: "))
        Pin = contd[14]
        if access == Pin:
            top_up = top + contd[12]
            val4 = (top_up,cont)
            querry= "UPDATE members SET Contribution= %s where Membership_ID = %s"
            cursor.execute( querry, val4)
            myconn.commit()
            print(f"{contd[1]} {contd[3]} you have succesfully made a contribution the sum of #{top}")
            contr_interest=int(0.15 * top)
            val_p=(contr_interest, cont)
            querry="UPDATE members SET Profit=%s where Membership_ID =%s"
            cursor.execute(querry, val_p)
            myconn.commit()
            val = (4, )
            query = "SELECT SUM(Contribution) from members"
            cursor.execute(query)
            result = cursor.fetchone()
            val = (result[0], 1)
            querry_= "UPDATE coop_society.coop_account SET Revenue_Generated= %s where ID = %s"
            cursor.execute( querry_, val)
            myconn.commit()
            #This command sums up profit coloumn then updates it to the revenue generated of the association
            # val_q = (4, )
            # query_q = "SELECT SUM(Profit) from members"
            # cursor.execute(query_q, )
            # result = cursor.fetchone()
            # val = (result[0], 1)
            # querry_w= "UPDATE coop_society.coop_account SET Revenue_Generated= %s where ID = %s"
            # cursor.execute( querry_w, val)
            # myconn.commit()
            val=(1, )
            querry= "select * from coop_society.coop_account where ID=%s" 
            cursor.execute(querry, val)
            upload = cursor.fetchone()
            wale= upload[1]- upload[2]
            val_k = (wale, 1)
            querry_= "UPDATE coop_society.coop_account SET Treasure_Balance = %s where ID = %s"
            cursor.execute( querry_, val_k)
            myconn.commit()
            # treasure= int(upload[3]- contd[13])
            # val_X=(treasure, 1)
            # querry_x="UPDATE coop_society.coop_account SET Treasure_Balance = %s where ID = %s"
            # cursor.execute(querry_x, val_X)
            # myconn.commit()

            ask= input("would you like to perform another operation: ")
            if ask== "yes":
                    operation()
            elif ask=="no":
                    sys.exit()
        else:
            print("You have entered a wrong pin,Kindly try again") 
            time.sleep(2)
            Contribution_member()
    else:
        print("Wrong input") 
        time.sleep(2)  
        Contribution_member()   
# print(result[0])

def loan_member():
    global loan_am
    print("Dear Member you are about to request for a loan from POPSON Coop_society, Kindly Enter your membership ID to continue")
    time.sleep(2)
    wait= input("Kindly enter your Membership_ID: ")
    val= (wait, )
    query = "select * from members where Membership_ID = %s"
    cursor.execute(query, val)
    global waitr
    waitr= cursor.fetchone()
    if waitr:
        print(f"Dear {waitr[1]} {waitr[3]} you are about to request for a loan with POPSON Coop_society")
        time.sleep(2)
        if waitr[10]== 0:
            #This line of code will verify if the user has an outstanding loan from the membership table
            loan_am=int(input("Enter loan amount: "))
            val=(1, )
            querry= "select * from coop_society.coop_account where ID=%s" 
            cursor.execute(querry, val)
            global upload
            upload = cursor.fetchone()
            if upload:
                if upload[3] > loan_am or upload[3]== loan_am :
                    """This line of code automatically checks if the association has money left in their treasure and also
                    the line of code checks if the amount requested is equal to or less than the treasure balance"""
                    print("Verifying ....")
                    time.sleep(2)
                    print("Accessing Data Page...")
                    time.sleep(2)
                    if waitr[12] != 0:
                        #This line of code verifies if the member has made a contribution, hence dictatates the interest rate of the loan to be granted
                        print(f"Dear {waitr[1]} {waitr[3]} you are about to be loaned #{loan_am} with an interest rate of 2%")
                        time.sleep(2)
                        print(f" Amount_payable= (102% of {loan_am}")
                        time.sleep(2)
                        global Amount_payable
                        Amount_payable=int((loan_am*0.02)+(loan_am))
                        time.sleep(2)
                        print(f"Dear {waitr[1]} {waitr[3]} you have requested for a laon of #{loan_am} at an interest rate of 2% Amount payable is #{Amount_payable} after a period of 24 working days")
                        time.sleep(2)
                        treasure_p= upload[1] - upload[2]
                        val_k = (treasure_p, 1)
                        querry_= "UPDATE coop_society.coop_account SET Treasure_Balance = %s where ID = %s"
                        cursor.execute( querry_, val_k)
                        myconn.commit()
                        time.sleep(2)
                        print("Proceed by entering your 4 digit passcode")
                        time.sleep(1)
                        request0= int(input("Enter your four digit pin: "))
                        pin = waitr[14]
                        if request0 == pin:
                        #This line of code compare the pin entered to the pin entered in the database
                            Loan_Amount = (waitr[10] + loan_am)
                            val2 = (Loan_Amount, pin)
                            querry= "UPDATE members SET Loan_Amount = %s where pin = %s"
                            cursor.execute( querry, val2)
                            myconn.commit()
                            time.sleep(2)
                            print("Your loan request has been granted ")
                            query = "SELECT SUM(Loan_Amount) from members"
                            val = (4,)
                            cursor.execute(query)
                            result_p = cursor.fetchone()
                            lok = upload[2]+loan_am
                            val_k = (lok, 1)
                            querry_= "UPDATE coop_society.coop_account SET Disbursement= %s where ID = %s"
                            cursor.execute( querry_, val_k)
                            myconn.commit()
                            treasu= upload[1] - upload[2]
                            val_a = (treasu, 1)
                            querry_a= "UPDATE coop_society.coop_account SET Treasure_Balance = %s where ID = %s"
                            cursor.execute( querry_a, val_a)
                            myconn.commit()
                            ask= input("would you like to perform another operation ")
                            if ask== "yes":
                                operation()
                            elif ask=="no":
                                    sys.exit()
                        else:
                            print("You have entered a wrong pin")
                            loan_member()
                    elif waitr[12] == 0:
                        #This line of code checks the member datatbase to confirm that the member has not contributed a kobo to the Coop Account
                        print("You have made 0 contribution so far, you will be charged 5% as interest rate on the requested loan amount")
                        time.sleep(2)
                        print(f"Dear {waitr[1]} {waitr[3]} you are about to be loaned the sum of #{loan_am} with an interest rate of 5%") 
                        time.sleep(2)
                        print(f"Amount_payable=(105% of {loan_am}")  
                        time.sleep(2)
                        Amount_payable=int((loan_am*0.05)+(loan_am)) 
                        time.sleep(2)
                        treasure= upload[1] - upload[2]
                        val_k = (treasure, 1)
                        querry_= "UPDATE coop_society.coop_account SET Treasure_Balance = %s where ID = %s"
                        cursor.execute( querry_, val_k)
                        myconn.commit()
                        time.sleep(2)
                        print(f"Dear {waitr[1]} {waitr[3]} you have requested for a laon of {loan_am} at an interest rate of 5% Amount payable is {Amount_payable} after a period of 24 working days")
                        time.sleep(2)
                        print("Proceed by entering your 4 digit passcode")
                        time.sleep(1)
                        request0=int(input("Enter your four digit pin: "))
                        pin = waitr[14]
                        if request0 == pin:
                            #This line of code compare the pin entered to the pin entered in the database
                            Loan_Amount = (waitr[10] + loan_am)
                            val2 = (Loan_Amount, pin)
                            querry= "UPDATE members SET Loan_Amount = %s where pin = %s"
                            cursor.execute( querry, val2)
                            myconn.commit()
                            time.sleep(2)
                            print("Your loan request has been granted ")
                            query = "SELECT SUM(Loan_Amount) from members"
                            val = (4,)
                            cursor.execute(query)
                            result_p = cursor.fetchone()
                            val_k = (result_p[0], 1)
                            querry_= "UPDATE coop_society.coop_account SET Disbursement= %s where ID = %s"
                            cursor.execute( querry_, val_k)
                            myconn.commit()
                            treasure= upload[1] - upload[2]
                            val_k = (treasure, 1)
                            querry_= "UPDATE coop_society.coop_account SET Treasure_Balance = %s where ID = %s"
                            cursor.execute( querry_, val_k)
                            myconn.commit()
                            ask= input("would you like to perform another operation ")
                            if ask== "yes":
                                operation()
                            elif ask=="no":
                                sys.exit()
                        else:
                            print("You have entered a wrong pin")
                            loan()
                    else:
                        print("Wrong Data !!!")
                        loan_member()        
                elif (loan_am == upload[3]) and (loan_am > upload[3] ) :
                        print("You cannot be granted the requested Amount, Kindly request for a lower Amount, Try Again !!!")
                        loan_member()          
                else:
                    print("You cannot be granted the requested Amount, Kindly request for a lower Amount, Try Again !!!")
                    loan_member()
            else:
                print("You have entered a wrong info, kindly check, confirm and Enter again !! ")
                loan_member()        

        elif waitr[10] !=0:
                #This line of code checks the coloumn of the loan for the member to authenticate if the user has an outstanding loan
                print(f"Dear {waitr[1]} {waitr[3]} you have an existing loan with Coop_society, You can't be granted a new loan \n Until the exixting loan has been paid back to the Coop Society ") 
                time.sleep(2)
                print("""
                Enter 1 to Repay your exixting loan
                Enter 2 to perform another Operation
                """)
                qwer=input(">>>  ")
                if qwer=="1":
                    Repay_Loan()
                elif qwer=="2":
                    operation()
        else:
            print("Your Datails cannot be found kindly Try again !!!")                       
    else:
        print("You are not a member of the society")  
        operation()


def Eligibility():
    print("Accessing Data page....")
    time.sleep(2)
    print("Fetching your information") 
    time.sleep(2)
    data= input("Enter your Membership_ID: ")
    time.sleep(1)
    data1=input("Enter your Email_Address: ")      
    val=(data1, data)
    querry= "select * from members where Email_address=%s and Membership_ID=%s" 
    cursor.execute(querry, val)
    resu = cursor.fetchone()
    if resu[10]== 0:
        time.sleep(2)
        print(f"Dear {resu[1]} {resu[3]} you are Eligible for a loan")
        time.sleep(3)
        seek=input("Would you like to Request for a loan?: ").lower().strip()
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

    global Amount_payable   
def Repay_Loan():
    print("Dear User kindly proceed with the repayment process")
    time.sleep(2)
    req= input("Kindly provide your Membership_ID: ")
    time.sleep(1)
    requ=input("Kindly enter your Email_Address: ")
    val=(requ, req)
    querry= "select * from members where Email_address=%s and Membership_ID=%s"
    cursor.execute(querry,val)
    grade=cursor.fetchone()
    if grade:
        print("Confirming Details provided...")
        time.sleep(2)
        print("Details confirmed")
        if grade[12] !=0:
            #This line of code verifies if the member has made a contribution
            Amount_payable_=int((grade[10]*0.02)+(grade[10]))
            time.sleep(2)
            while grade[7] != grade[10]:
                print(f"Dear {grade[1]} {grade[3]} you are Entitled to repay {Amount_payable_} for a loan of {grade[10]} at an interest rate of 2%")
                time.sleep(2)
                pay= int(input("Enter Repayment Amount: "))
                if pay == Amount_payable_:
                    #This line of code compares the amount entered and the expected repayment amount
                    print(f"Dear {grade[1]} {grade[3]} kindly confirm the Refund transaction, ")
                    time.sleep(1)
                    print("Kindly provide your Transaction pin ")
                    quest= int(input("Enter your transaction pin: "))
                    time.sleep(2)
                    if grade[14]==quest:
                        #This line of code compares the pin in the database and the pin entered 
                        print("Wait, While the transaction is been confirmed.... ")
                        time.sleep(2)
                        val_id=(grade[10], req)
                        querry= "UPDATE members SET Refund= %s where Membership_ID = %s"
                        cursor.execute(querry, val_id)
                        myconn.commit()
                        print("Transaction comfirmed.....")
                        time.sleep(2)
                        print("Thank you")
                        interest= int(Amount_payable_ - grade[10])
                        val_r= (interest, quest)
                        querry="UPDATE members SET Loan_Interest=%s where pin =%s"
                        cursor.execute(querry, val_r)
                        myconn.commit()
                        time.sleep(3)
                        ask= input("will you like to perform another transaction?: ").lower().strip()
                        if ask== "yes":
                            operation()
                        elif ask== "no":
                            sys.exit()
                    else:
                        print("You have entered a wrong pin, Kindly check, verify and Try again !!")
                        Repay_Loan()        
                elif pay !=Amount_payable_:
                    print("You have entered a wrong amount as to the expected amount, Kindly check, verify and Try again !!!")  
                    Repay_Loan()  
            else:
                time.sleep(2)
                print("Acessing Data ... !!!")
                time.sleep(2)
                print("You do not have any existing loan !!!")
                time.sleep(2)
                ask= input("will you like to perform another transaction?: ").lower().strip()
                if ask== "yes":
                    operation()
                elif ask== "no":
                    sys.exit()
        elif grade[12] == 0:
                #This line of code verifies 
                Amount_payable_0=int((grade[10]*0.05)+(grade[10]))
                time.sleep(2)
                while grade[7] != grade[10]:
                    print(f"Dear {grade[1]} {grade[3]} you are Entitled to repay {Amount_payable_0} for a loan of {grade[10]} at an interest rate of 5%")
                    time.sleep(2)
                    pay= int(input("Enter Repayment Amount: "))
                    if pay == Amount_payable_0:
                        print(f"Dear {grade[1]} {grade[3]} kindly confirm the Refund transaction, ")
                        time.sleep(1)
                        print("Kindly provide your Transaction pin ")
                        quest= int(input("Enter your transaction pin: "))
                        time.sleep(2)
                        if grade[13]==quest:
                            print("Wait, While the transaction is been confirmed.... ")
                            time.sleep(2)
                            val_id=(grade[10], req)
                            querry= "UPDATE members SET Refund= %s where Membership_ID = %s"
                            cursor.execute(querry, val_id)
                            myconn.commit()
                            print("Transaction comfirmed.....")
                            time.sleep(2)
                            print("Thank you")
                            interest= Amount_payable_0 - grade[10]
                            val_r= (interest, quest)
                            querry="UPDATE members SET Loan_Interest=%s where pin =%s"
                            cursor.execute(querry, val_r)
                            myconn.commit()
                            time.sleep(3)
                            ask= input("will you like to perform another transaction?: ").lower().strip()
                            if ask== "yes":
                                operation()
                            elif ask== "no":
                                sys.exit()
                        else:
                            print("You have entered a wrong pin, Kindly check, verify and Try again !!")
                            Repay_Loan()
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
                time.sleep(2)
                print("Dear Member you have entered a wrong input")
                Repay_Loan()                
def status():
    time.sleep(3)
    print("Dear User you are about to verify your payment status") 
    time.sleep(2) 
    emaii=input("Dear User kindly Enter your Email_Address: ")
    time.sleep(1)    
    user= input("Dear User Kindly Enter your Membership_ID: ")   
    val_P=(emaii, user)   
    querry="select * from members where Email_address=%s and Membership_ID=%s"  
    cursor.execute( querry, val_P)  
    date= cursor.fetchone()   
    if date:
        print("Accessing members data page.... ")
        time.sleep(2)
        if date[7]== date[10]:
            print("Paid")
            hull= input("Will you like to perform another operation? ")
            if hull =="yes":
                operation()
            elif hull =="no":
                sys.exit()    
        elif date[7] !=  date[10]:   
            print("Not Paid") 
            hot=input("Will you like to pay now? ").lower().strip()
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
    print("Dear member you are about to verify the interest amount on the loan incured ")
    time.sleep(2)
    client= input("Kindly input your Membership_ID: ")
    val_p= (client, )
    querry=" select * from members where Membership_ID = %s "
    cursor.execute(querry,val_p )
    d_client=cursor.fetchone()
    if d_client:
        ques= input("Have you paid your loan?: ")
        if ques=="yes":
            if d_client[7] == d_client[10]:
                print("Fetching Data ...")
                time.sleep(2)
                print("Acessing Data page")
                time.sleep(3)
                print(f" Dear {d_client[1]} {d_client[2]} the interest charged on your loan insured is {d_client[11]}")
                time.sleep(2)
                ask= input("will you like to perform another transaction? ")
                if ask== "yes":
                    operation()
                elif ask== "no":
                    sys.exit()

            elif d_client[7] != d_client[10]:
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


# # query = "SELECT SUM(Contribution) from members"
# # val = (4,)
# # cursor.execute(query)
# # result = cursor.fetchone()
# # print(result[0])


# val_a=(1, 0, 0, 0)
# querry_e = "INSERT into Coop_Account (ID, Revenue_Generated, Disbursement, Treasure_Balance ) VALUES(%s, %s, %s, %s) " 
# cursor.execute(querry_e, val_a)
# myconn.commit()   