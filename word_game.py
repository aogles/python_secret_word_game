import random


words_to_guess = ["dovagedy", "dracarys", "valar-morghulis", "valryrian", "daenerys", "Vhagar",
                  "syrax", "caraxes", "vermithor", "meleys", "seasmoke", "dreamfyre", "targaryen", "viserys", "rhaenyra", "jon-snow"]
word = random.choice(words_to_guess)


word_display = '_' * len(word)
guessed = False
guessed_letters = []
guessed_words = []
tries = 6
print("Let's play a word game!")
print(word_display)
print("you have", tries, "tries")
print("\n")

while not guessed and tries < 7:
    guess = input("Guess a letter or word!_")

    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You have guessed this letter", guess)
        elif guess not in word:
            print(guess, "is not in the word :(")
            tries -= 1
            guessed_letters.append(guess)
        else:
            print("Great job!", guess, "is in the word")
            guessed_letters.append(guess)
            completed_word = list(word_display)
            indices = [i for i, letter in enumerate(
                word) if letter == guess]
            for index in indices:
                completed_word[index] = guess
            word_display = "".join(completed_word)
            if "_" not in word_display:
                guessed = True

    elif len(guess) == len(word) and guess.isalpha():
        if guess in guessed_words:
            print("You have guessed this word already", guess)
        elif guess != word:
            print(guess, "is not the word :(")
            tries -= 1
            guessed_words.append(guess)
        else:
            guessed = True
            word_display = word

    else:
        print("Not a valid guess,try again!")
    print(word_display)
    print(tries)
    print("\n")
    if guessed:
        print("congrats you guessed the word!")
        break
    if tries == 0:
        print("sorry you ran out of tries, the word was", word)
        break
