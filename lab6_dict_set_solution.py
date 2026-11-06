"""
Lab 6 - Set and Dict 
(5 exercises in total)

Objective:
1. Review how to write a good python docstring (started from last lab).
2. Review how to code simple Python functions and write unit tests using assert.
3. Practice how to operate on set and dict.
4. Review iterations using loop.
5. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, a set, a dict, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Here is one solution of Lab 5 exercise 3: Remove the duplicate characters in a string.
E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"
"""
def remove_duplicates(s):
    """
    This function removes the duplicates from the string s.

    E.g.,
    >>> remove_duplicates("Apple")
    "Aple"
    """
    res = ''
    for c in s:
        if c not in res:
            res += c
    return res
    
# Your unit tests
assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"

"""
Exercise 1

Can you try to implement the above duplicates removal using data type set?

Hint: 1. We put the seen chars in the set while adding them to the res string;
      We also check if the new char is already in the set (more efficient than checking a string). If not seen, add it to the res string.
      2. To initialize an empty set: seen_set = set()
"""
def remove_duplicates_set(s):
    """
    This function removes the duplicates from the string s.

    E.g.,
    >>> remove_duplicates("Apple")
    "Aple"
    """
    res = ''
    seen_set = set()
    for c in s:
        if c not in seen_set:
            res += c
            seen_set.add(c)
    return res
    

# Your unit tests
assert remove_duplicates_set("apple") == "aple"
assert remove_duplicates_set("Popsipple") == "Popsile"

"""
Exercise 2

Assume you've collected many stones, 
and each character in the string stones represents a type of a stone. 
And each character in the string gems represents a type of a gem.

Write a function to calculate how many stones you've collected are actually jems. 
Requirement: Implement the function using data type set

E.g.,
gem_counting("abDFMdm", "admMQq") will return 4
gem_counting("abDFMdm", "af") will return 1
gem_counting("awCcM", "cQqW") will return 1
gem_counting("bFfL", "cQqW") will return 0

Hint: 
You can convert a list l (or a tuple, or a str) to a set with unique elements using set(l).
"""
def gem_counting(stones, gems):
    """
    This function returns the number of characters in the string stones that is also in the string gems

    E.g.,
    gem_counting("abDFMdm", "admMQq") will return 4
    gem_counting("abDFMdm", "af") will return 1
    """
    gems_set = set(gems)
    count = 0
    for c in stones:
        if c in gems_set:
            count += 1
    return count

# Your unit tests
assert gem_counting("abDFMdm", "admMQq") == 4
assert gem_counting("abDFMdm", "af") == 1
assert gem_counting("awCcM", "cQqW") == 1
assert gem_counting("bFfL", "cQqW") == 0




"""
Exercise 3

CapU is planning to launch a shuttle bus between main campus 
and the students accomendation. (Fake news but best wishes 😄)

To determine how many buses are needed each day, 
CapU keeps track of the students who use the shuttle bus service.

Write a function students_id() that takes a list of student ids as its parameter, 
and returns the number of different students who use the shuttle service.

E.g.,
students_id(['002', '003', '001', '004', '012']) returns 5
students_id(['002', '003', '001', '012', '003', '001']) returns 4

Hint: 
Think about which data type we should use to ease the work of finding distinctive values from a list.

"""
def students_id(ids):
    """
    Returns the number of different elements

    E.g.,
    students_id(['002', '003', '001', '004', '012']) returns 5
    students_id(['002', '003', '001', '012', '003', '001']) returns 4
    """
    # s = set(ids)
    # return len(s)
    return len(set(ids))
    

# Your unit tests

assert students_id(['002', '003', '001', '004', '012']) == 5
assert students_id(['002', '009', '001', '004', '012', '003', '003', '004']) == 6

