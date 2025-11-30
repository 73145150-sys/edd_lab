def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    
    # Caso recursivo
    return n * factorial(n - 1)


# Programa interactivo
while True:
    print("\n--- CÁLCULO DE FACTORIAL ---")
    numero = int(input("Ingresa un número (o -1 para salir): "))

    if numero == -1:
        print("Programa finalizado.")
        break

    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        print(f"El factorial de {numero} es: {factorial(numero)}")
