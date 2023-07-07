# Building a simple Calculator with python
import mod as mod
def calc_run():
    print("""What type of mathematical operation would you like to carry out?
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
        return mod.add(first_number, second_number)
    elif choice == 2:
        return mod.multiply(first_number, second_number)

    elif choice == 3:
        return mod.subtract(first_number, second_number)
        
    elif choice == 4:
        return mod.division(first_number, second_number)
        
    elif choice == 5:
        return mod.exponential(first_number, second_number)
        
    else:
        print("Invalid choice")

        
    #Message
    print("Thank you hope i have helped as your able friend in mathematics")