"""
Introduction to Exceptions in Python

In Python, exceptions are errors that occur during program execution. 
They allow your program to handle unexpected situations gracefully 
instead of crashing.

Benefits of using exceptions:
1. Keeps your program running even when an error occurs.
2. Separates normal code from error-handling code, making it cleaner and easier to read.
3. Provides detailed information about what went wrong, which can help with debugging.
4. Encourages robust and maintainable code by forcing you to think about potential errors and how to handle them.
"""

# num1 = int(input("Enter Num1: "))
# num2 = int(input("Enter Num2: "))
# print(f"num1 / num2 is {num1 / num2}.")
# print("Nice program!")
# print("This is the end of the program!")


try:
    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))
    print(f"num1 / num2 is {num1 / num2}.")
except ZeroDivisionError:
    print("ZeroDivisionError! Num2 cannot be 0")
except ValueError:
    print("Invaid input")

print("Nice program!")
print("This is the end of the program!")




# print(f"--- Beginning of More Exception Handling Examples ---\n")

# # Example 1: Handling a division by zero
# def divide(a, b):
#     try:
#         result = a / b
#         print(f"{a} / {b} = {result}")
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero!")
#     finally:
#         print("Finished divide operation.\n")

# divide(10, 2)  # Normal division
# divide(10, 0)  # Division by zero

# # Example 2: Handling multiple exception types
# def access_element(lst, index):
#     try:
#         value = lst[index]
#         print(f"Element at index {index} is {value}")
#     except IndexError:
#         print("Error: Index out of range!")
#     except TypeError:
#         print("Error: Provided input is not a list!")
#     finally:
#         print("Finished access operation.\n")

# my_list = [10, 20, 30]
# access_element(my_list, 1)    # Valid access
# access_element(my_list, 5)    # IndexError
# access_element(100, 0)        # TypeError

# # Example 3: Raising custom exceptions
# def check_positive(number):
#     if number < 0:
#         raise ValueError("Number must be positive!")
#     else:
#         print(f"{number} is positive.\n")

# check_positive(5)
# try:
#     check_positive(-3)
# except ValueError as e:
#     print(f"Caught an exception: {e}")


# print(f"--- End of Exception Handling Examples ---")
    
