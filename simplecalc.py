# Building a simple Calculator with python
def add(a, b):
    """This function add two numbers
    """
    return a + b

def multiply(a, b):
    """This is a function for multiplication

    """
    return a * b

def subtract(a, b):
    return a - b

def division(a, b):
    return a / b

def exponential(a, b):
    return a ** b
print("""Select an Option:
      \n 1. Addition
      \n 2. Multiplication
      \n 3. Subtraction
      \n 4. Division
      \n 5. Exponential
      
      """)

choice = int(input("Enter choice from 1 - 5: "))


first_number = float(input('Please Enter a number: '))
second_number = float(input('Please Enter another number to be calculated with: '))

if choice == 1:
    print("Addition of {0} and {1} is {2} ".format(first_number, second_number, add(first_number, second_number)))
elif choice == 2:
    print(f"multiplication is {multiply(first_number, second_number)}")

elif choice == 3:
    print(f"subtraction is {subtract(first_number, second_number)}")
    
elif choice == 4:
    print(f"Division is {division(first_number, second_number)}")
    
elif choice == 5:
    print(f"Exponential is {exponential(first_number, second_number)}")
    
else:
    print("Invalid choice")

    
#Message
print("Thank you hope i have helped as your able friend in mathematics")