N=0
while N <= 0.01:
    N = N + 0.001
    dayup = 1.0
    for i in range(365):
        if i % 7 in [5,6,0]:
            dayup = dayup
        else:
            dayup = dayup * (1 + N)
    print("{:.2f}".format(dayup))
