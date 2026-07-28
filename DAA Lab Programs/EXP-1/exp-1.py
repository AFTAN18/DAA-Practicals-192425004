words = input("Enter words separated by space: ").split()

for word in words:
    if word == word[::-1]:
        print(word)
        break
else:
    print("")
