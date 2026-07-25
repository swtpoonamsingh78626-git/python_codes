import random

words = ["python", "rainbow", "computer", "school", "banana"]

word = random.choice(words)

display = []

for letter in word:
    display.append("_")

lives = 6

print("🎮 Welcome to Hangman!")

while lives > 0:

    print("\nWord:", " ".join(display))

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You already guessed that letter!")
        continue

    if guess in word:
        print("✅ Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        lives -= 1
        print("❌ Wrong!")
        print("Lives left:", lives)

    if "_" not in display:
        print("\n🎉 Congratulations!")
        print("The word was:", word)
        break

if "_" in display:
    print("\n💀 Game Over!")
    print("The word was:", word)