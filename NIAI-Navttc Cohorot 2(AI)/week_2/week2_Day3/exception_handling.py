# error during execution(exception) can crash a program if not handle


try:
    num = int(input("enter a number"))
    print(10 / num)

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("that is not a valid number")

finally:
    print("done tring")

# task 1

# two user_input number ,hanling divison by zero
try:
    num_1 = int(input("enter a number"))
    num_2 = int(input("enter a number"))
    print(num_1 / num_2)

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("that is not a valid number")

finally:
    print("done tring")


# task 2

try:
    num_1 = int(input("enter a number"))
    num_2 = int(input("enter a number"))
    print(num_1 / num_2)

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("Sorry bro You have entered non_numeric input enter integer number")

finally:
    print("done tring")




# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input.")
# else:
#     print("You entered:", number)
# finally:
#     print("Program finished.")