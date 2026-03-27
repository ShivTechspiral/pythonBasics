my_ary = [4, 6, 6, 88, -22, -8, 787, 97875, -8]
new_ary =[]
print(my_ary)
for index, obj in enumerate(my_ary):
    if obj > 5:
        new_ary.append(obj + 2)
    #print(obj)
unique_ary = list(set(new_ary))
print(new_ary)
#print(unique_ary) 