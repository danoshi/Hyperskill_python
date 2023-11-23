# Don't download gutenberg corpus. Just import it
import nltk
number = int(input()) # a row number of a sentence in Gutenberg corpus
whitman = nltk.corpus.gutenberg.sents('whitman-leaves.txt')
print(whitman[number])
