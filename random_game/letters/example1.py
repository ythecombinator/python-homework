# -*- coding: utf-8 -*-

# Let's import random to generate pseudo-random numbers
import random
# Let's import string to get all the characters that are considered lowercase letters
import string

# Let's set the initial value of used chances to 0
guesses_taken = 0

# Making a list of letters
letters = list(string.lowercase)

# Chosing a random letter from the just generated list
letter = random.choice(letters)

# Explanation test
print('Guess a letter. (Type as the following: \'<letra minuscula>\') \n')

# Main loop
while guesses_taken < 10:

  guess = input("What's your try? ")

  guesses_taken = guesses_taken + 1

  # Giving the user some tips
  if letters.index(guess) < letters.index(letter):
      print('Why don\'t you try one that comes after the one you\'ve just tried?')

  elif letters.index(guess) > letters.index(letter):
      print('Why don\'t you try one that comes before the one you\'ve just tried?')

  else:
      break

# Final messages
if guess == letter:
    guesses_taken = str(guesses_taken)
    print('Good job! It took you only ' + guesses_taken + ' tries!')

if guess != letter:
    letter = str(letter)
    print('Sorry. The right answer was: ' + letter)
