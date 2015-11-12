# coding: utf-8

# Letter guessing game.

import random
import string

guessesTaken = 0

letter = random.choice(string.ascii_lowercase)

while guessesTaken < 6:

  print("Adevenha a letra.")
  guess = input()
  guessesTaken = guessesTaken + 1

  if guess == letter:
    break

if guess == letter:
  guessesTaken = str(guessesTaken)
  print("Você conseguiu em " + guessesTaken)

if guess != letter:
  letter = str(letter)
  print("Seu lixo. A letra era: " + letter)
