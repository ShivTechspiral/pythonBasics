#!/usr/bin/env python3

def famous_births(persons):
    if not isinstance(persons, dict):
        print("Error: Parameter must be a dictionary!")
        return

    # sort by date_of_birth
    sorted_persons = sorted(persons.items(), key=lambda x: x[1]["date_of_birth"])

    for key, person in sorted_persons:
        print(f"{person['name']} was born on {person['date_of_birth']}")


# dictionary of historical figures
women_scientist = {
    "ada": {
        "name"          : "ada Newton",
        "date_of_birth" : "1643-01-04"
    },
    "cecilia": {
        "name"          : "cecilia Einstein",
        "date_of_birth" : "1879-03-14"
    },
    "lisa": {
        "name"          : "lisa da Vinci",
        "date_of_birth" : "1452-04-15"
    },
    "grace": {
        "name"          : "grace Tesla",
        "date_of_birth" : "1856-07-10"
    }   
}

famous_births(women_scientist)