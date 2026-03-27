def greetings(name="nobel starager"):
    if not isinstance(name, str):
        print("Error! it was not a name")
    else:
        print(f'Hello {name}')
        
            

    
greetings("Shiv Shivam")
greetings("Shiva")
greetings()
greetings({'K': 7474564, 'i': 767})