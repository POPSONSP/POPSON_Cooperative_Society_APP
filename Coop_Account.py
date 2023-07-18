import time
def index():
    print("Welcome to POPSON Cooperative APP, Kindly proceed by following the neccesary Command !!!")
    time.sleep(3)
    print("""
    Enter 1 to proceed as a member 
    Enter 2 to proceed as a non user
          """)
    response= input(">>> ")
    if response =="1":
        from member import welcome
        welcome()
    elif response =="2":
        from user import welcome
        welcome() 
    else:
        print("Dear esteemed user you have entered a wrong input, Kindly Try Again !!!")
        response= input(">>> ")   
index()            