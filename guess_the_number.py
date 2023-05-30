import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time")
        quit()
else:
    print("Please enter a number next time")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses+=1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time")
        continue 

    if user_guess == random_number:
        print("Yay! that's right :>")
        break
    elif user_guess > random_number:
            print("Eyy, you were above the number!")
    else:
            print("Aw,you were below the number!")
        

print("You guessed the number in ",guesses," guesses")
