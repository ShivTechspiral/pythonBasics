try:
    print("enter a number less than 25")
    loop_number = int(input())
    if loop_number > 0 and loop_number < 25:
        while loop_number <= 25:
            print(f"Inside the loop, my variable is {loop_number}")
            loop_number += 1
    else:
        print("Error")
        
except Exception as e:
    print("something went wrong!!", e)
