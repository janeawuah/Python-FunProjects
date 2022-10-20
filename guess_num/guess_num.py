import random

num_to_guess = random.randint(1,10)
guessed_num = 0

while guessed_num != num_to_guess:
    guessed_num = input("Guess a number between 1 and 10: ")
    guessed_num = int(guessed_num)


    if guessed_num == num_to_guess:
        print("CONGRATULATIONS!!!!! ", guessed_num, " is the correct number. You guessed right")
    else:
        print("Sorry, please try again")