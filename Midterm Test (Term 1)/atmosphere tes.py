def main():
    layer = input("Descent atmosphere layer: ").strip().lower()
    if layer == "exosphere":
        print("Altitude between 700 and 10,000 km.")
    elif layer == "thermosphere":
        print("Altitude between 85 and 700 km.")
    elif layer == "mesosphere":
        print("Altitude between 50 and 85 km.")
    elif layer == "statosphere":  # Nota: en tu código original dice "statosphere" en lugar de "stratosphere"
        print("Altitude between 12 and 50 km.")
    elif layer == "troposphere":
        print("Altitude between 0 and 12 km.")
    else:
        print("Invalid layer.")

    altitude = float(input("Exact altitude: "))
    time = 0

    if altitude > 700:
        time += (altitude - 700) / 2
        altitude = 700

    if altitude > 85:
        time += (altitude - 85) / 0.5
        altitude = 85

    if altitude > 50:
        time += (altitude - 50) / 0.2
        altitude = 50

    if altitude > 12:
        time += (altitude - 12) / 0.075
        altitude = 12

    time += altitude / 0.02

    print("Total time:", round(time, 1))

if __name__ == "__main__":
    main()
