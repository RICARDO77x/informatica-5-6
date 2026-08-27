def main():
    # 1. Pedir la capa y pasarla a minúsculas
    layer = input("Enter the atmospheric layer: ").lower()
    
    # 2. Revisar cuál capa eligió y mostrar su rango de altitud
    if layer == "exosphere":
        print("Altitude range: 700 - 10000 km")
    elif layer == "thermosphere":
        print("Altitude range: 85 - 700 km")
    elif layer == "mesosphere":
        print("Altitude range: 50 - 85 km")
    elif layer == "stratosphere":
        print("Altitude range: 12 - 50 km")
    elif layer == "troposphere":
        print("Altitude range: 0 - 12 km")
    else:
        print("Invalid layer")
        return

    # 3. Pedir la altitud inicial
    altitude = float(input("Enter starting altitude in km: "))
    total_time = 0

    # 4. Calcular tiempo capa por capa desde arriba hacia abajo

    # Exósfera (700 a 10,000 km) - Velocidad: 2000 m/s
    if altitude > 700:
        km_in_layer = altitude - 700
        altitude = 700 # Bajamos el objeto a 700 km
        total_time += (km_in_layer * 1000) / 2000

    # Termósfera (85 a 700 km) - Velocidad: 500 m/s
    if altitude > 85:
        km_in_layer = altitude - 85
        altitude = 85 # Bajamos el objeto a 85 km
        total_time += (km_in_layer * 1000) / 500

    # Mesósfera (50 a 85 km) - Velocidad: 200 m/s
    if altitude > 50:
        km_in_layer = altitude - 50
        altitude = 50 # Bajamos el objeto a 50 km
        total_time += (km_in_layer * 1000) / 200

    # Estratósfera (12 a 50 km) - Velocidad: 75 m/s
    if altitude > 12:
        km_in_layer = altitude - 12
        altitude = 12 # Bajamos el objeto a 12 km
        total_time += (km_in_layer * 1000) / 75

    # Troposfera (0 a 12 km) - Velocidad: 20 m/s
    if altitude > 0:
        km_in_layer = altitude - 0
        total_time += (km_in_layer * 1000) / 20

    # 5. Imprimir el resultado final redondeado a 1 decimal
    print(f"Total descent time: {round(total_time, 1)}s")

if __name__ == "__main__":
    main()
