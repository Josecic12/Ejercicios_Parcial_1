def calcular_agua_por_organismo(agua_inicial, organismos_iniciales, generaciones):
    
    agua_actual = agua_inicial
    organismos_actuales = organismos_iniciales
    
   
    for _ in range(generaciones):
        organismos_actuales *= 2
    
   
    agua_por_organismo = agua_actual / organismos_actuales
    
    return agua_por_organismo

while True:
    
    agua_inicial = float(input("Introduce la cantidad inicial de agua: "))
    organismos_iniciales = int(input("Introduce el número inicial de organismos: "))
    generaciones = int(input("Introduce el número de generaciones (entre 0 y 50): "))
    
    
    if generaciones < 0 or generaciones > 50:
        print("Error: El número de generaciones debe estar entre 0 y 50. Por favor, intenta de nuevo.")
    else:
        
        agua_final = calcular_agua_por_organismo(agua_inicial, organismos_iniciales, generaciones)
        
        print(f"Cantidad de agua por organismo en la generación {generaciones}: {agua_final}")
        break