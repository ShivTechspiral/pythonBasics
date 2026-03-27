#!/usr/bin/env python3

import sys
if len(sys.argv) < 3:
    print("none")
    #print(sys.argv[1])
else:
    for values in reversed(sys.argv):
        if values != sys.argv[0]:
            print(values)