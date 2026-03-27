try:
    number = int(input())
    flag = 0
    while True:
        print(f"{flag} * {number} =  {flag * number}")
        flag += 1
        if flag >= 10:
            break

except Exception as e:
    print ( " Something wrong!", e)

