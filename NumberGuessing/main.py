from random import randint

DIFFICULTIES = {"easy":10, "medium":100, "hard":1_000, "extreme":10_000, "impossible":1_000_000}

def main():
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
            n = int(input(f"Guess (1 - {DIFFICULTIES[d]}): "))
            if not 1 <= n <= DIFFICULTIES[d]: raise ValueError
        except ValueError:
            print("Invalid input.")
            continue

        attempts += 1
        if n < goal:
            print("Higher!")
        elif n > goal:
            print("Lower!")
        else:
            print(f"You won in {attempts} attempts!")
            break

    # Replay
    if input("Try again? (y/n): ").lower()[0] == "y": main()

if __name__ == "__main__":
    main()
