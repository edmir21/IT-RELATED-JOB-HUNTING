import os 


APPLICANT_FILE = "applicant.txt"
JOBS_FILE = "jobs.txt"

def load_data(filename):
    data = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    entry = {}
                    for pair in line.split(","):
                        if "=" in pair:
                            key, value = pair.split("=", 1)
                            entry[key.strip()] = value.strip()
                    data.append(entry)
    return data



def save_data(filename, data):
    with open(filename, "w")as file:
        for entry in data:
            line = ";". join([f"[{key}={value}" for key, value in entry.items()])
            file.write(line + "\n")

def register_user():
   
    username = input("Enter your username: ").strip()
    if username in load_data(APPLICANT_FILE):
        print(" Username already exits! please try again.")
        return

    password = input("create a password: ").strip()
    fullname = input("Enter your Full name: ").strip()
    address = input("Enter your address").strip()
    age = input("Enter your age: ").strip()
    bday = input("Enter your birthday: ").strip()
    skills = input("Enter your skills in IT fields: ").strip()
    workexp = input("Enter your work experience: ").strip()
    educ = input("Enter your education background: ")
    

    user_data = {
        "passwords": password,
        "fullname": fullname,
        "address": address,
        "age": age,
        "bday": bday,
        "skills" : skills,
        "workexp": workexp,
        "educ": educ,
        "application_status": "Not Applied",
        "messages": ""

    }

    applicant = load_data(APPLICANT_FILE)
    applicant[username] = user_data
    save_data(APPLICANT_FILE, applicant)
    print(f"Applicant {username} registered successfully! ")

def login():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    applicant = load_data(APPLICANT_FILE)
    if username in applicant and applicant[username]["password"] == password:
        print(f"Welcome, {username}!")
        return username
    else:
        print("User name or password incorrect. Please try agian. agian.")
        return None
    
def admin_menu():
    while True:
        print("\n ADMIN MENU ")
        print("1. list of Registered Applicant")
        print("2. Post new Job")
        print("View Job Applications")
        print("4. Exit to Main Menu")
        choice = input ("Enter choice: ").strip()

        if choice == "1":
            list_of_registered_applicant()
        elif choice =="2":
            Post_new_Job ()
        elif choice == "3":
            view_applications_and_message()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def list_of_registered_applicant():
    applicant = load_data(APPLICANT_FILE)
    if not applicant:
        print("No applicant registered yet.")
        return
    for username, details in applicant.items():
        print(f"\n User")



def run_system():
    while True:
        print("\n Welcome to the Recruitment System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            username = login()
            if username:
                if username == "admin":
                    admin_menu()
                else:
                    user_menu(username)
        elif choice == "3":
            print("byebye!")
            break
        else:
            print("Invalid choice. Try again.")