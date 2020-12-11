""" This app allows the user to process several mathematical
functions using numpy and panda arrays """

import sys
import numpy as np

print('***************** Welcome to the Python Matrix Application***********')

start = input("Would you like to try things out? Y or N")
if start.upper() == 'Y':

    def phone_format(digits):
        """This method converts a 10 digit number
        into a phone number format with hyphens"""
        return format(int(digits[:-1]), ",").replace(",", "-") + digits[-1]

    # This prompts the user to enter phone number in 10 digit format
    while True:
        try:
            phone = int(input('Enter your phone number using only digits\n'))
            if len(str(phone)) != 10:
                print('The amount of numbers is not correct\n')
                raise ValueError

            if not str(phone).isnumeric():
                print('Your entry is not numeric, enter numbers only')
                raise ValueError

            p = phone_format(str(phone))
            print("The phone number you entered is: " + p)
            break

        except ValueError:
            print('Invalid entry, enter your phone number using numbers only '
                  'i.e. 1234567890\n')

    # This prompts the user to enter zipcode in 9 digit format with hyphen
    while True:
        def zip_split(zips):
            """This method splits the zipcode into 5 numbers before
            the hyphen and 4 numbers after"""
            split_z = zips.split("-")
            return split_z

        try:
            zipcode = (input('Please enter your zipcode in a xxxxx-xxxx format\n'))
            digit = zip_split(zipcode)

            if len(str(zipcode)) != 10:
                print('The amount of numbers is incorrect "-"\n')
                raise ValueError

            if '-' not in zipcode:
                print('Your entry was missing the hyphen\n')
                raise ValueError

            if not digit[0].isnumeric() or not digit[1].isnumeric():
                print('Letters are not allowed, please retry')
                raise ValueError

            print("The zipcode you entered is: " + zipcode + "\n")
            break

        except ValueError:
            print('Invalid entry, please enter your zipcode in a xxxxx-xxxx format '
                  'i.e. 12345-6789\n')

    # begins prompts for matrix number input and operations
    print("The next section works with number matrices and performs math functions")
    print("Enter the number sets for each matrix as 3 digits with a space in between"
          " example 1.5, 2, 3 would be entered 1.5 2 3\n")

    while True:
        def digit_split(numbers):
            """This method splits numbers to individual
            digits for use in matrix operations"""
            split = numbers.split(" ")
            return split


        try:
            # retrieves numbers for 1st set in matrix 1
            matrix = (input("Enter the first set of "
                            "3 numbers for your first matrix\n"))
            while True:
                first_m = digit_split(matrix)
                try:
                    if first_m[0].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if first_m[1].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if first_m[2].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if len(first_m) != 3:
                        print("Incorrect amount of numbers entered")
                        raise IndexError

                    break

                except IndexError:
                    print("Incorrect format, enter each number with a space. Ex. 1 2 3\n")
                    matrix = (input("Enter the first set of "
                                    "3 numbers for your first matrix\n"))

            # retrieves numbers for 2nd set in matrix 1
            matrix2 = (input("Enter the second set of "
                             "3 numbers for your first matrix\n"))
            while True:
                try:
                    first_m2 = digit_split(matrix2)

                    if first_m2[0].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if first_m2[1].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if first_m2[2].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if len(first_m2) != 3:
                        print("Incorrect amount of numbers entered")
                        raise IndexError

                    break

                except IndexError:
                    print("Incorrect format, enter each number with a space. Ex. 1 2 3\n")
                    matrix2 = (input("Enter the second set of "
                                     "3 numbers for your first matrix\n"))

            # retrieves numbers for 3rd set in matrix 1
            matrix3 = (input("Enter the third set of "
                             "3 numbers for your first matrix\n"))
            while True:
                try:
                    first_m3 = digit_split(matrix3)

                    if first_m3[0].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if first_m3[1].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if first_m3[2].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if len(first_m3) != 3:
                        print("Incorrect amount of numbers entered")
                        raise IndexError

                    break

                except IndexError:
                    print("Incorrect format, enter each number with a space. Ex. 1 2 3\n")
                    matrix3 = (input("Enter the third set of "
                                     "3 numbers for your first matrix\n"))

            # retrieves numbers for 1st set in matrix 2
            sec_matrix = (input("Enter the first set of "
                                "3 numbers of your second matrix\n"))
            while True:
                try:
                    sec_m = digit_split(sec_matrix)

                    if sec_m[0].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if sec_m[1].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if sec_m[2].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if len(sec_m) != 3:
                        print("Incorrect amount of numbers entered")
                        raise IndexError

                    break

                except IndexError:
                    print("Incorrect format, enter each number with a space. Ex. 1 2 3\n")
                    sec_matrix = (input("Enter the first set of "
                                        "3 numbers of your second matrix\n"))

            # retrieves numbers for 2nd set in matrix 2
            sec_matrix2 = (input("Enter the second set of "
                                 "3 numbers for your second matrix\n"))
            while True:
                try:
                    sec_m2 = digit_split(sec_matrix2)

                    if sec_m2[0].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if sec_m2[1].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if sec_m2[2].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if len(sec_m2) != 3:
                        print("Incorrect amount of numbers entered")
                        raise IndexError

                    break

                except IndexError:
                    print("Incorrect format, enter each number with a space. Ex. 1 2 3\n")
                    sec_matrix2 = (input("Enter the second set of "
                                         "3 numbers for your second matrix\n"))

            # retrieves numbers for 3rd set in matrix 2
            sec_matrix3 = (input("Enter the third set of "
                                 "3 numbers for your second matrix\n"))
            while True:
                try:
                    sec_m3 = digit_split(sec_matrix3)

                    if sec_m3[0].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if sec_m3[1].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if sec_m3[2].isalpha():
                        print("Please enter numbers only")
                        raise IndexError

                    if len(sec_m3) != 3:
                        print("Incorrect amount of numbers entered")
                        raise IndexError

                    break

                except IndexError:
                    print("Incorrect format, enter each number with a space. Ex. 1 2 3\n")
                    sec_matrix3 = (input("Enter the third set of "
                                         "3 numbers for your second matrix\n"))

            # print matrix 1
            print("Your first matrix is:")
            a = np.asarray([[first_m], [first_m2], [first_m3]], dtype=float)
            print(a)
            print("\n")

            # print matrix 2
            print("Your second matrix is:")

            b = np.asarray([[sec_m], [sec_m2], [sec_m3]], dtype=float)
            print(b)
            print("\n")

            # menu for mathematical options
            while True:
                try:
                    print("1. Add the two matrices together")
                    print("2. Subtract the two matrices")
                    print("3. Multiply the two matrices together")
                    print("4. Element by element multiplication")
                    print("5. Divide the two matrices")
                    print("6. To exit the program")

                    matrix_math = int(input("Please enter the number for "
                                            "the function you would like to perform"))

                    # Addition of matrices
                    if matrix_math == 1:
                        print("Addition\n")
                        print("The sum of the 2 matrices is: ")

                        # print answer
                        add = (np.sum(a + b, axis=1))
                        print(add)

                        # print transpose
                        print("The transpose is: ")
                        print(np.transpose(add))

                        # print mean
                        print("The row and column mean values of the results are:")
                        print("Column")
                        print(add.mean(0))
                        print("Row")
                        print(add.mean(1))

                    # Subtraction of matrices
                    if matrix_math == 2:
                        print("Subtraction")
                        print("The difference between the 2 matrices is: ")

                        # print answer
                        minus = (np.subtract(a, b))
                        print(minus)

                        # print transpose
                        print("The transpose is: ")
                        print(np.transpose(minus))

                        # print mean
                        print("The row and column mean values of the results are:")
                        print("Column")
                        print(minus.mean(0))
                        print("Row")
                        print(minus.mean(1))

                    # Multiplication of whole matrices
                    if matrix_math == 3:
                        print("Multiplication")
                        print("The product of the 2 matrices is")

                        # convert matrix lines to syntax for matmul
                        line_one = (np.matmul([float(first_m[0]), float(first_m[1]),
                                               float(first_m[2])],
                                              [float(sec_m[0]), float(sec_m[1]),
                                               float(sec_m[2])]))

                        line_two = (np.matmul([float(first_m2[0]), float(first_m2[1]),
                                               float(first_m2[2])],
                                              [float(sec_m2[0]), float(sec_m2[1]),
                                               float(sec_m2[2])]))

                        line_three = (np.matmul([float(first_m3[0]), float(first_m3[1]),
                                                 float(first_m3[2])],
                                                [float(sec_m3[0]), float(sec_m3[1]),
                                                 float(sec_m3[2])]))

                        # print answer
                        matrix_array = np.asarray([[line_one], [line_two], [line_three]])
                        print(matrix_array)

                        print("The transpose is: ")
                        print(np.transpose(matrix_array))

                        # print mean
                        print("The row and column mean values of the results are:")
                        print("Column")
                        print(matrix_array.mean(0))
                        print("Row")
                        print(matrix_array.mean(1))

                    # Multiplication of elements in matrices
                    if matrix_math == 4:
                        print("Multiplication")
                        print("The product of each element of the matrices is")
                        multi = np.multiply(a, b)
                        print(multi)

                        print("The transpose is: ")
                        print(np.transpose(multi))

                        print("The row and column mean values of the results are:")
                        print("Column")
                        print(multi.mean(0))

                        print("Row")
                        print(multi.mean(1))

                    # Division of matrices
                    if matrix_math == 5:
                        print("Division\n")
                        print("The quotient of the 2 matrices is:")

                        # print answer
                        divide = np.divide(a, b)
                        print(divide)

                        # print transpose
                        print("The transpose is: ")
                        print(np.transpose(divide))

                        # print mean
                        print("The row and column mean values of the results are:")
                        print("Column")
                        print(divide.mean(0))
                        print("Row")
                        print(divide.mean(1))

                    # Exit application
                    if matrix_math == 6:
                        print('Thank you for trying out the Python Matrix Application')
                        sys.exit()

                    # header at the end of a successful process
                    else:
                        print("Select an option between 1-6\n")

                # error catch for invalid entry at menu
                except ValueError:
                    print("Please enter a number between 1-6\n")

        # error catch for invalid entry during number input
        except ValueError:
            print("Please enter 3 numbers")
else:
    print('Thank you for trying out the Python Matrix Application')
    sys.exit()
