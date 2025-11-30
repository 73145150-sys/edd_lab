def power(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    
    # Caso recursivo
    return base * power(base, exponente - 1)


# Programa interactivo
continuar = "s"

while continuar.lower() == "s":
    print("\n--- CÁLCULO DE POTENCIA ---")
    
    base = float(input("Ingresa la base: "))
    exponente = int(input("Ingresa el exponente (entero): "))

    # Si el exponente es negativo, avisamos (opcional)
    if exponente < 0:
        print(" Este programa no soporta exponentes negativos con recursión simple.")
    else:
        resultado = power(base, exponente)
        print(f"✔ {base} elevado a {exponente} es: {resultado}")

    #continuar = input("\n¿Deseas calcular otra potencia? (s/n): ")

#print("\nPrograma finalizado.")
