import sqlite3
import time

con = sqlite3.connect("personal_project1.db")
cur = con.cursor()
import time

def seconds(n):
    return time.sleep(n)

print("Welcome to RunFree!\n")

seconds(3)

print("I'll help you find the right training program for ya...\n")

seconds(3)

cur.execute('''
CREATE TABLE IF NOT EXISTS user (
user_id INTEGER PRIMARY KEY,
username TEXT, 
password TEXT)
'''
)
con.commit()

i=1

# LOGIN SCREEN------------------------------------------------------------------------------------------------------------------------------------

login_1=str(input("Let's get started! If you already have an account, type \"Y\". Otherwise, type \"N\" to get started\n"))

reset = "N/A"
# While loop to keep trying if user gets something wrong in the login
while i > 0:
    if login_1 == "Y" or reset == "Y":
        login_1="N/A"
        # Another while loop to keep trying if username is incorrect
        while True:
            login_2U = input("Username: ")
            login_2P = input("Password: ")
            # Getting user input and extracting it from "user" database (U and P)
            cur.execute("SELECT username FROM user WHERE username=?", (login_2U,))
            con.commit()
            username=cur.fetchone()
            cur.execute("SELECT password FROM user WHERE password=?", (login_2P,))
            con.commit()
            user_pw=cur.fetchone()
            # If login is correct, BAAAAANG
            if username is not None and user_pw is not None:
                print(f"Welcome to RunFree, {login_2U}!") 
                break
            elif username is None:
                print("Username not found. Try again")
                seconds(1)
            elif user_pw is None:
                print("Incorrect password. Try again")
                seconds(1)
        i -= 1    
    # Adding new user info to the "user" database
    elif login_1 == "N":
        print("Create account\n") 
        login_1U = input("Username: ")
        login_1P = input("Password: ")
        # Inserting new account input into "user" database
        # Added except if account already exists
        try:
            cur.execute('''
                        INSERT INTO user (username) VALUES (?)
                        ''', (login_1U,))
            cur.execute('''
                        INSERT INTO user (password) VALUES (?)
                        ''', (login_1P,))
            con.commit()
            print("Successful login")
            seconds(3)
            # Back to beggining... 
            reset = str(input("Type \"Y\" to go back to the log in.\n"))    
        except sqlite3.IntegrityError:
            print("Account already exists")
            seconds(3)
            # Back to beggining...
            reset = str(input("Type \"Y\" to go back to the log in.\n"))

# LOGIN SCREEN-----------------------------------------------------------------------------------------------------------------------------------------

# IF USER HAS NO RUNNING PLAN--------------------------------------------------------------------------------------------------------------------------

if login_1U: #doesnt have table:
    print("It seems you're new here! Let me introduce you to RunFree... \n")
    seconds(3)
    print("blah blah blah\n")
    seconds(3)
    print("Ready to get started?")
    seconds(3)
    while True:
        continue_no_plan1=input("Type \"Y\" to begin building the right plan for YOU!")
        if continue_no_plan1=="Y":
            print("poop")
            break
        else:
            print("make sure you type capital \"Y\" to get started!!!")

    # Gathering info on USERRRR
    print(f"Great! Let's gather some personal info so we can make the perfect plan tailored for you, {login_1U}.\n")

    # AGE ()
    age=int(input("How old are you?\n"))

    # GENDER (Male, Female, Other)
    while True:
        print("What's your gender?\n")
        gender=input("Type \"Male\", \"Female\", or\"Other\"\n") 
        if gender=="Male" or gender=="Female" or gender=="Other":
            break
        else:
            print("Make sure you type the word exactly as it shows!!!")

    # RUNNING EXPERTISE (Begginer, Intermediate, Advanced)
    while True:
        print("How experienced are you?")
        r_s=("\"Beginner\", \"Intermediate\", or \"Advanced\"\nPs. Don't know? Type \"I\" to figure out what you should pick!\n")
        if r_s=="I":
            print("Blah")
        elif r_s=="Beginner" or r_s=="Beginner" or r_s=="Beginner":
            break
        else:
            print("Make sure you type the word exactly as it shows!!!")


    cur.execute('''
    SELECT * WHERE 
    
    
    '''
    )
    



# IF USER HAS NO RUNNING PLAN----------------------------------------------------------------------------------------------------------------------------

# IF USER HAS RUNNING PLAN-------------------------------------------------------------------------------------------------------------------------------

# IF USER HAS RUNNING PLAN-------------------------------------------------------------------------------------------------------------------------------
con.close()