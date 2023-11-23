# Write your code here
game_name = "H A N G M A N"
print(game_name, sep='\n')
hidden_word = "python"
word = input("Guess the word: ")

if word == hidden_word:
    print("You survived!")
else:
    print("You lost!")
