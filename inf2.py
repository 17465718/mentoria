def EsMultiplo(a, b):
    if b == 0:  
        return False
    return a % b == 0

def main():
    try:
        num1 = int(input("Introduce el primer número entero: "))
        num2 = int(input("Introduce el segundo número entero: "))
        
        if EsMultiplo(num1, num2):
            print(f"{num1} es múltiplo de {num2}.")
        elif EsMultiplo(num2, num1):
            print(f"{num2} es múltiplo de {num1}.")
        else:
            print("Ninguno de los números es múltiplo del otro.")
    except ValueError:
        print("Por favor, introduce números enteros válidos.")

if __name__ == "__main__":
    main()
