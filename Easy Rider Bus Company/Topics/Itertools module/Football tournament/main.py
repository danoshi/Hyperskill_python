# the variable 'teams' is already defined
import itertools

#teams = ['Best-ever', 'Not-so-good', 'Amateurs']

for t in itertools.combinations(teams, 2):
    print(t)
