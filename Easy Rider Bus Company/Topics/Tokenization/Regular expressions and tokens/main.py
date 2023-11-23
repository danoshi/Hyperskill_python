from nltk.tokenize import regexp_tokenize

sentence = input()
#sentence = "The more you read, the more you learn."
print(regexp_tokenize(sentence, "[A-z'-]+"))


