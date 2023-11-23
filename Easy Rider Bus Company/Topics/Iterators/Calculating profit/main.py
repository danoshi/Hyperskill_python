# costs = [5000]
# revenues = [1000]
# months = ['Jan']

res = []
for rev, cost in zip(revenues, costs):
    erg = rev - cost
    res.append(erg)

for month, erg in zip(months, res):
    print(month, erg)
