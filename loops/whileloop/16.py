# 10. Write a Python program that asks the user to guess a pre-defined secret
#  word (e.g., "python"). Provide feedback like "Incorrect, try again" if the 
# guess is wrong. When the user guesses correctly, print "Congratulations, you
#  guessed the word!" Allow the user to exit the program by typing "quit."

from wonderwords import RandomWord
generator = RandomWord()
#the upper code is used to generate a random word. Paila suru pip install wonderwords garne ani matra yo chalcha code.

ans='.'
while(ans.lower()!='exit'):
    word=generator.word()
    print(word)
    wordGuess=input("Guess a random word:") 
    if(wordGuess.lower()==word):
        print("Congratulations, you guessed the word")
    else:
        print("Incorrect, try again")
    ans=input("Enter 'exit' to stop or anything to continue:")

    