
def calculate_power(base, power):
    return base ** power


if __name__ == "__main__":
    
       
        base = float(input("Enter the base number: "))
        power = float(input("Enter the power (n): "))

       
        result = calculate_power(base, power)
        print(f"{base} raised to the power of {power} is {result}")
    