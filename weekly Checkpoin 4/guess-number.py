import random

def main():

    name = input("What's your name? ").title().strip()
    print(f"Hello {name} I am thinking of a number between 1 and 100")
    print("difficulty level")
    print("easy")
    print("medium")
    print("hard")

    difficulty =  input("Choose a difficulty level: ").strip().lower()

    if difficulty == ("easy"):
        print("you selected difficulty", difficulty)
        print("Now guess the number I'm thinking of between 1 and 10")
        number = random.randint(1, 10)
        guess = 0
        while guess != number:
            guess = int(input("take a guess: "))
            if guess> number:
                print("Your guess is too high")
            elif guess < number:
                print("Your guess is too low")
        print(f"Good Job, {name}! You guesse my number!")


    if difficulty == ("medium"):
        print("you selected difficulty", difficulty)
        print("Now guess the number I'm thinking of between 1 and 100")
        number = random.randint(1, 100)
        guess = 0
        while guess != number:
            guess = int(input("take a guess: "))
            if guess> number:
                print("Your guess is too high")
            elif guess < number:
                print("Your guess is too low")
        print(f"Good Job, {name}! You guesse my number!")



    if difficulty == ("hard"):
        print("you selected difficulty", difficulty)
        print("Now guess the number I'm thinking of between 1 and 1000")
        number = random.randint(1, 1000)
        guess = 0
        while guess != number:
            guess = int(input("take a guess: "))
            if guess> number:
                print("Your guess is too high")
            elif guess < number:
                print("Your guess is too low")
        print(f"Good Job, {name}! You guesse my number!")







if __name__ =="__main__":
    main()
