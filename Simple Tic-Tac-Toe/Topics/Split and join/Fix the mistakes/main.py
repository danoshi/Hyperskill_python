text = input()
words = text.split()
for word in words:
    # finish the code here
    if word.startswith(("https://", "http://", "www.", "WWW.")):
        print(word)
