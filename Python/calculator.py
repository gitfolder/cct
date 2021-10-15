# take user input and validate, keep asking until number given, or quit on CTRL+C or CTR+D
def number_input(text):
    while True:
        try:   return float(input(text))
        except ValueError: print("Not a number")
        except (KeyboardInterrupt, EOFError): raise SystemExit

def print_menu():
    print("\n1. Add\n2. Substract\n3. Multiply\n4. Divide\n0. Exit")
    return number_input("Select option : ")

# recursively calling this function to run
def select_option( opt ):
    if   opt == 0: return
    elif opt == 1: add()
    elif opt == 2: substract()
    elif opt == 3: multiply()
    elif opt == 4: divide()
    else: print("Not an option")
    select_option( print_menu() )
    
def add():
    amount = number_input("Enter how many numbers you want to sum : ")
    total = 0
    for n in range(int(amount)):
        total += number_input("Enter number {0} : ".format(n+1))
    print( "\nSum result : " + str( total ))
    
def substract():
    one = number_input("Provide first number : ")
    two = number_input("Provide second number : ")
    print( "\nSubstraction result : " + str( one-two))

def multiply():
    amount = number_input("Enter how many numbers you want to multiply : ")
    product = 1.0 if amount>0 else 0
    for n in range(int(amount)):
        product *= number_input("Enter number {0} : ".format(n+1))
    print( "\nMultiplication result : " + str( product ))
    
def divide():
    one = number_input("Provide first number : ")
    two = number_input("Provide second number : ")
    if two == 0: print("Cannot divide by zero")
    else:        print( "\nDivision result : " + str( one/two))

select_option( print_menu() ) # initial call