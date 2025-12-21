# 1 removing all elements in a set but clear function
sett={1,2,3,4,5,6}
sett.clear()
print(sett) # producec empty set

# 2 checking op of the code snippet
a={1,2,3,4}
b={3,4,5,6}
print(a-b)  # op is {1,2}

# 3 checking if an element present in the set
settt={1,2,3,4,5,6}
num=int(input("Enter a num to check  : "))
if num in settt:
    print("num exists")
else:
    print("num not exist")


# 4 program to find intersection of 2 sets
set1={1,2,3,4,5,6}
set2={3,4,5,6,7}
inter=(set1&set2)
print(set1,set2)
print("the intersection is  : ", inter)


# 5 set handling duplicate values
numbers = {1, 2, 3}
numbers.add(2)
numbers.add(3)
numbers.add(4)

print(numbers) # here op is {1,2,3,4}

# Sets are implemented using hash tables.

# Each element must have a unique hash.

# If the hash already exists, Python won’t insert the duplicate.
