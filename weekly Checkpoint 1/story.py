def main():
    # planet = input("Planet: ")

    # # Separation
    # print("Hello", planet)

    # # Ending
    # print("Hello", end=" ")
    # print(planet)

    # # Concatenation
    # print("Hello " + planet)

    # # Formatted String
    # print(f"Hello {planet}")

    name = input("What's your name? ").title().strip()
    color = input("Tell me a color: ").lower().strip()
    adj = input("Give me an adjective: ")
    goal = input("A goal you would like o achieve: ")

    print(f"Hello {name}!")
    print()

    print("this your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will fially {goal}.")

    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will fially {goal}.".upper())
if __name__ == "__main__":
   main()
