import time
import random

name1 = input("Enter first player's name: ")
name2 = input("Enter second player's name: ")
time.sleep(1)

print("Welcome to the Number Guessing Game!")
print(f"{name1} and {name2}, you will take turns guessing a number between 1 and 10. You have three turns each to guess the number.")
print("The player who guesses the number correctly first wins!")
time.sleep(1)
print("Okay! Let's start the game!")
time.sleep(1)

guessed_number = []

while len(guessed_number) != 5:
    random_number = random.randint(1, 10)
    while random_number in guessed_number:
        random_number = random.randint(1, 10)
    guessed_number.append(random_number)

p1_score = []
p2_score = []
for i in range(3):
    print(f"\nRound {i+1}:")
    print(f"The number to guess is: {guessed_number[i]}")  # Display the guessed number by the computer
    
    print(f"{name1}, it's your turn to guess the number.")
    guess1 = int(input("Enter your guess: "))
    while guess1 in p1_score or guess1 in p2_score:
        print("You have already guessed this number!")
        guess1 = int(input("Enter your guess: "))
    if guess1 == guessed_number[i]:
        print(f"Congratulations {name1}! You guessed the number!")
        p1_score.append(guess1)
    else:
        print(f"Sorry {name1}, that's not correct.")
        
    print(f"{name2}, it's your turn to guess the number.")
    guess2 = int(input("Enter your guess: "))
    while guess2 in p1_score or guess2 in p2_score:
        print("You have already guessed this number!")
        guess2 = int(input("Enter your guess: "))
    if guess2 == guessed_number[i]:
        print(f"Congratulations {name2}! You guessed the number!")
        p2_score.append(guess2)
    else:
        print(f"Sorry {name2}, that's not correct.")
    
    # Display scores after each round
    print(f"\nScores after Round {i+1}:")
    print(f"{name1}'s score: {len(p1_score)}")
    print(f"{name2}'s score: {len(p2_score)}")

print("\nGame Over!")
print(f"{name1}'s final score: {len(p1_score)}")
print(f"{name2}'s final score: {len(p2_score)}")

if len(p1_score) > len(p2_score):
    print(f"Congratulations {name1}! You are the winner!")
elif len(p2_score) > len(p1_score):
    print(f"Congratulations {name2}! You are the winner!")
else:
    print("It's a tie!")