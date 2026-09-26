"""
When comparing the efficiency of an algorithm, we often consider its
time complexity and space complexity, usually focusing on the worst-case scenario.

Time complexity is a function that describes 
how long an algorithm takes in terms of the input size.

Space complexity is a function that describes 
how much memory (space) an algorithm requires to the input size.

Big O notation represents the “order of magnitude” of a function's growth 
as the input size becomes large.
It shows how the running time or space of an algorithm grows relative to the input size n,
ignoring constant factors and lower-order terms. 
E.g., if an algorithm takes f(n) = 3n^2 + 5n + 10 steps, its time complexity big O is O(n^2). 
We ignore lower-order terms 5n + 10, because for large n, the n^2 term dominates. 
We also ignore the constant coefficient 3, leaving the Big O as O(n²).

Assuming the quantity of input is n,
Common time complexities: O(1), O(log n), O(n), O(nlog n), O(n^2), O(2^n), etc.
Common space complexities: O(1), O(n), O(n^2), etc.
"""

#### Constant Time O(1): 
# O(1) means the running time does not depend on the input size.
def sum_nums(a, b):
    return a + b

assert sum_nums(4, 5) == 9
assert sum_nums(0, -1) == -1


def first_item(nums): 
    """Return the first item of a list, or None if the list is empty."""
    if not nums: # if (len(nums) == 0):
        return None
    return nums[0]

assert(first_item([3, 2, 4]) == 3)
assert(first_item([]) == None)


#### Logarithmic time O(logn)
# O(logn) - Highly efficient!

def binary_search(nums, target):
    '''Perform binary search on a sorted list to find the index of a target value.'''
    left = 0  # First index
    right = len(nums) - 1  # Last index
    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    return -1

assert binary_search([1, 5, 8, 10], 8) == 2
assert binary_search([1, 5, 8, 10], 4) == -1


#### Linear Time O(n):
# The running time grows at a linear function of n (proportional to n), where n is the size of input nums

def sum_all_items(nums):
    total = 0
    for num in nums:
        total += num
    return total

assert sum_all_items([3, 2, 4]) == 9
assert sum_all_items([3]) == 3 
assert sum_all_items([]) == 0



def create_list(n):
    a_list = []
    for i in range(n):
        a_list.append(i)
    return a_list
assert create_list(3) == [0, 1, 2]
assert create_list(1) == [0]



def linear_search(nums, target):
    nums_length = len(nums)
    for i in range(nums_length):
        if nums[i] == target:
            return i
    return -1
assert linear_search([1, 5, 8, 10], 8) == 2
assert linear_search([1, 5, 8, 10], 4) == -1


#### Quadratic Time O(n^2):
# The running time grows at a quadratic function of n, where n is the size of input nums

def create_matrix(n):
    a_matrix = []
    for i in range(n):
        a_matrix.append([])
        for j in range(n):
            a_matrix[i].append(j)
    return a_matrix

assert create_matrix(2) == [[0, 1], [0, 1]]
assert create_matrix(1) == [[0]]
assert create_matrix(0) == []






#### Space complexity ####


# Constant Space O(1)
def sum(a, b):  # Assume nums is not empty
    result = a + b
    return result



# Linear Space O(n)
def create_list_space(n):  # Or create a set, dictionary
    a_list = []
    for i in range(n):
        a_list.append(i)
    return a_list


assert create_list_space(4) == [0, 1, 2, 3]


# Quadratic Space O(n^2):
def create_matrix_space(n):
    a_matrix = []
    for i in range(n):
        a_matrix.append([])
        for j in range(n):
            a_matrix[i].append(j)
    return a_matrix


assert create_matrix_space(3) == [[0, 1, 2], [0, 1, 2], [0, 1, 2]]




"""
Now let's analyze some classical algorithms together!
"""


### Factorial iterative implementations
def factorial(n):  # Time: O(n), Space: O(1)
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res



### Finonacci iterative implementations

def my_fib(n):  # Time: O(n), Space: O(n)
    """
    Return a list containing the first n Fibonacci numbers.

    E.g.,
    If n = 1, return [0]
    If n = 2, return [0, 1]
    If n = 3, return [0, 1, 1]
    If n = 4, return [0, 1, 1, 2]
    """
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        res = [0, 1]
        for i in range(2, n):
            res.append(res[-1] + res[-2])
            #res.append(res[i - 1] + res[i - 2])
        return res


assert my_fib(1) == [0]
assert my_fib(2) == [0, 1]
assert my_fib(5) == [0, 1, 1, 2, 3]
assert my_fib(7) == [0, 1, 1, 2, 3, 5, 8]




### Search algorithms

# Compared to linear search and binary search algorithms
def search_dict(nums, target):  # T: O(n), S: O(n)
    nums_length = len(nums)
    dict = {}
    for i in range(nums_length):
        dict[nums[i]] = i
    if target in dict:
        return dict[target]
    else:
        return -1
