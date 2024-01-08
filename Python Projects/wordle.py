print("Welcome to wordle!")
word = input("Enter a five letter word to challenge").strip().upper()
for i in range(5):
    guess = input("\nguess the word").strip().upper()
    if word == guess:
        print("You got it right!!")
        break;
    else: 
        for l in range(5):
            if word[l] == guess[l]:
                print(word[l], end="")
            else:
                print(" ", end="")
print(f"The word is {word}")