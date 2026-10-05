def main():
    not_validated = True
    while not_validated:
        try:
            #number = imput("enter a number: ") # "1"
            number = int(input("Enter a number between 1 and 11: ")) #1
            if number in nums:
                print("Number stored sucesfully.")
                not_validated = False # -> break
                else
        except ValueError:
            print("Enter a NUMBER")







if __name__ =="__main__":
    main()
