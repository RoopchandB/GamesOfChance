import random

money = 100

#Write your game of chance functions here


def coinFlipp(guess, bet):
  result = random.randint(1, 2)
  
  if bet > money:
    print("Please bet with the amount you have,not more than that!!\n")
  elif bet <= 0:
    print("Please have a minimum of 1$ to place a bet\n")
    return 0  
 
  elif guess == "heads" and result == 1:
    print("Coin flipped and you guessed:" + guess + "\nYou placed $" + str(bet) + " on " + guess + "." + "\nThe coin lands on " + guess + "!" + "\nWon $" + str(bet) + "\nTotal amount in your betwallet is $" + str(money+bet) + "!")
    return bet
  elif guess == "heads" and not result == 1:
    print("Coin flipped and you guessed:" + guess + "\nYou placed $" + str(bet) + " on " + guess + "." + "\nThe coin lands on tails!" + "\nLost $" + str(bet) + "\nTotal amount in your betwallet is $" + str(money-bet) + "!")
    return -bet
  elif guess == "tails" and result == 1:
    print("Coin flipped and you guessed:" + guess + "\nYou placed $" + str(bet) + " on " + guess + "." + "\nThe coin lands on tails!" + "\nLost $" + str(bet) + "\nTotal amount in your betwallet is $" + str(money-bet) + "!")
    return -bet
  elif guess == "tails" and not result == 1:
    print("Coin flipped and you guessed:" + guess + "\nYou placed $" + str(bet) + " on " + guess + "." + "\nThe coin lands on " + guess + "!" + "\nWon $" + str(bet) + "\nTotal amount in your betwallet is $" + str(money+bet) + "!")
    return bet
  else:
    print("Your guess is not valid. Enter 'heads' or 'tails'")


def cards(bet):
  my_card = random.randint(1, 13)
  your_card = random.randint(1, 13)
  if(bet < 0):
    print("The min bet amount is 1 dollar")
    return 0
  elif(bet > money):
    print("Please bet with the amount you have,not more than that!!\n")
  elif(my_card > your_card):
    print("My card is higher! with the value of " + str(my_card) + " as compared to your card with the value of " + str(your_card) + "." + "\nI won $" + str(bet) + "!" + "\nThe total amount I have in my card wallet is $" + str(money + bet) + "!")
    return bet
  elif(my_card < your_card):
    print("Your card is higher! with the value of " + str(your_card) + " as compared to my card with the value of " + str(my_card) + "." + "\nI lost $" + str(bet) + "!" + "\nThe total amount you have in your cardwallet is $" + str(money - bet) + "!")
    return -bet
  else:
    print("It's a tie! neither of us was won or lost have")
    return 0



def diceRoll(guess,bet):
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  sum_of_dice = dice1 + dice2
  if(bet < 0):
    print("The min bet amount is 1 dollar")
    return 0
  elif(bet > 25):
    return "The max bet amount is 20 dollars"
  elif(sum_of_dice % 2 == 0 and guess =="Even"):
    total_Amount = money + bet
    print("You guessed the sum is " + guess + "\nYou placed $" + str(bet) + " on " + guess + "\nThe sum of two dice's is " + str(sum_of_dice) + " and it is "+ guess + "." + "\nWon $" + str(bet) + "\nYour total money is " + str(total_Amount) + " dollars remaining.")
    return bet
  elif(sum_of_dice % 2 == 0 and guess =="Odd"):
    total_Amount = money - bet
    print("You guessed the sum is " + guess + "\nYou placed $" + str(bet) + " on " + guess + "\nThe sum of two dice's is " + str(sum_of_dice) + " and it is even." + "\nLost $" + str(bet) + "\nYour total money is " + str(total_Amount) + " dollars remaining.")
    return -bet
  elif(sum_of_dice % 2 != 0 and guess =="Even"):
    total_Amount = money - bet
    print("You guessed the sum is " + guess + "\nYou placed $" + str(bet) + " on " + guess + "\nThe sum of two dice's is " + str(sum_of_dice) + " and it is odd." + "\nLost $" + str(bet) + "\nYour total money is " + str(total_Amount) + " dollars remaining.")
    return -bet
  elif(sum_of_dice % 2 != 0 and guess == "Odd"):
    total_Amount = money + bet
    print("You guessed the sum is " + guess + "\nYou placed $" + str(bet) + " on " + guess + "\nThe sum of two dice's is " + str(sum_of_dice) + " and it is "+ guess + "." + "\nWon $" + str(bet) + "\nYour total money is " + str(total_Amount) + " dollars remaining.")
    return bet
  else:
    print("Your guess is not valid. Enter 'Even' or 'Odd'")




def roulette(guess, bet):
  randomBall = random.randint(0,36)
  if randomBall == 36:
    print("This is the highest roulette landed on")
  else:
        print("The roulette landed on " + str(randomBall))

  if bet > money:
    print("Please bet with the amount you have,not more than that!!\n")
  elif bet <= 0:
    print("Please have a minimum of 1$ to place a bet\n")
    return 0 
  elif guess == randomBall:
    print("You guessed: " + str(guess) + "\nThe randomBall in roulette wheel spinned to:" + str(randomBall) + "\nThis is the biggest win of the day,Happy Days!!!" + "\nYou won " + str(bet * 34) + "!" + "\nTotal amount in your roulette wallet is $" + str(money + bet * 34) + "!!")
    return bet * 34
  elif guess == "Even" and randomBall % 2 == 0:
    print("You guessed: " + str(guess) + "\nThe randomBall in roulette wheel spinned to:" + str(randomBall) + "\nIt is Even" + "\nYou won " + str(bet) + "!" + "\nTotal amount in your roulette wallet is $" + str(money + bet) + "!")
    return bet
  elif guess == "Even" and randomBall % 2 != 0:
    print("You guessed: " + str(guess) + "\nThe randomBall in roulette wheel spinned to:" + str(randomBall)  + "\nIt is Odd" + "\nYou lost " + str(bet) + "!" + "\nTotal amount in your roulette wallet is $" + str(money - bet) + "!")
    return -bet
  elif guess == "Odd" and randomBall % 2 == 0:
    print("You guessed: " + str(guess) + "\nThe randomBall in roulette wheel spinned to:" + str(randomBall)  + "\nIt is Even" + "\nYou lost " + str(bet) + "!" + "\nTotal amount in your roulette wallet is $" + str(money - bet) + "!")
    return -bet
  elif guess == "Odd" and  randomBall % 2 != 0:
    print("You guessed: " + str(guess) + "\nThe randomBall in roulette wheel spinned to:" + str(randomBall)  + "\nIt is Odd" + str(randomBall) + "\nYou won " + str(bet) + "!" + "\nTotal amount in your roulette wallet is $" + str(money + bet) + "!")
    return bet
  elif guess != randomBall:
    print("lose $" + str(bet) + """.
have $""" + str(money - bet) + ".")
    return -bet

#Call your game of chance functions here

money += coinFlipp("heads", 10)
money += cards(5)
money += diceRoll("Even", 2)
money += roulette("Even", 10)
money += roulette(3, 1)
money += roulette("Odd", money)
print("Your total amount of money is " + str(money))


