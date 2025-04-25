import time
import random

name1 = input("Enter first player's name: ")
time.sleep(1)
name2 = input("Enter second player's name: ")
time.sleep(1)
print("Welcome to the Number Guessing Game!")
time.sleep(1)
print(f"{name1} and {name2}, you will take turns guessing a number between 1 and 10. You have three turns each to guess the number.")
print("The player who guesses the number correctly first wins!")
time.sleep(1)
print("Okay ! Let's start the game!")
time.sleep(2)

guessed_number=[]
while len(guessed_number) < 1:
    random_number = random.randint(1, 10)
    if random_number not in guessed_number:
        guessed_number.append(random_number)
    else:
        random_number = random.randint(1, 10)
        guessed_number.append(random_number)

score1 = 0
score2 = 0

for round_num in range(1, 4):
    print(f"Round {round_num}:")
    
    print(f"{name1}, it's your turn to guess the number.")
    guess1 = int(input("Enter your guess: "))
    if guess1 == random_number:
        print(f"Congratulations {name1}! You guessed the number!")
        score1 += 1
    else:
        print(f"Sorry {name1}, that's not correct.")
    
    print(f"{name2}, it's your turn to guess the number.")
    guess2 = int(input("Enter your guess: "))
    if guess2 == random_number:
        print(f"Congratulations {name2}! You guessed the number!")
        score2 += 1
    else:
        print(f"Sorry {name2}, that's not correct.")
    print("-" * 30)


print("Game Over!")
print(f"Guessed number was: {guessed_number}")
print(f"Final Scores:\n{name1}: {score1}\n{name2}: {score2}")

if score1 > score2:
    print(f"{name1} wins!")
elif score2 > score1:
    print(f"{name2} wins!")
else:
    print("It's a tie!")