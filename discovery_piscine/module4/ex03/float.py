try:
    input_num = (input ("give me the number: "))
    

    if '.' in input_num:
        parts = str(input_num).split(".")

        integer_part = parts[0]
        decimal_part = parts[1]

        if  decimal_part == '0':
            print(f"this number is a Integer.")
        else:
            print(f"this number is a Decimal.")

    else:
        print(f"this number is a Integer.")

except Exception as e:
    print(e)