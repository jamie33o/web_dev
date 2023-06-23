import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: not valid value")

#handle zerodivisionerror exception
try:
    result = x/y
except ZeroDivisionError:
    print("Error: can't devide by zero")

print(f"{x} / {y} = {result}")