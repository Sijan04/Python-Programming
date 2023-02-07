from random import randint


guessNumber=int(input("Enter guess betweeen 1 to 5 :"))
randomNumber=randint (1,5)

if guessNumber==randomNumber:
     print("you have won")

else:
    print("you have lost")
    print("Random number was:",randomNumber)