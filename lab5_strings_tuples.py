"""
Lab 5 - Strings and Tuples 

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 

Complete the function below to reverse a string.
Please use the accumulator algorithm instead of return s[::-1].

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the string concatenation using the operator '+'
"""
def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'
    """
    pass
    

# Write your unit tests below



"""
Exercise 2

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2
    """
    pass
    

# Write your unit tests below



"""
Exercise 3 

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: in
"""
def remove_duplicates(s):
    """
    Write your docstring
    """
    pass


# Write your unit tests below



"""
Exercise 4

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""
def find_index(s, t):
    """
    Write your docstring
    """
    pass


# Write your unit tests below



"""
Exercise 5

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


def project_completion_day(day, days_to_completion):
    """
    Write your docstring
    """
    pass

# Write your unit tests below




"""
Exercise 6

Write a function count_days_starting_with(c) that takes a character c
and returns the number of days in days_week whose names start with c.

Note: we've declared a tuple of days_week in line 136, which is
days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')

E.g.,

count_days_starting_with('T') returns 2, because of 'Tuesday' and 'Thursday'.
count_days_starting_with('M') returns 1, because of 'Monday'.
count_days_starting_with('S') returns 2, because of 'Saturday' and 'Sunday'.
count_days_starting_with('X') returns 0, because of no element in days_week starts with 'X'.

"""

def count_days_starting_with(c):
    # Your code here
    pass


assert count_days_starting_with('T') == 2
assert count_days_starting_with('S') == 2
assert count_days_starting_with('M') == 1
assert count_days_starting_with('W') == 1
assert count_days_starting_with('F') == 1
assert count_days_starting_with('X') == 0


"""
Exercise 7

Write a function highest_score(students) that takes a list of student records and
returns the name of the student with the highest score. 
Each student record contains a student's name and score, in the format (name, score).

Hints:
1. Use a loop to examine each student's record.
   You can use 
   for s in students:
   to iterate through the students list. Then use s[0] to get the current element's name,
   and s[1] to get its score.
   
   Or, you can use 
   for name, score in students:
   to iterate through the students list. Python automatically unpacks each student record 
   into the two variables name and score. This works because each record contains
   exactly two values, whether the record is a tuple or a list.
2. Track the highest score and the corresponding student's name.
3. If multiple students have the same highest score, return the name of the first student with that score.
"""

def highest_score(students):
    # Your code here
    pass


assert highest_score([("Alice", 85), ("Bob", 92), ("Carol", 78)]) == "Bob"
assert highest_score([("Tom", 90), ("Amy", 95), ("Sam", 88)]) == "Amy"
assert highest_score([("David", 75)]) == "David"



"""Log Parsing Exercise (Optional Challenge)

You are given a log string containing application logs 
in a standardized format. Each log entry contains 
a timestamp, severity level, module name, and message.
Your task is to implement two functions to parse and filter
these logs.

Log format - Each log line follows this pattern:
YYYY-MM-DD HH:MM:SS [LEVEL] module.py Message

Sample log data:
log_string = "
2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect
"

Implement a function parse_log_line(line) to parse a single log line into its components.

Your function returns:
A tuple of 4 elements: (timestamp, level, module, message)

timestamp (str): Date and time in format "YYYY-MM-DD HH:MM:SS"
level (str): Log severity level ("ERROR", "WARNING", or "INFO")
module (str): The Python module/file name (e.g., "database.py")
message (str): The log message text

E.g.,
line = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
parse_log_line(line) == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')

Hints:
1. str.split() returns a list of strings, split by default (whitespace).
"hello world python".split()
# Returns: ['hello', 'world', 'python']

2. string concatenation
'I like ' + 'you'
# Returns 'I like you'

3. str.join()
list = ['Hello, ', 'world!']
' '.join(list)
# Returns 'Hello,  world!'
"""

def parse_log_line(line):
    pass




# Your unit tests




# Use your parse_log_line() to parse all the lines in the sample data log_string,
# and store each tuple item in a list.
# Hint: log_string.split('\n') will return a list of lines.




"""
Remember to complete the lab quiz on e-learn. That's all for this lab!
"""
