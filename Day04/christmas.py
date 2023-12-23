while(True):
    word = input("What is the word: ")
    total = 0
    for letter in word:
        total = ord(letter)
    total = total / len(word)
    print(f"Total = {total}\n")