
import random
from art import stages, logo
from words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

print(logo)

display = ['_' for _ in range(word_length)]
print(display)

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"{guess} alread chosen")

  for position, letter in enumerate(chosen_word):
    if letter == guess:
      display[position] = letter
      print(display)

  if guess not in chosen_word:
    print(f"{guess} is not in the word")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("you loose")

  if "_" not in display:
    end_of_game = True
    print("you win")

  print(stages[lives])

  

