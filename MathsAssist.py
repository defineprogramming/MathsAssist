import time
import os
def clear():
    os.system('cls')
divider = "-------------------------"
# Welcome
print("========== MATHSASSIST STARTED ==========")
time.sleep(1)
print("Welcome to MathsAssist")
print(divider)
# Changelogs
time.sleep(1)
print("v0.2.0 changes:")
print(divider)
print("Added subtraction component")
print("Added multiplication component")
print("Added division component")
print("Removed unneccessary lines")
print("Removed response delays")
print("Program now restarts after each calculation")
print("Added error if response does not exist")
print(divider)
# Main Program & Navigation Interface
while True:
    print("What would you like to do?")
    print(divider)
    print("Options:")
    print("1 | Addition")
    print("2 | Subtraction")
    print("3 | Multiplication")
    print("4 | Division")
    navigation = int(input("Enter a number: "))
    # Addition Module
    if navigation == 1:
        time.sleep(1)
        additionnuma = int(input("Enter number A: "))
        print("========== NUMBER A SUBMITTED ==========")
        additionnumb = int(input("Enter number B: "))
        print("========== NUMBER B SUBMITTED ==========")
        addition = additionnuma + additionnumb
        print("Result is", addition)
    # Subtraction Module
    if navigation == 2:
        time.sleep(1)
        subtractionnuma = int(input("Enter number A: "))
        print("========== NUMBER A SUBMITTED ==========")
        subtractionnumb = int(input("Enter number B: "))
        print("========== NUMBER B SUBMITTED ==========")
        subtraction = subtractionnuma - subtractionnumb
        print("Result is", subtraction)
    # Multiplication Module
    if navigation == 3:
        time.sleep(1)
        multiplicationnuma = int(input("Enter number A: "))
        print("========== NUMBER A SUBMITTED ==========")
        multiplicationnumb = int(input("Enter number B: "))
        print("========== NUMBER B SUBMITTED ==========")
        multiplication = multiplicationnuma * multiplicationnumb
        print("Result is", multiplication)
    # Division Module
    if navigation == 4:
        time.sleep(1)
        divisionnuma = int(input("Enter number A: "))
        print("========== NUMBER A SUBMITTED ==========")
        divisionnumb = int(input("Enter number B: "))
        print("========== NUMBER B SUBMITTED ==========")
        division = divisionnuma / divisionnumb
        print("Result is", division)
    # 404 Error Returned
    else:
        print("Sorry, the command you entered does not exist. (404)")
        time.sleep(2)
        clear()
