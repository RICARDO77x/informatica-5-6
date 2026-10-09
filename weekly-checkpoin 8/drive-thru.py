def main():
      welcome()
      choise = int(input("Select your order: "))
      get_item(choise)


def welcome():
      menu =["Cheeseburger", "Fries", "soda", "Ice Cream", "Cookie"]
      print("welcome to the pollos hermanos!")
      print("Here's the menu chose:")
      for i in range(len(menu)):
           print(f"{i+1}. {menu[i]}")
#range cuanta todo lo de la lista

def get_item(order):
     kitchen = ["🍔", "🍟", "🥤", "🍦", "🍪"]
     if 1 <= order <= 5:
          print(kitche[order - 1])
        else
          print("Not in our menu.")
   #  if order == 1:
    #print("")
     #elif order == 2:



#def get_item():



if __name__ =="__main__":
    main()
