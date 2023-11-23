words = input()
length = len(words)
sliceStr = words[length::-1]
if sliceStr == words:
    print("Palindrome")
else:
    print("Not palindrome")
