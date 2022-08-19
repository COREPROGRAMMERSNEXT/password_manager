from cryptography.fernet import Fernet


def write_key():
    with open("key.key","wb") as f:
        key = Fernet.generate_key()
        f.write(key)
    return None

try:
    open("key.key")
except:
    write_key()

# secret key
def load_key():
    file = open("key.key","rb")
    key = file.read()
    return key


# master password manager
master_pwd = input("What is the master password :_")

if master_pwd == "":
    pass
else:
    print("wrong password\nquitting...")
    quit()

key = load_key() + master_pwd.encode()
fer = Fernet(key)

# function to list all passwords
def view():
    col_width = 20
    with open('passwords.csv','r') as f:
        for line in f.readlines():
            username, passwd = line.rstrip().split(', ')
            cols_pace = " " * (col_width - len(username))
            print(username, cols_pace, fer.decrypt(passwd.encode()).decode())

        return None

# function to add a new password in file
def add():
    account_name = input("Account name :_")
    passwd = input("password :_")
    with open('passwords.csv','a') as f:
        f.write(f"{account_name}, {fer.encrypt(passwd.encode())}\n")
    return None               


# Main loop
RUNNING = True
while RUNNING:
    mode = input("add a new password(new)\nor view passwords(view)\nPress 'q' to quit :_").lower()

    if mode == "view":
        view()
        pass
    elif mode == "add":
        add()
        pass
    elif mode == "q":
        RUNNING = False
    else:
        print("invalid input....!")
    
    
    
