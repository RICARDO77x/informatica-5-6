def main():
    welcome()
    choice = int(input("Select your order: "))
    get_item(choice)


def welcome():
    menu = ["Cheeseburger", "Fries", "soda", "Ice Cream", "Cookie"]
    print("Welcome to the pollos hermanos!")
    print("Here's the menu choice:")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")


def get_item(order):
     kitchen = ["🍔", "🍟", "🥤", "🍦", "🍪"]
     if 1 <= order <= 5:
          print(kitche[order - 1])
        else
          print("Not in our menu.")


if __name__ == "__main__":
    main()
