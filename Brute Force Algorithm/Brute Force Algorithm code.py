text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

found = False

for i in range(len(text) - len(pattern) + 1):
    j = 0

    while j < len(pattern) and text[i + j] == pattern[j]:
        j += 1

    if j == len(pattern):
        print("Pattern found at index", i)
        found = True

if not found:
    print("Pattern not found")
