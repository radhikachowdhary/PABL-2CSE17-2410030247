def factorial_digits(n):
    res = 1
    
    for i in range(2, n + 1):
        res *= i
    
    digits = [int(digit) for digit in str(res)]
    
    return digits

num = 6
result = factorial_digits(num)

print(f"The factorial of {num} is 720")
print(f"The digits are: {result}")
