import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
stages = hangman_art.stages

word = random.choice(word_list)

print(hangman_art.logo)
print(f"The Word: {word}")
listGuess = []
for i in range(len(word)):
    listGuess.append("_")

condition = True
lives = 6
while condition:
    guess = input("Guess a letter: ").lower();

    indexGuess = 0
    correctAnswer = 0
    for char in word:
        if char == guess:
            listGuess[indexGuess] = guess
            correctAnswer +=1
        indexGuess +=1
    if correctAnswer == 0:
        lives -=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    
    print(stages[lives])

    if "_" not in listGuess:
        condition = False
        print("You win")
    
    if lives == 0:
        condition = False
        print("You Lose")

    print(' '.join(listGuess))