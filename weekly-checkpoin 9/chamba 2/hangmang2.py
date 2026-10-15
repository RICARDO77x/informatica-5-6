def main():
   with open("words.txt") as file:
       content = file.read()
       print(content)
       Turn file into a list
    with open("words.txt") as start_game:
       start_game = start_game.read().splitlines()

   # for day in range(len(hoco_list)):
      #  print(f"Day {day + 1}: {hoco_list[day]}")

if __name__ == "__main__":
    main()

