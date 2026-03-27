import sys

try:
    if len(sys.argv) == 2:
        z_find = sys.argv[1].count("z")
        if z_find == 0:
            print( "none" ) 
        else: 
            while z_find > 0:
                print ("z", end="")
                z_find -= 1 
    else:
        print("none")
except Exception as e:
    print(e)

