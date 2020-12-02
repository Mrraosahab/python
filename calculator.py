# Hello this is a simple python calculator
#Created by Pradeep Kumar Yadav

# Here we are creating some functions

# add two number
def add(x, y):
    return x+y


# subtract two numbers
def sub(x, y):
    return x-y


# multiply two numbers 

def mul(x, y):
    return x*y


# divide two numbers

def div(x, y):
    return x/y




# Here we are creating a while loop for re-execute the code

while True:
    print('''\nEnter 1 for Addition \nEnter 2 for Subtraction \nEnter 3 for Multiplication \nEnter 4 for Division''')
    choice = input("\nEnter a choice: ")

    # this is first condition for our program, here we are asking to the user to enter a choice
    # We are taking the user's choice as a string
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter First number: "))
        num2 = float(input("Enter Second number: "))
        
        if choice=="1":
            print(add(num1, num2))

        elif choice=="2":
            print(sub(num1, num2))

        elif choice=="3":
            print(mul(num1, num2))

        elif choice=="4":
            if num2==0:
                print("The", num1 ,"can not be divided by Zero")
            else:
                print(div(num1, num2))
            

        break
    else:
        print("\nPlease enter a valid number")