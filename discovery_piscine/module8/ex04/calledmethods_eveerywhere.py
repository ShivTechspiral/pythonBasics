import sys
def shrink(param):
    print(param[0:7])
def enlarge(param):
    i = len(param)
    j = 8-i
    part = str('z'*j)
    print(f' {param}{part}' )

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        if len(i) > 8:
            shrink(i)
        else:
            enlarge(i)
