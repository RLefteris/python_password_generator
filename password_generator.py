import random, string
from time import sleep

chars = list(string.ascii_letters + string.digits + "!@#$^&*()/")
def genr_passwd():
    pass_len = int(input("How long you want your password to be ---> "))
    random.shuffle(chars)
    password = []
    for x in range(pass_len):
        password.append(random.choice(chars))
    random.shuffle(password)
    password = "".join(password)
    print("\nYour password is -->> ",password)

option = input("Do you want to generate a password? (Yes/No) -> ")

if option.lower() == "yes":
    genr_passwd()
else:
    print("Program will terminate in 2 seconds")
    sleep(2)
    quit()