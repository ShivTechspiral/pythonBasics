try:
    first_num = int (input())
    second_num = int(input())
    multiply = first_num*second_num
    print( f"{first_num} * {second_num}  = {multiply}")
    if multiply > 0:
            print("the number is positive")
    elif multiply == 0:
            print("the number is positive and negative")
    else:
            print("the number is negative")
except Exception as e:
     print("something went wrong!!", e)
