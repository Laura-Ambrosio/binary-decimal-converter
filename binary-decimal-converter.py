# Number Conversion
# -----------------
# Develop a program that converts decimal numbers to binary and from binary to decimal.
# Extension: Validate input and show error messages for incorrect data.

# Display the menu
print("\nNumber Conversion")
print("-----------------")
print("\n1. Convert from binary to decimal.")
print("2. Convert from decimal to binary.\n")

# Ask the user to choose an option from the menu
opcion = input("Enter one of the options above: ")

# If the user enters something other than option 1 or 2, ask again
while opcion != "1" and opcion != "2":
    opcion = input("You must enter option 1 or 2. Try again: ")

# Constants for base systems
BASE_BINARIO = 2
BASE_DECIMAL = 10

# Initialize variables
num_decimal = 0
num_binario = ""

# Option 1: Binary to Decimal
if(opcion == '1'):

    # Ask for the sign bit and the binary number
    signo = input("Enter the sign bit of the binary number (0 for positive, 1 for negative): ")

    while signo != "0" and signo != "1":
        signo = input("\nInvalid sign bit. Please enter 0 (for positive) or 1 (for negative): ")

    # Loop until valid binary input is received
    while True:
        valido = True
        num = input("\nEnter the binary number: ")

        if num == "":
            valido = False

        for letra in num:
            if letra != "0" and letra != "1":
                valido = False
                print("Input must be a binary number. Try again: ")
                break

        if valido:
            break

    # Convert binary to decimal
    i = len(num) - 1
    for digito in num:
        if digito == '1':
            num_decimal += (BASE_BINARIO ** i)
        i -= 1

    # Show result with sign bit
    if signo == '0':
        print(f"\n{signo}{num}(2) corresponds to {num_decimal}(10)")
    elif signo == '1':
        print(f"\n{signo}{num}(2) corresponds to -{num_decimal}(10)")

# Option 2: Decimal to Binary
elif (opcion == '2'):

    num = input("Enter the decimal number: ")

    while not num.lstrip("+-").isdigit():
        num = input("Enter the decimal number: ")

    signo = ""

    for digito in num:
        if digito == '-' or digito == '+':
            signo = digito

    num = int(num.lstrip("+-"))
    dividendo = num

    while dividendo != 0:
        resto = dividendo % 2
        dividendo = dividendo // 2
        num_binario = num_binario + str(resto)

    binario_invertido = num_binario[::-1]
  
# If the sign is +, the binary value will be printed with an additional 0 on the left indicating that it is positive, and if it is -, the same, but a 1 will be added on the left.
    
    if signo == '-':
        bitSigno = 1
        print(f"\nThe number {num} in binary is {bitSigno}{binario_invertido}")
        print("When the entered decimal number is negative, a sign bit of 1 is added to the left of the translated binary number.")
    else:
        bitSigno = 0
        print(f"\nThe number {num} in binary is {bitSigno}{binario_invertido}")
        print("When the entered decimal number is positive, a sign bit of 0 is added to the left of the translated binary number.")


       
