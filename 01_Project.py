''' we are going to write a programe that generates a random number and 
ask the user to guess it. 
if the player guess is highter than the actual number, the program displays 
"Lower numbers please".
Similarly if the user guess is too low, the program print 
"Highter number please". when the user guess the correct number, 
program display the number of guesses the player uset to arrives at the 
number.

Hint : use the random module 
'''

import random 
randNumber = random.randint(1,100)
# print(randNumber) // random Number show in user output
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("enter your guess : "))
    guesses += 1
    if(userGuess==randNumber):
       print("you guessed it right !")
    else:
         if(userGuess>randNumber):
             print("you guesses it wrong enter a smaller number ")
         else:
             print("you guesses it wrong! enter a large number ")
        
         print(f"you guessed the number in {guesses} guesses ")
    
with open("hiscore.txt","r") as f:
    hiscore = int(f.read())
    
    if(guesses<hiscore):
        print("you have just broken the high score! ")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses()))






































































































