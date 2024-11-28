import string as st
import random
print(f"welcome buddy, lets give you a lucky number today {st.whitespace}")

range_ = input("Wanna choose a range (Y/N)?   ")

if range_ == "Y":
    result = ""
    s = int(input("Input the start of the range:    "))
    st = int(input("Input the end of the range:     "))
    result = random.randrange(s, st)
    print(result)
elif range_ == "N":
    result = random._urandom(24)
    print(result)
