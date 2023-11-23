# the list "meals" is already defined
# your code here

end = 0
for m in meals:
    erg = int(m.get("kcal"))
    end += erg
print(end)
