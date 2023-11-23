num = input()

my_list = [int(n) for n in num]
end_list = []
for x in range(0, len(my_list)-1):
    erg = (my_list[x] + my_list[x + 1]) / 2
    end_list.append(erg)

print(end_list)
