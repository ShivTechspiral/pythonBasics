def Calculate (num1, num2):
    print (f"{ num1 } + { num2 } = { num2 + num1 } \n{ num1 } - { num2 } = { num2 - num1 } \n{ num1 } / { num2 } = { num2 / num1 } \n{ num1 } * { num2 } = { num2 * num1 } \n ")

out_param1 = int(input("give me the first number: " ))
out_param2 = int(input("give me the Second number: " ))

Calculate(out_param1, out_param2)