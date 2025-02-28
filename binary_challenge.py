import re

def is_valid_binary(binary):
    """Check if a string is a valid binary number (supports floating points and negatives)."""
    return bool(re.fullmatch(r"-?[01]+(\.[01]+)?", binary))

def decimal_to_binary(n):
    """Convert decimal to binary (handles integers and floating points)."""
    if isinstance(n, int):  # Integer case
        return bin(n)[2:] if n >= 0 else "-" + bin(abs(n))[2:]

    # Floating-point case
    integer_part = int(n)
    fractional_part = abs(n - integer_part)  # Handle negatives properly
    binary_integer = bin(abs(integer_part))[2:]

    # Convert fractional part
    binary_fraction = ""
    while fractional_part and len(binary_fraction) < 10:  # Limit precision
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fraction += str(bit)
        fractional_part -= bit

    binary_result = binary_integer + ("." + binary_fraction if binary_fraction else "")
    return binary_result if n >= 0 else "-" + binary_result

def binary_to_decimal(binary):
    """Convert binary to decimal (supports integer and floating point)."""
    if not is_valid_binary(binary):
        raise ValueError("Invalid binary number format.")

    negative = binary.startswith("-")
    if negative:
        binary = binary[1:]

    if "." in binary:
        integer_part, fractional_part = binary.split(".")
        decimal_integer = int(integer_part, 2)
        decimal_fraction = sum(int(bit) * (1 / (2 ** (i + 1))) for i, bit in enumerate(fractional_part))
        result = decimal_integer + decimal_fraction
    else:
        result = int(binary, 2)

    return -result if negative else result

def binary_calculator():
    print("Binary Calculator with Error Handling")
    print("Operations: + (Add), - (Subtract), * (Multiply), / (Divide), & (AND), | (OR), ^ (XOR), ~ (NOT)")

    # Get user input
    bin1 = input("Enter first binary number: ").strip()
    if not is_valid_binary(bin1):
        print("Error: Invalid binary number format.")
        return

    operator = input("Enter operation (+, -, *, /, &, |, ^, ~): ").strip()
    if operator not in {"+", "-", "*", "/", "&", "|", "^", "~"}:
        print("Error: Invalid operator.")
        return

    if operator != "~":
        bin2 = input("Enter second binary number: ").strip()
        if not is_valid_binary(bin2):
            print("Error: Invalid binary number format.")
            return

    try:
        # Convert binary to decimal
        num1 = binary_to_decimal(bin1)
        num2 = binary_to_decimal(bin2) if operator != "~" else None

        # Perform calculation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        elif operator == '&':
            result = int(num1) & int(num2)
        elif operator == '|':
            result = int(num1) | int(num2)
        elif operator == '^':
            result = int(num1) ^ int(num2)
        elif operator == '~':
            result = ~int(num1)
        else:
            print("Error: Unsupported operation.")
            return

        # Convert result back to binary
        binary_result = decimal_to_binary(result)
        print(f"Result in Binary: {binary_result}")

    except ValueError as e:
        print(f"Error: {e}")

# Run the binary calculator
binary_calculator()
