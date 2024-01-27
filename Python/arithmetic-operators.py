a = int(input())
b = int(input())

try:
    add = a + b
    diff = a - b
    prod = a * b
    rem = a % b
    print("Addition:", add)
    print("Subtraction:", diff)
    print("Multiplication:", prod)
    div = a // b
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division:", div)

#added try-except for efficient output

