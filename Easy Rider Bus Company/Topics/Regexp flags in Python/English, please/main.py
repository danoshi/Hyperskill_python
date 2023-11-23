import re

sentence = input()
pattern = r'(means|Hello|and|is|See|you|China|England|the|USA)'
result = re.findall(pattern, sentence, flags=re.IGNORECASE)

print(result)