"""
Exercise 4

Similar as exercise 3, write a function called students_id_occurrences() 
that takes a list of student ids as its parameter, 
and returns the occurences of each different student 
who uses the shuttle service in the form of dictionary data type.

E.g.,
students_id_occurrences(['002', '003', '001', '004', '012']) 
returns {'002': 1, '003': 1, '001': 1, '004': 1, '012': 1}}

students_id_occurrences(['002', '003', '001', '012', '003', '001']) 
returns {'002': 1, '003': 2, '001': 2, '012': 1}

Hint: To initialize an empty dict: id_dict = {}
"""
def students_id_occurrences(ids):
    """
    Returns the occurences of different elements in a dict

    E.g.,
    students_id_occurrences(['002', '003', '001', '004', '012']) 
    returns {'002': 1, '003': 1, '001': 1, '004': 1, '012': 1}}

    students_id_occurrences(['002', '003', '001', '012', '003', '001']) 
    returns {'002': 1, '003': 2, '001': 2, '012': 1}
    """
    d = {}
    for id in ids:
        if id in d:
            d[id] += 1
        else:
            d[id] = 1
    return d


# Your unit tests

assert students_id_occurrences(['002', '003', '001', '004', '012'])  ==  {'003': 1, '002': 1, '001': 1, '004': 1, '012': 1}
assert students_id_occurrences(['002', '003', '001', '012', '003', '001']) == {'002': 1, '003': 2, '001': 2, '012': 1}

r"""
Exercise 5

Complete the following function to count 
the frequency of words in a given paragraph.

E.g.,
word_frequency("I am alive. I am happy.") 
returns {'I': 2, 'am': 2, 'alive': 1, 'happy': 1}

word_frequency("I do not like water. I like fruits.") 
returns {'I': 2, 'do': 1, 'not': 1, 'like': 2, 'water': 1, 'fruits': 1}

Hint: 
import Python's regular expression (pattern used to search for text patterns) module re. 
re.findall(r'\b\w+\b', s) returns list of words from s that matches the pattern of word.
"""
import re
def word_frequency(paragraph):
    """
    Count the frequency of each word in a given paragraph.
    This function returns a dictionary where each key is a word
    and its associated value is the number of times the word
    appears in the paragraph.

    Examples:
        >>> word_frequency("I am alive. I am happy.")
        {'I': 2, 'am': 2, 'alive': 1, 'happy': 1}
    """
    words = re.findall(r'\b\w+\b', paragraph)
    d = {}
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

# Your unit tests
assert word_frequency("I am alive. I am happy.") == {'I': 2, 'am': 2, 'alive': 1, 'happy': 1}
assert word_frequency("I do not like water. I like fruits.") ==  {'I': 2, 'do': 1, 'not': 1, 'like': 2, 'water': 1, 'fruits': 1}








"""
Real-world Coding Question (Optional challenge): Extract Repository IDs and Names from GitHub API Data

The GitHub API allows you to search for repositories using different criteria. 
The following code sends a request to GitHub to find Python repositories with more than 300,000 stars.

The API response is converted into a Python dictionary called response_dict. 
Inside this dictionary, the key "items" contains a list of repository dictionaries,
where each repository includes information such as id, name, stars, and more.
"""


import sys, os
sys.path.append(os.path.expanduser("~/pylibs"))
import requests

url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>350000"
# You can copy and paste the url into your browser to view the data.

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)

# print(f"Status Code: {response.status_code}") 
# HTTP response status code 200 means The server processed the request and returned the requested data successfully.

response_dict = response.json() # Convert the response object to a dictionary
# print(response_dict)

"""
Task: Write a function called id_name_repo_starred_350k(response_dict) that
takes response_dict as its parameter, 
traverses the list stored under the "items" key,
returns a dictionary containing all repository id → name pairs.

Ensure that your function passes the unit test provided below.
"""

# Save the repositories' id: name as a pair in a dict, and print them out.
def id_name_repo_starred_350k(response_dict):
    items = response_dict["items"] # a list of dictionaries
    d = {}
    for item in items:
        d[item["id"]] = item["name"]
    return d


assert id_name_repo_starred_350k(response_dict) == {
    13491895: 'free-programming-books',
    54346799: 'public-apis',
    83222441: 'system-design-primer'
    }


"""
Remember to complete the lab quiz on e-learn. That's all for this lab!
"""
