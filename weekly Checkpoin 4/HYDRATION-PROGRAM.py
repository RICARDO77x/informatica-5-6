import time

def main():
    start = 160

    name = input("Hi! What's your name? ").title().strip()
    print(f"HI {name}! The football game is about to start, I'll remember you when to drink water.")
    ready = input("Are you ready to start?:")
    print("the time is estart")
    print()
    print()
    print("-----------------------------------------------------------------------------------------")

    while start > 0:
        if ready == "yes":
            print("Water pause has started.")
            time.sleep(60)
            start -= 1
        elif ready == "no":
            print("Okay, I'll wait")
            break

if __name__ == "__main__":
    main()


