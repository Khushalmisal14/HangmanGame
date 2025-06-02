# Hangman Game Using Python-----------------------------

import random

# 1. Predefined list of 5 words
word_list = ['apple', 'table', 'grape', 'chair', 'bread']
chosen_word = random.choice(word_list)

# 2. Set up variables
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# 3. Create a display version of the word
display_word = ['_' for _ in chosen_word]

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# 4. Game loop
while incorrect_guesses < max_guesses and '_' in display_word:
    print("Current word:", ' '.join(display_word))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Invalid input. Please enter one single letter.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You've already guessed that letter. Try another.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Correct!\n")
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong! You have {max_guesses - incorrect_guesses} guesses left.\n")

# 5. Game result
if '_' not in display_word:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 Game Over! The word was:", chosen_word)
