#First TP, make a user dictionary and generate a password for the user each time he requests it
import string as st
import random
import art


with_all = str(random.sample(st.printable, 10))

say = "admin"
user_data = {
    "name": say,
    "age": 35,
    "email": "admin@gmail.com",
    "phone": "08089326713",
    "password": [""],
}



def loading():
    print("___________________________________________________________________________________\n###################################################################################\n___________________________________________________________________________________")



empt_pass = "\"your password is empty!!!\""

def view_data(data):
    if data["password"] == "":
        data["password"] = empt_pass

    for key, value in data.items():
        print(f"{key}: {value}")
    return loading()

def make_pass():
    loading()
    pass_opt = int(input(f"""\t Hello {user_data["name"].capitalize()} you have chosen to create a new password for your profile...
                1. create password manually:
                2. use our secure password generator:
                ==> """))
    if pass_opt == 1:
        ask_man_pass = input(f"Type in your desired password:\t")
        if len(ask_man_pass) >= 8 and ask_man_pass.isalnum() and not ask_man_pass.isalpha() and not ask_man_pass.isnumeric() and not ask_man_pass.islower() and not ask_man_pass.isupper():
            renter_pass = input("Confirm your password:\t")
            if ask_man_pass != renter_pass:
                print("Password does not match\n Terminating program...")
                return make_pass()
            else:
                user_data["password"].clear()
                user_data["password"].append(ask_man_pass)
                print(f"strong password \n You have succesfully created your password for {user_data["name"].capitalize()} \n Your new password is {user_data["password"]}")
    elif pass_opt == 2:
        print(f"strong password \n You have succesfully created your password for {user_data["name"].capitalize()} \n Your new password is {ask_man_pass}")
    return loading()

make_pass()
view_data(user_data)
