#creating database

data= {
        'name': ['sachin', 'tanuj'],
        'age': [22,25],
        'email': ['sachin@gmail.com', 'tanuj@gmail.com'],
        'pin': ['1234', '1234'],
        'amount': [20000, 10000],
    }


def choose1():
    """This funtion is 
    the first choise to make"""
    choice1= int(input("Enter your choice (in numbers): \n 1. SignUp \n 2. Signin \n 3. Forget Password \n 4. Exit \n" ))
    if (choice1 == 1):
        signup()
    elif(choice1 == 2):
        login()
    elif(choice1==3):
        forget()
    elif(choise2==4):
        exit()
    else:
        print("Invalid choice. Please enter a corresponding number")
        choose1()

def choose2():
    """ this funtion is
    to choose part2"""
    choice2= int(input("Enter your choice (in numbers): \n 1. Check Balance \n 2. Deposit \n 3. Whithdrawal \n 4. Change pin \n 5. LogOut \n"))
    if (choice2 == 1):
        balance()
    elif(choice2 == 2):
        deposit()
    elif(choice2==3):
        withdraw()
    elif(choice2==4):
        pinchange()
        exit()
    else:
        print("Invalid choice. Please enter a corresponding number")
        choose2()    
        
def login():
    """This function is 
    to login"""
    uname = input("Enter Account Name: ")
    pwd = input("Enter PIN")
    if uname in data['name'] and pwd in data['pin']:
            print("Login Success")
            choose2()
    else:
        print("Account does not exist")
        choose1()
    
    
def signup():
    """This funtion is
    to signup"""
    uname = input("Enter your name: ")
    data['name'].append(uname)
    age = int(input("Enter your age: "))
    data['age'].append(age)
    email = input("Enter your email id: ") 
    data['email'].append(email)
    pin = input("Enter your new PIN: ")
    data['pin'].append(pin)
    amount = (int(input("Enter the amount in your account: ")))
    data['amount'].append(amount)
    print("You have successfully created your account. WELCOME!")
    choose1()
    
def exit():
     """This funtion is
    to logout"""
    print("You are succesfullly Logged Out from the session. \n Thank You. Come Again")
    
def withdraw():
     """This funtion is
    to withdraw"""
    uname=input("enter your name")
    draw=int(input("Enter amount to withdraw: "))
    for i in range(len(data['name'])):
            if data['name'][i] == uname:
                if data['amount'][i] > draw:
                    data['amount'][i]-= draw
                    print("You have drawn Rs.", draw)
                    print("Your balance now is ",data['amount'][i]) 
                else:
                    print("Sorry!! You have no enough balance; Rs.", data['amount'][i] )
                    choose2()
    
def deposit():
     """This funtion is
    to deposit"""
    uname=input(enter your name)
    depo = int(input("Enter amount to deposit: "))
        for i in range(len(data['name'])):
            if data['name'][i] == uname:
                data['amount'][i] += depo
                print("Rs.",depo,"is successfully credited")             
                print("Your new balance is ", data['amount'][i])
                choose2()
        
def balance():
    """This funtion is
    to check balance"""
    uname=input(enter your name)
        for i in range(len(data['name'])):
            if data['name'][i] == uname:
                print("Your new balance is ", data['amount'][i])
                choose2()
    
def pinchange():
    """This funtion is
    to change pin or for forget pin option"""
    email = input("Enter your email id")
    for i in range(len(data['email'])):
        if data['email'][i] == email:
            new = input("Enter new PIN ")
            new1 = input("Confirm the PIN ")
            if new== new1:
                data['pin'][i] = new
                print("PIN is Successfully Changed")
                choose1()
            else: 
                print("PIN doesn't match. try again")
                pinchange()
        else:
            print(" Email not found. Try Agian")
            pinchange()

choose1()
