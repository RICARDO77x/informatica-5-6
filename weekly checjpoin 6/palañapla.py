def main():
    print("--- Binary to Decimal Converter ---")
    
    valores = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    
    while True:
        binary_input = input("\nEnter your binary number (or type 'exit' to quit): ")
        
        if binary_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        binario = []
        for caracter in binary_input:
            binario.append(int(caracter))
        
        decimal_resultado = convertir_con_lista(binario, valores)
        
        print(f"The resulting decimal number is: {decimal_resultado}")

def convertir_con_lista(binario, valores):
    total = 0
    
    for i in range(len(binario)):
        if binario[i] == 1:
            total = total + valores[i]
            
    return total

if __name__ == "__main__":
    main()
