password = "Python is awesome"
try:
    checkpass = input()
    if checkpass == password:
        print ("ACCESS GRANTED")

    else:
        print ("ACCESS DENIED")
       
except Exception as e:
    print("something didn't go well! \n", e)
