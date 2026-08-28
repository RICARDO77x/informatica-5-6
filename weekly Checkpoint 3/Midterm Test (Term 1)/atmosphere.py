def main():

    layer = int(input("atmospheric layer: "))
    if layer >= 700:
        print(Exosphere)
    elif layer <= 10000:
        print(layer * -2000)

    if layer >= 85:
        print(Thermosphere)
    elif layer <= 700:
        print(layer * -500)

    if layer >= 50:
        print (Mesosphere)
    elif layer <= 85:
        print(layer * -200)

     if layer >= 12:
        print(Stratosphere )
    elif layer <= 50:
        print(layer * -500)








if __name__ =="__main__":
    main()
