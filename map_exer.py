# 1 square a list
sqr_list=[1,2,3,4,5,6]
sqr=list(map(lambda x: x**2, sqr_list))
print(sqr)


# 2 op of the code
from functools import reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(result)
# op : 24


# 3 upper case
words = ["apple", "banana", "cherry"]
uppercase = list(map(str.upper, words))
print(uppercased)


# 4 to find gcd using reduce
from functools import reduce
import math

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

nums = [48, 64, 80]
print(gcd_list(nums))


# 5 comparison of map and filter
# Transforms each element	                                Selects elements based on condition
# Function returns a new value                           	Function returns True/False
# Same length as input (unless transformed to same value)	Subset of original elements
# map(lambda x: x**2, [1,2,3]) → [1,4,9]	                filter(lambda x: x%2==0, [1,2,3,4]) → [2,4]


