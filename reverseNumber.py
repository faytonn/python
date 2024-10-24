import sys

def convert_to_decimal(number, base):
    """
    Convert a number from a given base to decimal (base 10).
    """
    decimal_value = 0
    for digit in number:
        # Determine the numeric value of the current digit/character
        if digit.isdigit():
            # If it's a digit (0-9), convert it directly to an integer
            value = int(digit)
        else:
            # If it's a letter (a-z), convert it to an integer (10-35)
            value = ord(digit) - ord('a') + 10
        
        # Update the decimal value by multiplying the current value and adding the new digit
        decimal_value = decimal_value * base + value
    
    return decimal_value

def convert_from_decimal(number, base):
    """
    Convert a decimal (base 10) number to a given base.
    """
    if number == 0:
        return '0'
    
    digits = []
    while number > 0:
        remainder = number % base
        if remainder < 10:
            # For remainders 0-9, convert directly to string
            digits.append(str(remainder))
        else:
            # For remainders 10-35, convert to corresponding letter (a-z)
            digits.append(chr(ord('a') + remainder - 10))
        
        number //= base  # Reduce the number for the next iteration
    
    return ''.join(reversed(digits))

def main():
    current_conversion = None  # This will keep track of the current conversion settings
    for line in sys.stdin:
        line = line.strip()  # Remove any trailing newline characters
        
        if '>' in line:
            # If the line contains '>', it's a conversion definition
            initial_base, final_base = map(int, line.split('>'))
            current_conversion = (initial_base, final_base)  # Update the current conversion
        else:
            # Otherwise, it's a number to convert
            number = line
            if current_conversion is not None:
                initial_base, final_base = current_conversion
                # Convert the number to decimal
                decimal_value = convert_to_decimal(number, initial_base)
                # Convert the decimal number to the final base
                converted_value = convert_from_decimal(decimal_value, final_base)
                print(converted_value)  # Output the converted value

if __name__ == "__main__":
    main()