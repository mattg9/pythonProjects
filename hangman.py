# HANGMAN
# Matthew Gaston
#
# A guess the word game
# Makes of use of Random, Variables, Boolean,
# Input and Output, Integer, Char,
# String, Length, and Print
 
import random
# list of possible game words randomly chosen when the game starts
dictionary = ["green day", "blink", "red hot chili peppers",
              "foo fighters", "black keys", "runaway nation",
              "breaking benjamin", "the beatles"]

# determine if letter user guessed is contained in the game word
def isCorrectLetter(letter, word, hiddenWord):
    flag = False
    index = 0
    charCount = 0
    for char in word:
        if char == letter:
            flag = True
            charCount += 1
            hiddenWord[index] = letter
        index += 1
    if flag == True:
        print("Very Good! There is ", charCount, " ", letter, ".")
    else:
        print ("Nope! There is no ", letter)        
    # return the result of guessed letter
    return "".join(hiddenWord)

# determine if user guessed the right word
def isCorrectGuess(word, gameword):
    result = word == gameword
    if result == True:
        print("That's correct!")
    else:
        print("Nope! That's not it!")
    return result

# make gameword invisible
def hideWord(word):
    w = list(word)
    for i in range(len(w)):
        if w[i] != ' ':
            w[i] = '*'
    return "".join(w)
            
def main():
    answer = input("Want to play Hangman? (y/n): ")
    if answer != 'y':
        exit()
    gameWord = random.choice(dictionary)
    hiddenWord = hideWord(gameWord)
    guessWordCount = 0
    guessLetterCount = 0
    # up to 5 word guesses and only 10 incorrect letter guesses
    while guessWordCount < 5 and guessLetterCount < 10:
        print(hiddenWord)
        play = input("Guess letter or word? (l/w): ")
        # guess word workflow
        if play == 'w':
            guess = input("What's the word?: ")
            if not isCorrectGuess(guess, gameWord):
                guessWordCount += 1
            else:
                break
        # guess letter workflow
        elif play == 'l':
            letter = input("Guess a letter: ")
            hiddenWord = isCorrectLetter(letter, list(gameWord), list(hiddenWord))
        # user error
        else:
            print("invalid input")
          
# execute the game
if __name__ == "__main__":
    while True:
        main()
