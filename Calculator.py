# Simple calculator application that asks a user to input two numbers and an operation, display the answer and write the equation to a text file


# Asks the user if they would like to see all saved equations 

user_choice = input('\nWould you like to view all saved equations? Y/N: \n')

# Function to print contents of the equations.txt file

def view_sums():

    # User input file name

    txt_file = input('Please enter the name of the file you wish to view including the file extension. (e.g. equations.txt): ')

    # Check user input is correct 

    if txt_file.lower() == 'equations.txt':

        # Open file, read all lines and print to the terminal minus new line

        with open('equations.txt', 'r') as f:

            for line in f.readlines():

                print(line.strip())


    # Error if user inputs a filename that does not match expected input

    else:
        print('File does not exist, please try again')
        return view_sums()


# Main calculator function # 

def simple_calc():

    if user_choice.lower() == 'n':

        while True:

            # Define filename to opewn later

            file = open('equations.txt', 'a')

            # Request user input

            a = (input('\nPlease enter the first number: \n'))
            op = input('Please enter the required operation (i.e. +, -, x or /): \n')
            b = (input('Please enter the second number: \n'))

            # Check a and b are digits before continuing to prevent program crashing

            while a.isdigit() and b.isdigit():

                # If/elif statements to produce result depending on user operation requests

                if op == '+': 
                    
                    # Cast user inputted numbers to int
                    answer = int(a) + int(b)

                     # String to produce equation and result
                    equation = str(f'\n{a} + {b} = {answer}')

                    # Write equation and result to file
                    file.write(equation) 

                    # Print result to terminal
                    print(f'Result = {answer}')

                    # Ask user if they want to continue
                    cont = input('\nDo you want to continue? Y/N: ') 

                    # If not, exit the program
                    if cont.lower() == 'n': 
                        exit()

                    # Run function again until user quits
                    else:
                        return simple_calc()

                elif op == '-':

                    answer = int(a) - int(b)
                    equation = str(f'\n{a} - {b} = {answer}')
                    file.write(equation)
                    print(f'Result = {answer}')
                    
                    cont = input('\nDo you want to continue? Y/N: \n')
                    if cont.lower() == 'n':
                        exit()
                    else:
                        return simple_calc()

                elif op == 'x':

                    answer = int(a) * int(b)
                    equation = str(f'\n{a} x {b} = {answer}')
                    file.write(equation)
                    print(f'Result = {answer}')

                    cont = input('\nDo you want to continue? Y/N: \n')
                    if cont.lower() == 'n':
                        exit()
                    else:
                        return simple_calc()

                elif op == '/':

                    answer = int(a) / int(b)
                    equation = str(f'\n{a} / {b} = {answer}')
                    file.write(equation)
                    print(f'Result = {answer}')
                    cont = input('\nDo you want to continue? Y/N: \n')
                    if cont.lower() == 'n':
                        exit()
                    else:
                        return simple_calc()

                else:

                    # Errors for incorrect input, return to top of function

                    print('\nIncorrect input, please try again\n')

                    return simple_calc()

            else:
                print('\nIncorrect input, please try again\n')

                return simple_calc()

    else:
        
        view_sums()

simple_calc()