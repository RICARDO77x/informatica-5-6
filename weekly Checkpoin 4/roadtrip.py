def main():
    answer = "" # Initialize
    followup = ""

    while answer != "Yes!": # Condition
        answer = input("Are we there yet? ").strip().title() #update
        if answer == "Yes":
            followup = input("Really? ").strip().title()
        if followup == "Yes!":
         break

    print("We just arrived NUEVO CASAS GRANDES!")








if __name__ =="__main__":
    main()
