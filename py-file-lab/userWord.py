wordWithoutVovels = ""
userWord=input("Enter a word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter in "AIUEO":
        continue
    else:
        wordWithoutVovels += letter

print(wordWithoutVovels)