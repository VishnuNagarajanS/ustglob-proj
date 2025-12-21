lst = [1, 2, 3, 4, 5]
lst.append(6)  # 1 appended a number
print("appended list  : ",lst)
lst.pop(3) # 2 removed number at index 3
print("removed by index list  :",lst)
lst[1:3] = [10, 20]
print("sliced list  : ",lst) # 3 list slicing

# 4 checked if an element exist in list
num=int(input("enter the number to be checked  :"))
if num in lst:
    print("exist")
else:
    print("not exists")

# 5 set function used to check duplicates
listt=[1,1,2,2,2,3,3,4,5,5]
print("The list with duplicate values", listt)
sett=set(listt)
print("the list without duplicats", sett)
    


