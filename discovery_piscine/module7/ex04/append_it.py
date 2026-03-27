import sys

try:
    ism_find = "ism"
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:        # skip script name
            if ism_find not in arg:     # check if "ism" already exists
                print(f"{arg + ism_find}")
        
            
                
        
    else:
        print("none")
except Exception as e:
    print(e)

