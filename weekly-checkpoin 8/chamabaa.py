def main():
    print("Binary to Decimal Converter")
    print("This program converts binary numbers into decimal numbers.\n")
    
    while True:
        binary_input = input("Enter a binary number (or type 'exit' to quit): ").strip()
        
        if binary_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        if not all(char in '01' for char in binary_input):
            print("Invalid input! Please enter only 0s and 1s.\n")
            continue
            
        decimal_result = binary_to_decimal(binary_input)
        print(f"Decimal number: {decimal_result}\n")

def binary_to_decimal(binary_str):
    valores = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    
    binario = []
    for caracter in binary_str:
        binario.append(int(caracter))
        
    total = 0
    for i in range(len(binario)):
        if binario[i] == 1 and i < len(valores):
            total = total + valores[i]
            
    return total

if __name__ == "__main__":
    main()
