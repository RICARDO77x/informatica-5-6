def main():

    p = float(input("Enter your quantity in pesos:"))
    s = float(input("Enter your quantity in soles:"))
    r = float(input("Enter your quantity in reais:"))


    mxn = (p * 0.0054) + (s*5.07) + (r* 3.28)
    usd = mxn / 17.06


    print("USD:", round(usd, 2))
    print("MXN:", round(usd, 2))












if __name__ =="__main__":
    main()
