
def array_of_names(my_array):
    new_array = [f"{key.title()} {value.title()}" for key, value in my_array.items()]
    print(new_array)


persons = {
    "john": "smith",
    "petr": "will",
    "anna": "seth"
}

array_of_names(persons)

#g = "gdfgd"
#print(g.title())
