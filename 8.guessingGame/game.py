import sys
import random
import cowsay

number = random.randint(0, 10)
cowsay.cow('Try to guess the number between 0 to 10 in 3 guesses!')

guess1 = int(input('\n Enter your first guess: '))
if guess1 == number:
        cowsay.cow('You guest in on the first try! Congratulation!')
        sys.exit()
elif guess1 > number:
        cowsay.cow('Your guess is higher than the number!')
else:
        cowsay.cow("Your guess is lower than the number!")

guess2 = int(input('\n Enter your second guess: '))
if guess1 == number:
        cowsay.cow('You guest in on the second try! Great job!')
        sys.exit()
elif guess2 > number:
        cowsay.cow('Your guess is higher than the number!')
else:
        cowsay.cow("Your guess is lower than the number!")

guess3 = int(input('\n Enter your third guess: '))
if guess3 == number:
        cowsay.cow('You guest in on the third try! Nice!')
elif guess3 > number:
        cowsay.cow('Your guess is higher than the number: ' + str(number))
        cowsay.cow('Sorry, you just lost!')
else:
        cowsay.cow('Your guess is lower than the number: ' + str(number))
        cowsay.cow('Sorry, you just lost!')

                                                                
