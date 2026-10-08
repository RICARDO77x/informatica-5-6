def main():
    print("--- Conversor de Binario a Decimal ---")
    
    valores = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    
    binary_input = input("Introduce tu número binario: ")
    
    binario = []
    for caracter in binary_input:
        binario.append(int(caracter))
    
    decimal_resultado = convertir_con_lista(binario, valores)
    
    print(f"El número decimal resultante es: {decimal_resultado}")

def convertir_con_lista(binario, valores):
    total = 0
    
    for i in range(len(binario)):
        if binario[i] == 1:
            total = total + valores[i]
            
    return total

if __name__ == "__main__":
    main()
