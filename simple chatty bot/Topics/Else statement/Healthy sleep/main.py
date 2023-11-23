A = int(input())
B = int(input())
H = int(input())

if A <= H <= B:
    print("Normal")
if H > B and H > A:
    print("Excess")
if H < A and H < B:
    print("Deficiency")
