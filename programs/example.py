# <QUESTION 1>

# Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

# <EXAMPLES>

# endsPy("ilovepy") → True
# endsPy("welovepy") → True
# endsPy("welovepyforreal") → False
# endsPy("pyiscool") → False

# <HINT>

# What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
    
def endsPy(input):
    lower_case = input.lower()
    if lower_case.endswith("py"):
        return True
    else: 
        return False

    
# <QUESTION 2>

# Given a list of items, return a dictionary mapping items to the amount
# of times they appear in the list

# Note: the order of this dictionary does not matter

# <EXAMPLES>

# one(['apple', 'banana', 'orange', 'orange', 'apple', 'apple']) → {'apple':3, 'orange':2, 'banana':1}
# one(['tic', 'tac', 'toe']) → {'tic':1, 'tac':1, 'toe':1}
    
def one(items):
    empty_dictionary = {}
    for item in items: 
        print(item)
        empty_dictionary[item] = items.count(item)
        print(empty_dictionary)
    return empty_dictionary


# <QUESTION 3>

# Given two numbers, a & b, and an operator, evaluate the operation between a & b
# using the given operator

# The operator will be a string, and will only be +, -, *, or /. 

# <EXAMPLES>

# two(2, 4, '+') → 6
# two(7, 3, '-') → 4
# two(3, 1.5, '*') → 4.5
# two(-5, 2, '/') → -2.5

def two(a, b, operator):
    if operator == "+":
        return a + b 
    elif operator == "-":
        return a - b
    elif operator == "/":
        return a / b
    elif operator == "*":
        return a * b

# <QUESTION 4>

# Given a positive integer, return the next integer below it that has an
# integer square root (is the square of another integer)

# If the number has a square root, just return the number

# <EXAMPLES>

# three(7) → 4          # 4 is the square of 2
# three(64) → 64        # 64 is the square of 8 already
# three(32) → 25

# <HINT>

# We can use `x ** 0.5` to get the square root of `x`

def three(num):
    y = 0
    while num > 0: 
        x = num ** 0.5 
        if x - int(x) == 0: 
            y = num
            break
        num -= 1
    return y

# <QUESTION 5>

# Given two integers, return the greatest common factor of the two numbers

# <EXAMPLES>

# four(32, 24) → 8
# four(18, 11) → 1
# four(10, 50) → 10

def four(a, b):
    pass

# <QUESTION 6>

# Given a string, return a string where each letter is the previous letter in the alphabet
# in comparison to the original string

# For a or A, use z or Z respectively

# Ignore characters that aren't in the alphabet, such as whitespace or numbers

# <EXAMPLES>

# five('wxyz') → 'vwxy'
# five('abc') → 'zab'
# five('aAbB') → 'zZaA'
# five('hello world') → 'gdkkn vnqkc'
# five('54321') → '54321'

def five(string):
    pass
