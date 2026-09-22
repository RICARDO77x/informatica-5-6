def main():

    tasks =[]

    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)

        new_task = input("Enter tasks: ").capitalize().strip()

        if new_task == "Exit":
            break
        elif new_task in tasks:
            tasks.append(new_task)
        elif new_task in tasks:
            del_confirm = input(f"Did you completed {new_taks}? (y/n): ").lower().strip()
            if del_confirm == "y":
                tasks.remove(new_task)
        else:
            continue

#fruits = ["apple", "banana", "cherry"]
    #print("pineapple" not in fruits)

    #fruits = "apple"
    #print("b" in fruits)




















if __name__ == "__main__":
    main()
