print("Simple calculator!")

first_number = input("First number? ")

if first_number.isnumeric() == False:
    print("Please input a number.")
    exit()

operation = input("Operation? ")

second_number = input("Second number? ")

if second_number.isnumeric() == False:
    print("Please input a number.")
    exit()

second_number = int(second_number)

result = 0
first_number = int(first_number)
if operation == "+":
    result = first_number + second_number
    label = "sum"
elif operation == "-":
    result = first_number - second_number
    label = "difference"
elif operation == "*":
    result = first_number * second_number
    label = "product"
elif operation == "/":
    result = first_number / second_number
    label = "quotient"
elif operation == "**":
    result = first_number**second_number
    label = "exponent"
elif operation == "%":
    result = first_number % second_number
    label = "modulus"
else:
    print("Operation not recognized.")
    exit()

print(f"{label} of {first_number} {operation} {second_number} equals {result}")
