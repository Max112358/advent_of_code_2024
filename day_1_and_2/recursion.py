def calculate_fib(number1):
    if number1 == 0:
        return 0
    if number1 == 1:
        return 1
    return calculate_fib(number1 - 1) + calculate_fib(number1 - 2)
result = calculate_fib(50)
print(result)