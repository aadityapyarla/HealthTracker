# Health Management System
import os
from datetime import datetime


def time_stamp():
    return str(datetime.now().strftime("%d/%m/%Y %I:%M:%S %p"))


def log(user_name):
    user_exists = os.path.isfile(f"{user_name}_food.txt")
    if not user_exists:
        print("You are not registered!")
        create = input("Wanna register?(y/n): ").lower()
        if create == "y":
            action = int(input("(1) for Food log (2) for exercise log: "))
            if action == 1:
                log = input("Enter your food log: ").capitalize()
                with open(f"{user_name}_food.txt", "a") as file_1:
                    file_1.write(f"[{time_stamp()}]: {log}\n")
                    print("Successfully Logged!")
                with open(f"{user_name}_exe.txt", "a"):
                    pass
            elif action == 2:
                log = input("Enter your exercise log: ").capitalize()
                with open(f"{user_name}_exe.txt", "a") as file_2:
                    file_2.write(f"[{time_stamp()}]: {log}\n")
                    print("Successfully Logged!")
                with open(f"{user_name}_food.txt", "a"):
                    pass
            else:
                print("I didn't understand?")

        else:
            print("Thank you for using Health Manager")
    else:
        action = int(input("(1) for Food log (2) for exercise log: "))
        if action == 1:
            log = input("Enter your food log: ").capitalize()
            with open(f"{user_name}_food.txt", "a") as file_1:
                file_1.write(f"[{time_stamp()}]: {log}\n")
                print("Successfully Logged!")
        elif action == 2:
            log = input("Enter your exercise log: ").capitalize()
            with open(f"{user_name}_exe.txt", "a") as file_2:
                file_2.write(f"[{time_stamp()}]: {log}\n")
                print("Successfully Logged!")
        else:
            print("I didn't understand?")


def retrieve(user_name):
    user_exists = os.path.isfile(f"{user_name}_food.txt")
    if not user_exists:
        print("You are not registered!")
        create = input("Wanna register?(y/n): ").lower()
        if create == "y":
            with open(f"{user_name}_food.txt", "a"):
                pass
            with open(f"{user_name}_exe.txt", "a"):
                pass
            print("Your registered successfully! Log something to retrieve.")
        else:
            print("Thank you for using Health Manager")
    else:
        retrieve = int(input("(1) for Food log (2) for exercise log: "))
        if retrieve == 1:
            with open(f"{user_name}_food.txt") as file:
                for line in file:
                    print(line, end="")
            print("Successfully retrieved")
        elif retrieve == 2:
            with open(f"{user_name}_exe.txt") as file:
                for line in file:
                    print(line, end="")
            print("Successfully retrieved")
        else:
            print("I didn't understand")

try:
    print("Welcome to your Health Manager")
    print("(1) to log and (2) to Retrieve")
    action = int(input("Enter number for action: "))
    user_name = input("Enter your name: ")
    if action == 1:
        log(user_name)
    elif action == 2:
        retrieve(user_name)
    else:
        print("I didn't understand?")
except KeyboardInterrupt:
    pass