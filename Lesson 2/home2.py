dict1 = {}
lst = []

dict1["key1"] = "value1"
# dict1 = dict([
    # (1, 1),
    # (2, 4),
    # (3, 9),
    # "sa",
# ])
# dict1 = dict([
            #  (1, 2),
            #  "ke",
# ])

dict1[("some", "tupl")] = ["some", "lst"]
dict1[1] = 2
dict1[33] = "abc"

print(dict1)
print(dict1["key1"])
del dict1["key1"]

for key in dict1:
    lst.append(key)


print(dict1)
print(lst)
