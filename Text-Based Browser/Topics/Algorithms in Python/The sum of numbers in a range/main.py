def range_sum(numbers, start, end):
    res = 0
    for n in numbers:
        if start <= n <= end:
            res += n
    return res


input_numbers = list(map(int, input().split()))
a, b = list(map(int, input().split()))

print(range_sum(input_numbers, a, b))
