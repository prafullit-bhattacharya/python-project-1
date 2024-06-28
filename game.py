import random

# Snake-Water-Gun game
# 1 for water
# -1 for snake
# 0 for gun
computer = random.choice([1, -1, 0])

# Dictionary to map user input to game choices
youdict = {"s": -1, "w": 1, "g": 0}

# Dictionary to reverse map choices to their string representation
reversedict = {-1: "snake", 1: "water", 0: "gun"}

youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
if youstr not in youdict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youdict[youstr]
    print(f"You entered: {reversedict[you]}")
    print(f"Computer chose: {reversedict[computer]}")

    if computer == you:
        print("Tie")
    else:
        if (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
            print("You Win!")
        elif (computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer == 0 and you == 1):
            print("You Lose!")
        else:
            print("Something went wrong!")
