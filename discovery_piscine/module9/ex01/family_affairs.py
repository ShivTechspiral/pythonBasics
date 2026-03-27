def find_the_redheads(fam_name):
    new_list = []
    for key, value in fam_name.items():
        if value == "red":
            new_list.append(key)
    return new_list


dupond_family = {
    "sam": "red",
    "ellie": "blond",
    "mike":  "black",
    "sristi": "brown",
    "jim": "red"
}

print(find_the_redheads(dupond_family))