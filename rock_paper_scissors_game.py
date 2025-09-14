from random import randint
from logo import logo_game

print(logo_game)
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
attempts = 5
is_user_win = 0
is_computer_win = 0
print(f"YOU HAVE {attempts} ATTEMPTS TO BEAT THE COMPUTER AND WIN!\nLET'S TRY?")

while attempts > 0:
    user_move = input("Pick rock🪨 [r], paper📜 [p] or scissors✂️ [s]: \n").lower()
    attempts -= 1
    if user_move == "r": user_move = rock
    elif user_move == "p": user_move = paper
    elif user_move == "s": user_move = scissors
    else: raise SystemExit("🔥Invalid option! Try again!🔥")

    computer_random_number = randint(1, 3)
    computer_move = ""
    if computer_random_number == 1: computer_move = rock
    elif computer_random_number == 2: computer_move = paper
    elif computer_random_number == 3: computer_move = scissors
    print(f"Computer chose {computer_move}.")

    if user_move == computer_move: print(f"Draw!️🙌\nAttempts: {attempts}/5")
    elif user_move == rock and computer_move == paper: print(f"😭😭😭YOU LOSE😭😭😭\nAttempts: {attempts}/5"); is_computer_win += 1
    elif user_move == rock and computer_move == scissors: print(f"🏆😜YOU WIN!🏆😜\nAttempts: {attempts}/5"); is_user_win += 1
    elif user_move == paper and computer_move == rock: print(f"🏆😜YOU WIN!🏆😜\nAttempts: {attempts}/5"); is_user_win += 1
    elif user_move == paper and computer_move == scissors: print(f"😭😭😭YOU LOSE😭😭😭\nAttempts: {attempts}/5"); is_computer_win += 1
    elif user_move == scissors and computer_move == rock: print(f"😭😭😭YOU LOSE😭😭😭\nAttempts: {attempts}/5"); is_computer_win += 1
    elif user_move == scissors and computer_move == paper: print(f"🏆😜YOU WIN!🏆😜\nAttempts: {attempts}/5"); is_user_win += 1
if is_user_win > is_computer_win:
    print("🥳🥳🥳🥳🏆🔥🏆🔥YOU'RE THE WINNER🏆🔥🏆🔥🥳🥳🥳🥳")
else:
    print("😭😭😭😭😭😭😭SORRYYYYYY! YOU LOSE!😭😭😭😭😭😭😭")



