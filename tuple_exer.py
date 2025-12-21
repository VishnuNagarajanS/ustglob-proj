my_tuple = (10, 20, 30)
print(my_tuple)
# 1 No we cannot modify elements in tuplke. As tuple are immutable we get a error here

#my_tuple[1] = 99   #  Trying to change element at index 1 Error occurs


# 2 Accessing second to last elemnt in tuple
print(my_tuple[-2])

# 3 List and Tuple are both Data structure in python but do have some differences.
# List are mutable while tuple are immutable
# we initialize list with [] and tuple with ()
# list has values of same or different data type but tuple have only values of same data type


# 3 Changing value of tuple by list conversion
t = (1, 2, 3, 4)
temp_list = list(t)
temp_list[2] = 100
t = tuple(temp_list)
print(t)

# sum of tuple values

summ=sum(t)
print("the sum is  : ",summ)


 


