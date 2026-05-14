import random
import string

passwords = {}

try:
    with open ("pass.txt","r") as file:
        for line in file:
            website,pwd= line.strip().split(":")
            passwords[website]= pwd

except:
    pass

def generate_pass():
    chars=string.ascii_letters + string.digits + "!@#$"
    password="".join(random.choice(chars) for _ in range(8))

    return password

while True:
    print("......password manager App .....")
    print("1 ---> SAVE PASSWORD ")
    print("2 ---> VIEW PASSWORD ")
    print("3 ---> GENERATE PASSWORD")
    print("4 ---> EXIT")

    choice= input("Enter your choice: ")

    if choice == "1":
        site= input("Enter website: ")
        pwd= input("Enter password: ")

        passwords[site]=pwd

        with open("pass.txt","a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Saved!!!!!!!!!!!!!!!")
    
    elif choice == "2":
        if not passwords:
            print("No data")
        else:
            for site,pwd in passwords.items():
                print(  site,":",pwd)

    elif choice == "3":
        print("GEnerated password:- ",generate_pass())
        
    elif choice == "4":
        print("ok byee...")
        break
    else:
        print("Invalid input!!!!!!!!!!!!!!!!")