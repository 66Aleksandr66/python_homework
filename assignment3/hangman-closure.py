# Task 4
def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        result = ""
        for char in secret_word:
            if char in guesses:
                result+= char
            else:
                result+= "_"
        print(result)
        if "_" not in result:
            return True
        else:
            return False
    return hangman_closure

game = make_hangman(input("Enter your word: "))
while True:
    result = game(input("Enter your guess: "))
    if result:
        break
print("You've done!")
