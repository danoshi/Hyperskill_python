def index():
    syn = float(input())
    if syn < 2:
        print("Analytic")
    elif 2 <= syn <= 3:
        print("Synthetic")
    else:
        print("Polysynthetic")


index()
