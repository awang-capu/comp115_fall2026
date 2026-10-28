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
    # return s[::-1]
    res = ''
    for c in s:
        res = c + res
    return res
    

# Write your unit tests below
assert reverse_str("Abd") == "dbA"
assert reverse_str("COMP115") == "511PMOC"


"""
Exercise 2

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string. 
Note that uppercase vowels are also considered vowels.

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
    count = 0
    vowels = 'aeiouAEIOU' #['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] 
                          #('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for c in s:
        if c in vowels:
            count += 1
    return count
    

# Write your unit tests below

assert count_vowels("Apple") == 2
assert count_vowels("Hmmm") == 0

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
    Return a string with duplicate characters removed, keeping the first occurrence.

    E.g.,
    >>> remove_duplicates("apple")
    'aple'
    >>> remove_duplicates("pear")
    'pear'
    """
    res = ''
    for c in s:
        if c not in res:
            res = res + c
    return res


# Write your unit tests below

assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"
assert remove_duplicates("pear") == "pear"


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
    Return the index of the first occurrence of t in s, or -1 if not found.

    E.g.,
    -------
    >>> find_index("hello", "l")
    2
    >>> find_index("Abdccc", 'c')
    3

    """
    # i = -1
    # for c in s:
    #     i += 1 
    #     if c == t:
    #         return i
    # return -1

    for i in range(len(s)):
        if s[i] == t:
            return i
    return -1



# Write your unit tests below

assert find_index("Abd", 'b') == 1
assert find_index("Abdccc", 'c') == 3
assert find_index("Abd", 'w') == -1

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
    Calculate and return the day of the week when a project will be completed.

    E.g., 
    >>> project_completion_day("Monday", 3)
    'Thursday'
    >>> project_completion_day("Friday", 10)
    'Monday'
    """
    today = find_index(days_week, day) # days_week.index(day)
    return days_week[(today + days_to_completion) % 7]

# Write your unit tests below

assert project_completion_day('Monday', 4) == 'Friday'
assert project_completion_day('Monday', 7) == 'Monday'
assert project_completion_day('Saturday', 2) == 'Monday'
assert project_completion_day('Saturday', 1) == 'Sunday'


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
    """
    Calculate and return the number of days whose names start with character c.

    E.g.,
    >>> count_days_starting_with('T')
    2
    >>> count_days_starting_with('M')
    1
    """
    count = 0
    for day in days_week:
        if day[0] == c:
            count += 1
    return count

assert count_days_starting_with('T') == 2
assert count_days_starting_with('M') == 1


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
    """
    Find and return the name of the student with the highest score.

    E.g.,
    >>> highest_score([("Alice", 85), ("Bob", 92), ("Carol", 78)])
    'Bob'
    >>> highest_score([("David", 88), ("Emma", 95), ("Frank", 80)])
    'Emma'
    """
    name_highest = ''
    score_highest = 0
    for s in students:
        if s[1] > score_highest:
            score_highest = s[1]
            name_highest = s[0]
    return name_highest

    # name_highest = ''
    # score_highest = 0
    # for name, score in students:
    #     if score > score_highest:
    #         score_highest = score
    #         name_highest = name
    # return name_highest


assert highest_score([("Alice", 85), ("Bob", 92), ("Carol", 78)]) == "Bob"
assert highest_score([("Tom", 90), ("Amy", 95), ("Sam", 88)]) == "Amy"
assert highest_score([("David", 75)]) == "David"



"""Log Parsing Exercise (Optional Challenge)

You are given a log string containing application logs 
in a standardized format. Each log entry contains 
a timestamp, severity level, module name, and message.
Your task is to parse and analyze these logs.

As in log_string below, the log format - each log line follows this pattern:
YYYY-MM-DD HH:MM:SS [LEVEL] module.py Message
"""


log_string = """2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect
"""


"""
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
list = ['Hello,', 'world!']
' '.join(list)
# Returns 'Hello, world!'
"""

def parse_log_line(line):
    parts = line.split()
    return (parts[0] + ' ' + parts[1], parts[2][1:-1], parts[3], ' '.join(parts[4:]))
    # return (' '.join(parts[:2]), parts[2][1:-1], parts[3], ' '.join(parts[4:]))

# Your unit tests
line = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
assert parse_log_line(line) == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')



"""Now use your parse_log_line() to parse all the lines in the sample data log_string,
and store each tuple item in a list.
Hint: log_string.splitlines() will return a list of lines with a skip for empty lines."""
entries = []
lines = log_string.splitlines()
for line in lines:
    entries.append(parse_log_line(line))
#print(entries)



"""Now you can use what you've learnt about accumulator algorithm to do more data analyzing. 
For example, to count how many ERROR logs there."""
count_error = 0
for entry in entries:
    if entry[1] == 'ERROR':
        count_error += 1
#print(count_error)

"""
Remember to complete the lab quiz on e-learn. That's all for this lab!
"""
