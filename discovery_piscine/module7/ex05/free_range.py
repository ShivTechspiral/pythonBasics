#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    first_num  = int(sys.argv[1])
    second_num = int(sys.argv[2])

    if first_num >= second_num:
        print("none")
    else:
        array = []
        a1 = []
        a1 = list(range(first_num, second_num))
        

        print(a1)
        flag  = first_num

        while flag <= second_num:
            array.append(flag)
            flag += 1

        print(array)