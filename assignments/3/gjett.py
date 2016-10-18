import random

def main():
    secret = random.randint(1, 100)

    while True:
        attempt = int(input("Make a guess: "))

        if attempt == secret:
            print("You guessed correctly! The number was", secret)
            break;
        elif attempt > secret:
            print("The correct number is lower than your guess")
        elif attempt < secret:
            print("The correct number is higher than your guess")

if __name__ == "__main__":
    main()
