categories = {}
count = 0

def average(*numbers):
    return sum(numbers) / len(numbers)

def setCategories():
    while True:
        try:
            count = int(input("Enter the number of categories: "))
            break
        except ValueError:
            print("Invalid input.")
            continue
    
    categories.clear()
    for i in range(count):
        while True:
            try:
                inp = input(f"Enter the {i + 1}. category: ")
                val = int(input(f"Enter the value for category '{inp}': "))

                if val < 0:
                    print("Value is smaller than 0, setting it to 0.")
                    val = 0
                elif 100 < val:
                    print("Value is bigger than 100, setting it to 100.")
                    val = 100
                else:
                    pass

                categories[inp] = val
                break
            except ValueError:
                print("Invalid input.")
                continue
        

def main():
    print("********** Average Score Calculator **********\n")
    setCategories()
    print(f"Average score: {average(*list(categories.values()))}")

if __name__ == "__main__":
    main()
