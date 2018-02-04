def get_secret_word():
    secret_word = input('Please enter a word to be guessed\n'
            'that does not contain ? or white space: ').lower()
    
    return secret_word


#This function checks whether or not the secret word is valid. If the secret word has a question mark or a space, check_secret_word will return "False".
#If not, it will return "True".
def check_secret_word(secret_a_word):
    if "?" in secret_a_word:
            return False
    elif secret_a_word.isspace():
            return False
    elif " " in secret_a_word:
            return False
    elif not secret_a_word:
            return False
    else:
        return True

#This function is used to display the hangman according to the number of wrong guesses.
#If the number of wrong guesses is between 1 and 7, display_hangman will print the corresponding component of the hangman.
def display_hangman(num_wrong_guesses):
    if num_wrong_guesses == 1:
        print("     |")
    if num_wrong_guesses == 2:
        print ("     |")
        print ("     0")
        
    if num_wrong_guesses == 3:
        print ("     |")
        print ("     0")
        print ("     |")
        
    if num_wrong_guesses == 4:
        print ("     |")
        print ("     0")
        print ("    /|")
      
    if num_wrong_guesses == 5:
        print ("     |")
        print ("     0")
        print ("    /|\\")

    if num_wrong_guesses == 6:
        print ("     |")
        print ("     0")
        print ("    /|\\")
        print ("    /")
        
    if num_wrong_guesses == 7:
        print ("     |")
        print ("     0")
        print ("    /|\\")
        print ("    / \\")
      
#This function is used to define whether or not the game is over. If the user has 7 wrong guesses, is_game_over will return "True" and print that the player failed.
#If the user correctly guesses the secret word, is_game_over will return "True" and print that the player correctly guessed the secret word.
#If not, is_game_over will simply return "False".
def is_game_over(num_wrong_guesses):
    if num_wrong_guesses == 7:
        print ("You failed to guess the secret word: ", secret_a_word)
        return True
    elif guessSoFar == secret_a_word:
        print ("You correctly guessed the secret word: ", secret_a_word)
        return True
    else:
        
        return False

def get_guess(guess):
    while len(guess) != 1 or guess in stGuesses:
        while len(guess) != 1:
            guess = input("You can only guess a single character. Please enter your next guess: ")
#Each time the user's guess is one that was already guessed, the user is asked to enter a new guess.
        while guess in stGuesses:
            guess = input("You already guessed the character: " + guess + " Please enter your next guess: ")





#The value of get_secret_word becomes a global variable and is assigned to secret_a_word.
secret_a_word = get_secret_word()


#The Boolean value returned by check_secret_word is assigned to the variable, checkFlag.
checkFlag = check_secret_word(secret_a_word)


#While the secret word has a question mark or a space, secret_a_word is redefined to the input determining the secret word to be guessed.
#In other words, the user is asked for a new secret word.
#While the secret word has a question mark or a space, checkFlag obtains a new Boolean value for the new secret word.
#This loop will repeat until checkFlag returns "True" (the secret word no longer contains question marks or spaces.
while checkFlag == False:
    secret_a_word = get_secret_word()
    checkFlag = check_secret_word(secret_a_word)

#secret_a_word is turned into a list and assigned to the variable, listSecret.
listSecret = list(secret_a_word)

print("\n"*30)

#Initializing values for the loops
#Question mark times the length of listSecret is assigned to the variable, guessSoFar, making a string of question marks as long as the secret word.
guessSoFar = "?"*len(listSecret)

#guessSoFar is turned into a list and assigned to the variable, NotKnownList.
NotKnownList = list(guessSoFar)

#Before anything happens, guessNumber and num_wrong_guesses are set to 0. These values will change due to the following while loop as the user inputs guesses.
guessNumber = 0
num_wrong_guesses = 0
#An empty string is set to the variable, stGuesses. Later, this string will be filled with characters guessed by the user.
Guesses = []
stGuesses = ""
#===============

while num_wrong_guesses < 7:

    print ("")
#guessSoFar, the string of question marks, is displayed.
    print (guessSoFar)
#stGuesses, the string of guesses is displayed.
    print ("So far you have guessed: " + ', '.join(Guesses))

           
#The user's next guess is inputted and assigned to the variable, guess.
    guess = input('Please enter your next guess: ')
#Each time the user's guess is more than 1 character long, the guess is reassigned to a new guess until it is 1 character long.

    while len(guess)!=1 or guess in Guesses:
            while len(guess) != 1:
                guess = input("You can only guess a single character. Please enter your next guess: ")
#Each time the user's guess is one that was already guessed, the user is asked to enter a new guess.
            while guess in Guesses:
                guess = input("You already guessed the character: " + guess + " Please enter your next guess: ")

#The latest guess is added to the string of already guessed letters
                
    Guesses.append(guess)
    Guesses = sorted(Guesses)   


        #========================
    if guess in listSecret:
#If the user's guess is part of the secret word, guess number is increased by a value of 1.
        guessNumber += 1
#If the user's guess is part of the secret word, an empty list is created and assigned to the variable, listIndex.
#If an element of listSecret at index i is the same as the guess, that element will be appended to listIndex.
        listIndex=[]
        for i in range (0,len(listSecret)):
            if listSecret[i] == guess:
                listIndex.append(i)

                
#print (listIndex)
#A question mark in NotKnownList is replaced with the correctly guessed letter at the appropriate position.
        for i in listIndex:
            NotKnownList[i] = guess

#NotKnownList is joined into a string of question marks with the correctly guessed values in the string. This string is assigned to the variable, guessSoFar.

        guessSoFar = ''.join(NotKnownList)

#Verifying if the whole secret word was guessed:
        if guessSoFar == secret_a_word:
            break
#The hangman is displayed according to the number of wrong guesses.
        display_hangman(num_wrong_guesses)


#If guessSoFar is not the secret word, 1 is added to the number of guesses, guessNumber, and the number of wrong guesses.
#In addition, the hangman is displayed according to the number of wrong guesses.
    else:
        guessNumber +=1
        num_wrong_guesses +=1
        
        display_hangman(num_wrong_guesses)
        
#is_game_over is called with the number of wrong guesess.
is_game_over(num_wrong_guesses)



def play_hangman():
    while not is_game_over:

        if __name__ == "__main__":
            play_hangman()
