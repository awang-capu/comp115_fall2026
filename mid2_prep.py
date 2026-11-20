"""
Mid2 Exam Preparation Exercises (Optional, but highly recommended)


Objective:
1. Review the function 
2. Review the conditionals (if-else)
3. Review the program flow (for/while - continue, break)
4. Practice when to use and how to operate on the collection data types: 
tuple, list, string, set, dictionary.
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable (accumulator) that is assigned to an integer, a list, etc. 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable.
"""


"""
Exercise 1 - Code tracing

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
practice_if(80, 80)?

Your answer is: 

"""


def practice_if(score, average):
    if score < average:
        print("Do better next time!")
    else:
        if score >= 90:
            print("Woot woot!")
        elif score > 80:
            print("Great job!")
        else:
            print("Nicely done!")


"""
Exercise 2 - Code tracing

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
print(practice_for_if([5, 5, 2, 9], 3))?

Your answer is: 

"""


def practice_for_if(nums, target):
    list = []
    for num in nums:
        if num > target:
            list.append(num)
    return list


"""
Exercise 3 - Code tracing

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
print(practice_function([5, 5, 2, 9, 6]))?

Your answer is: 

"""


def practice_function(nums):
    even_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)


#print(practice_function([5, 5, 2, 9, 6]))
"""
Exercise 4, 5, 6 - Code tracing

First read and understand the following function.
Then answer the questions below:

Question 1: What will it print if we call this function by running 
print(practice_for_index_1([5, 5, 2, 9, 9, 6], 9))?
Your answer is: 


Question 2: Are the function practice_for_index_1(nums, target) and 
the function practice_for_index_2(nums, target) have the same 
functionality? Why?
Your answer is: 


Question 3: Are the function 
practice_for_index_2(nums, target) and the function 
practice_for_index_3(nums, target) have the same 
functionality? Why?
Your answer is: 


"""


def practice_for_index_1(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def practice_for_index_2(nums, target):
    index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            index = i
            break
    return index


def practice_for_index_3(nums, target):
    index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            index = i
    return index


"""
Exercise 7 - Code tracing

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
practice_string("morning")?

Your answer is: 

And what is the time complexity of the algprithm?
"""


def practice_string(s):
    count = 0
    for c in s:
        if c > 'g':
            count += 1
    return count

# print(practice_string("morning"))


"""
Exercise 8 - Code tracing

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
print(summarize_scores(scores))?

Your answer is: 

And what is the time complexity of the algprithm?
"""

def summarize_scores(data):
    total = 0
    count = 0
    for student in data:
        if data[student] >= 70:
            total += data[student]
            count += 1
    return count, round(total / count, 1)

scores = {
    "Alice": 80,
    "Bob":   62,
    "Carol": 90,
    "David": 54,
}

#print(summarize_scores(scores))




"""
Exercise 9 - Coding question

Write a function named "exist_in_both" that takes two strings as input 
and returns the number of characters that occur in both strings.
You can assume that all characters within a string are unique (no repeats).

For example, 
if the function is passed "lap" and "help", 
the function exist_in_both("lap","help") will return 2,
because the characters "l" and "p" occur in both strings.

For example,
exist_in_both("computer","mute") wil return 4.

Function implementation.
Design and pass your own unit tests.

"""


def exist_in_both(str1, str2):
    pass


# Write your unit tests below




"""
Exercise 10 - Coding question

If both adjacent letters in a word are the same, 
we call the two adjacent letters are "good neighbors".

E.g.1, there are one pair of good neighbors inside the word "apple",
since word[1] == word[2], and they are both 'p'.

E.g.2, there are two pairs of good neighbors inside the word "occurrence",
since word[1] == word[2], and they are both 'c'; 
word[4] == word[5], and they are both 'r'.

E.g.3, there are two pairs of good neighbors inside the word "hmmm",
since word[1] == word[2], and they are both 'm'; 
word[2] == word[3], and they are both 'm'.


Write a function called "good_neighbors" that accepts a word as input, 
and return the number of pairs of good_neighbors. 
Assume that all the letters in the word are lowercase letters, 
and there are at least two letters in the word.

For example, good_neighbors("happy") will return 1, 
since there is one pair of adjacent letters 'p'.

good_neighbors("occurrence") will return 2, 
since there are twp pairs of adjacent letters, 'c' and 'r'.

word_example = "arrrrhhh"
good_neighbors(word_example) will return 5, since
word_example[1] == word_example[2], both 'r'
word_example[2] == word_example[3], both 'r'
word_example[3] == word_example[4], both 'r'
word_example[5] == word_example[6], both 'h'
word_example[6] == word_example[7], both 'h'


Hint:

We may compare each letter word[i] with its neighbor word[i + 1], 
while traversing the word using index i. Use the accumulator algorithm pattern.


Function implementation.
Design and pass your own unit tests.
"""


def good_neighbors(word):
    pass


# Write your unit tests below



"""
Exercise 11 - Coding question

Implement a function called "more_than_2" that accepts a list of strings as input. 
The function identifies strings that occur more than two times in the list,
and return these strings as a list. 

Eg.1, fruits = ["apple", "banana", "apple", "apple", "apple", "pear", "orange",
"banana", "banana", "watermelon"] 
more_than_2(fruits) will return ["apple","banana"]. 

Eg.2, colors = ["red", "red", "yellow", "green", "red", "yellow", "orange",
"green", "banana", "yellow"] 
more_than_2(colors) will return ["red", "yellow"]. 

Hint: Utilize dict data type to count the occurrences for each string, 
then traverse all the keys in the dict and compares its value to 3. 
Use the accumulator algorithm pattern.

Function implementation.
Design and pass your own unit tests.
"""

def more_than_2(words):
    pass


# Write your unit tests below



'''
Best of luck with your Mid2 exam preparation!!

Alice
'''
