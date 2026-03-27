import sys

def downcase_it(value):
    print(value.lower())

if len(sys.argv) >1:
    for i in sys.argv:
        if i != sys.argv[0]:
            downcase_it(i)
else:
    print("none")

