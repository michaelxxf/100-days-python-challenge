#First TP, make a user dictionary and generate a password for the user each time he requests it
import string as st
import random

user_data = {
    "name": "admin",
    "age": 35,
    "email": "admin@gmail.com",
    "phone": int("08089326713"),
    "password": "",
}
with_all = st.printable
with_digits = st.digits
with_alpha = st.ascii_letters
with_specials = st.punctuation
# print(random.sample(with_all, 7))
# print(random.sample(with_all, 7))
# print(random.sample(with_all, 7))
# print(random.sample(with_all, 7))
# print(random.sample(with_all, 7))
# print(random.sample(with_all, 7))
# notw = ""
# print(notw)
# print(notw.join(with_all))
# notw = random.sample(with_all, 7)
# print(notw)
# def pass_gen(s, paswd_option):
#     result =""
#     result.join(random.sample(paswd_option, s))
#     return result
#     print(result)

# # s = int(input("length of generated password:    "))
# # paswd_option = st.ascii_letters
# # s = 6

# pass_gen(7, with_alpha)

result ="hd"
result.join(random.sample(with_all, 5))
print(result)