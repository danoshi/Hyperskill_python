num = int(input())
erg = 0
end_erg = 0.0

for _numbers in range(num):
    calc = int(input())
    erg = calc + erg

end_erg = erg / num
print(float(end_erg))
