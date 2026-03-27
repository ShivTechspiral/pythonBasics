import sys

try:
    if len(sys.argv) > 1:
        print(f" parameters: {len(sys.argv) - 1}")
        for values in sys.argv:
            if values != sys.argv[0]:
                i = len(str(values))
                print(f" {values}: {i}")
            
    else:
        print("none")
except Exception as e:
    print (e)
