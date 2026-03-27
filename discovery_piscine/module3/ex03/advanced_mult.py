try:
    number = 0
    flag = 0
    while number <= 10:
        print(f"\n Table of {number}:",  end="  ")
        while flag <= 10:
            print(f"{flag * number}", end=" ")
            flag += 1
        number += 1
        flag = 0

except Exception as e:
    print ( " Something wrong!", e)

