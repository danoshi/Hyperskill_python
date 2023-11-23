word = input().split()
alp = []
for words in word:
    if words.endswith("s"):
        alp.append(words)
print("_".join(alp))
