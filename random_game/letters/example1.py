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
print('Advinhe qual letra do alfabeto eu pensei. (Digite da seguinte forma: \'<letra minuscula>\') \n')

# Main loop
while guesses_taken < 10:

  guess = input("Diga a letra: ")

  guesses_taken = guesses_taken + 1

  # Giving the user some tips
  if letters.index(guess) < letters.index(letter):
      print('Tente uma que venha depois dessa.')

  elif letters.index(guess) > letters.index(letter):
      print('Tente uma que venha antes dessa.')

  else:
      break

# Final messages
if guess == letter:
    guesses_taken = str(guesses_taken)
    print('Bom trabalho! Voce advinhou em ' + guesses_taken + ' tentativas!')

if guess != letter:
    letter = str(letter)
    print('Não deu. A letra desejada era: ' + letter)
