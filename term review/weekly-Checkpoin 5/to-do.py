def main():
    tareas = []
    while True:
        print("Hello, I am your listing assistant; I am here to note down whatever you tell me.")
        print(F"you have {len(tareas)} tareas to do")
        print(tareas)
        command = input("what do you want to do? (add, complete, or stop): ").lower()
        if command == "add":
            new_tareas = input("Enter a new tareas: ")
            tareas.append(new_tareas)


        if command == "complete":
            new_tareas = input("")

        elif command == "stop":
            break















if __name__ == "__main__":
    main()
