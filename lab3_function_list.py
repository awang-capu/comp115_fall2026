"""
Lab 3 - Functions and Lists (including 8 exercises)

Objective:
1. Practice coding simple Python functions and writing unit tests testing functions by assert
2. Practice how to operate on lists
3. Practice with iterations using loop
4. Practice using the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, etc. 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Example 1: 

To implement a function for calculating the perimeter of a rectangle,
we know this function should have two parameters as inputs: length and width
of a rectangle.
We should also know this function should return a value of the perimeter.
Before or after our function implementation, we know that our function, let's say,
function's name is rectangle_perimeter, shoud pass the unit tests such as:
assert rectangle_perimeter(5, 6) == 22
assert rectangle_perimeter(1.25, 2.43) == 7.36
assert rectangle_perimeter(1.001, 2.005) == 6.01
"""

def rectangle_perimeter(length, width):
    perimeter = (length + width) * 2
    return round(perimeter, 2) # Round to the result to two decimal places


assert rectangle_perimeter(5, 6) == 22
assert rectangle_perimeter(1.25, 2.43) == 7.36
assert rectangle_perimeter(1.001, 2.005) == 6.01

"""
Exercise 1 (10 marks)

1 US dollar is around 1.34 Canadian dollars.
Write a function that takes American dollars as input 
and return the Canadian dollars equivalent. 

Requirement: Use round() to round the result to two decimal places.
For example, convert_american_dollars(100.05) should return 134.07

Uncomment the unit tests below to verify your function implementation.
"""


def convert_american_dollars(american_dollars):
    pass

# assert convert_american_dollars(1) == 1.34
# assert convert_american_dollars(100) == 134
# assert convert_american_dollars(100.05) == 134.07


"""
Exercise 2 (10 marks)

Suppose the days of the week are numbered as follows:
Monday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3,
Friday = 4, Saturday = 5, Sunday = 6
You are going on a trip that lasts n days.

Implement a function named back_day_from_trip
with day_today and days_trip as input parameters, and return the name
of the back day from the trip. 

E.g.1, day_today is 0, which is Monday, and the days_trip is 2,
you will be back on "Wednesday", so your function will return "Wednesday".

E.g.2, day_today is 1, which is Tuesday, and the days_trip is 9,
you will be back on "Thursday", so your function will return "Thursday".

Your function should be able to pass the unit tests below. 

Hints: day_back = (day_today + days_trip) % 7
days_week[0] will be "Monday"

Uncomment the unit tests below to verify your function implementation.
"""

days_week = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]
def back_day_from_trip(day_today, days_trip):
    pass

# assert back_day_from_trip(3, 5) == "Tuesday"
# assert back_day_from_trip(1, 2) == "Thursday"
# assert back_day_from_trip(1, 7) == "Tuesday"
# assert back_day_from_trip(1, 9) == "Thursday"




"""
Example 2 - To implement our own sum function that takes a list of numbers
as a parameter and returns the sum of the numbers.
"""
def my_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

assert my_sum([1, 4, 5]) == 10
assert my_sum([9, 5]) == 14


"""
Exercise 3 (10 marks) - From interactive textbook 10.31.4

Write a function called average that takes a list of numbers as a parameter 
and returns the average of the numbers.

(Note: there is a built-in function named sum() but pretend you cannot use it.)

Uncomment the unit tests below to verify your function implementation.

"""

# Function implementation (10 marks)
def average(nums):
    pass



# assert average([1, 2, 3]) == 2
# assert average([1, 2, 3, 4]) == 2.5
# assert average([2, 9, 2]) == 4.33



"""
Exercise 4 (10 marks)

Write a function called sum_of_first_3(nums) to return the sum of the 
first three numbers in the list of nums.

Assume the input nums is a list of numbers, and will always have no less than 3 elements.
"""

# Function implementation (10 marks)
def sum_of_first_3(nums):
    pass



# assert sum_of_first_3([1, 2, 3]) == 6
# assert sum_of_first_3([1, 2, 30, 4]) == 33
# assert sum_of_first_3([-1, 9, 2, 100]) == 10



"""
Exercise 5 (10 marks) - From interactive textbook 10.31.6

Write a function sum_of_squares(nums) that 
computes the sum of the squares of the numbers in the list nums. 
For example, sum_of_squares([2, 3, 4]) should return 4 + 9 + 16 which is 29:

Hint: you can use the power operator ** to calculate square

Uncomment the unit tests below to verify your function implementation.

"""

# Function implementation
def sum_of_squares(nums):
    pass

# assert sum_of_squares([2, 3, 4]) == 29
# assert sum_of_squares([2, 4]) == 20
# assert sum_of_squares([]) == 0


"""
Exercise 6 (10 marks)

Write a Python function named add_number that adds a constant k to every element,
and return the list. 

Uncomment the unit tests below to verify your function implementation.

"""

# Function implementation 
def add_number(nums, k):
    pass

# assert add_number([2, 4, 1], 5) == [7, 9, 6]
# assert add_number([7, 8], -5) == [2, 3]


"""
Exercise 7 (20 marks) 

Write a function called squares() that takes a list of numbers nums as its parameter 
and returns a list of nums' squares.

For example,
squres([1, 2, 3, 4]) will return [1, 4, 9, 16]
squares([2, 4, 6, 7, 8]) will return [4, 16, 36, 49, 64]

Hint:
Create a variable assigned to an empty list [], 
and use the append() to add the required elements to the list.

Uncomment the unit tests below to verify your function implementation.

"""

# Function implementation
def squares(nums):
    pass


# assert squares([2, 3, 4]) == [4, 9, 16]
# assert squares([2, 4]) == [4, 16]
# assert squares([5, 6, 7]) == [25, 36, 49]
# assert squares([]) == []


"""
Exercise 8 (20 marks) 

Write a function called repeat_elements() that takes a list of numbers nums as its parameter 
and returns a list of repeating each element twice.

For example,
repeat_elements([1, 2, 3, 4]) will return [1, 1, 2, 2, 3, 3, 4, 4]
repeat_elements([2, 7, 8]) will return [2, 2, 7, 7, 8, 8]

Hint:
Create a variable assigned to an empty list [], 
and use the append() to add the required elements to the list.


Uncomment the unit tests below to verify your function implementation.
"""

# Function implementation 
def repeat_elements(nums):
    pass


# assert repeat_elements([1, 2, 3, 4]) == [1, 1, 2, 2, 3, 3, 4, 4]
# assert repeat_elements([2, 7, 8]) == [2, 2, 7, 7, 8, 8]
# assert squares([]) == []




"""
Now finish the quiz_lab3 on e-learn. That's all for lab3.
"""
