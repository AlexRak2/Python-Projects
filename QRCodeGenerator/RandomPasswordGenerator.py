import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password(length):
    random.shuffle(characters)
    password = []

    for x in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)

def main():
    option = input("Do you want to generate a passowrd (y/n)? ")

    if option == "y" or option == "Y":
        password_length = int(input("How long should your password be? "))
        password = generate_password(password_length)
        print(password)

    elif option == "n" or option == "N":
        print("Application Stopping....")
        quit()
    else:
        print("Invalid Input, Try Again")
        main()

main()


