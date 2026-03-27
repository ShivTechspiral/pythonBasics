#!/usr/bin/env python3
try:
    verifyNumber = int(input())
    if verifyNumber == 0:
        print ("this number is equel to zero")
    else:
        print ("this number is different from zero")
    
except Exception as e:
    print( "An unexpected error occured - Check the input!\n", e)