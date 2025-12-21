# 1 adding a new key value pair in a existing dictionary
student = {"name": "Vishnuu", "age": 22}
student["grade"] = "A"
print(student)

# 2 accessing a non existant key
student = {"name": "John", "age": 20}
# print(student["marks"])   #  this produces a KeyError


# 3 a function to return keys of values greater that 50
def keys_greater_than_50(d):
    return [key for key, value in d.items() if value > 50]
scores = {"math": 40, "science": 75, "english": 60}
print(keys_greater_than_50(scores))

# 4 to iterate over both keys and values
student = {"name": "John", "age": 20, "grade": "A"}
for key, value in student.items():
    print(key, ":", value)

# 5 function to merge two dictionary
def merge_dicts(d1, d2):
    merged = d1.copy()   
    merged.update(d2)    
    return merged
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))



