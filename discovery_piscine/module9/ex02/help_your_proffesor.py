def average(my_class):
    num_list = []
    sum = 0
    for key, value in my_class.items():
        num_list.append(value)
    count = len(num_list)
    for i in num_list:
        sum += i
    avg = sum/count
    return avg
    


class_3B = {
    "sam": 66,
    "danial": 33,
    "victor": 88,
    "petr": 45
}

class_3C = {
    "danial": 33,
    "victor": 88,
    "vijay": 90,
    "raj": 98,
    "Selva": 0
}

print(f"Average for the class 3B: {average(class_3B)}")
print(f"Average for the class 3B: {average(class_3C)}")