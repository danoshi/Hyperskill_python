# put your code here

num = int(input())
i = 0
sum_input = 0
avg_input = 0
break_var = 55

while num != break_var:
    if num == break_var:
        break
    else:
        sum_input += num
        i += 1
        num = int(input())


avg_input += round(sum_input / i)
print(i)
print(sum_input)
print(avg_input)
