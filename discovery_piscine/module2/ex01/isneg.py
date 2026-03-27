#!/usr/bin/env python3
try:
    verifyNumber = int(input())
    if verifyNumber == 0:
        print ("this number is both positive and negative.")
    elif verifyNumber > 0:
        print ("this number is positive")
    else:
        print( "The number is negative")
    
except Exception as e:
    print( "An unexpected error occured - Check the input Number!\n", e)