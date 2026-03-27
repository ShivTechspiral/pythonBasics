import sys

try:
    if len(sys.argv) == 2:
        validate = input("What was the prameter? ")
        if str(sys.argv[1]) == str(validate):
            print("Good job!")

        else:
            print( "Nope, sorry...")
    else:
        print("none")
except Exception as e:
    print (e)
