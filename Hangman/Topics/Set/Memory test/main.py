numbers = input().split()
answers = input().split()

numbers_set = set(numbers)
answers_set = set(answers)

print(answers_set == numbers_set)
