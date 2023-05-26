print("Welcome to my first quiz game")
print("Let's test your knowledge on cats!")
play = input("Would you like to play ? ") 

if play != "yes":
    quit()

print("Yay! Let's play :>")
score = 0 

answer = input("1. What is a baby cat called ? ")
if answer.lower() == "kitten":
    print("Good job!, onwards we go")
    score +=1
else: 
    print("Aw, Wrong answer :<")

answer = input("2. What is a group of cats called ? ")
if answer.lower() == "clowder":
    print("That's right!")
    score +=1
else: 
    print("Nooo :( )")

answer = input("3. What is the noise a cat makes when it is happy ? ")
if answer.lower() == "purr" or answer.lower() == "purring":
    print("Yes, you got it! ")
    score +=1
else: 
    print("Nope, that's not it")

answer = input("4. What is garfield's favorite food ? ")
if answer.lower() == "lasagna":
    print("Good job!, onwards we go")
    score +=1
else: 
    print("Aw, Wrong answer :<")

answer = input("5. How many teeth does a cat have ? ")
if answer == "30" or answer == "thirty" or answer == "Thirty":
    print("Yess, you did it!")
    score +=1
else: 
    print("That's wrong :< ")

print("You've reached the end of this quiz, good job! :>")
print("You got " + str(score) + " questions out of five right")