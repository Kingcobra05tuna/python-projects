from random import randint

DIFFICULTIES =  {
    "easy": 10, "medium": 100, "hard": 1_000,
    "extreme": 10_000, "impossible": 1_000_000}

def game():
    # Get valid input
    while True:
        d = input(f"Difficulty {tuple(DIFFICULTIES)}: ").strip().lower()
        if d in DIFFICULTIES: break
        print("Invalid input.")

    # Set the random number goal
    goal = randint(1, DIFFICULTIES[d])
    attempts = 0

    # Guessing until finding the goal
    while True:
        try:
            num = int(input(f"Guess (1 - {DIFFICULTIES[d]}): "))
            if not 1 <= num <= DIFFICULTIES[d]: raise ValueError
        except ValueError:
            print("Invalid input.")
            continue

        attempts += 1
        if num < goal:
            print("Higher!")
        elif num > goal:
            print("Lower!")
        else:
            print(f"You won in {attempts} attempts!")
            break

# Makes the game replayable
def main():
    while True:
        game()
        if input("Try again? (y/n): ").lower()[0] != "y": break

if __name__ == "__main__":
    main()
