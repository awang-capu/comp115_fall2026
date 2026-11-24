"""
Introduction to Recursion in Python

Recursion is when a function calls itself to solve a smaller version of a problem.
It is often elegant for problems that can be divided into similar subproblems, 
but each recursive call uses the call stack, which can cost additional memory.

All recursive algorithms must obey three important laws:

1. A recursive algorithm must have a base case.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.
"""
def sum_iterative(n):
    """
    Returns the sum of integers from 1 to n.
    """
    total = 0
    for i in range(n + 1):
        total += i
    return total

def sum_recursive(n):
    if (n == 1):
        return 1
    return n + sum_recursive(n - 1)

assert sum_iterative(1) == 1
assert sum_iterative(3) == 6
assert sum_iterative(10) == 55
assert sum_iterative(100) == 5050

assert sum_recursive(1) == 1
assert sum_recursive(3) == 6
assert sum_recursive(10) == 55
assert sum_recursive(100) == 5050


# Iterative version of Fibonacci sequence
def my_fib_iterative(n):
    """
    Returns the first n Fibonacci numbers using an iterative approach.
    """
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    res = [0, 1]
    for i in range(2, n):
        res.append(res[-1] + res[-2])
    return res

assert my_fib_iterative(1) == [0]
assert my_fib_iterative(2) == [0, 1]
assert my_fib_iterative(5) == [0, 1, 1, 2, 3]
assert my_fib_iterative(7) == [0, 1, 1, 2, 3, 5, 8]


# Recursive version of Fibonacci sequence
def my_fib_recursive(n):
    """
    Returns the first n Fibonacci numbers using a recursive approach.
    """
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibs = my_fib_recursive(n - 1)
        fibs.append(fibs[-1] + fibs[-2])
        return fibs
    
assert my_fib_recursive(1) == [0]
assert my_fib_recursive(2) == [0, 1]
assert my_fib_recursive(5) == [0, 1, 1, 2, 3]
assert my_fib_recursive(7) == [0, 1, 1, 2, 3, 5, 8]


def binary_search(nums, target):  # T: O(log n), S: O(1)
    """
    Perform binary search on a sorted list to find the index of a target value.
    """
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

def binary_search_recursive(nums, target, left=0, right=None):
    """
    Perform binary search recursively on a sorted list to find the index of a target value.
    Time complexity: O(log n), Space complexity: O(log n) due to recursion stack
    """
    if right is None:
        right = len(nums) - 1

    if left > right: # Base case: if search interval is invalid
        return -1

    mid = (left + right) // 2
    if target < nums[mid]:
        return binary_search_recursive(nums, target, left, mid - 1)
    elif target > nums[mid]:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return mid

# Test both versions
nums = [1, 5, 8, 10]
assert binary_search(nums, 8) == 2
assert binary_search(nums, 4) == -1

assert binary_search_recursive(nums, 8) == 2
assert binary_search_recursive(nums, 4) == -1



# Test and compare iterative and recursive implementations
def test_fibonacci():
    test_cases = [1, 5, 7]
    for n in test_cases:
        iterative_result = my_fib_iterative(n)
        recursive_result = my_fib_recursive(n)
        print(f"n = {n}")
        print(f"Iterative: {iterative_result}")
        print(f"Recursive: {recursive_result}")
        assert iterative_result == recursive_result, "Mismatch between iterative and recursive!"
        print("Both methods match!\n")

if __name__ == "__main__":
    test_fibonacci()
