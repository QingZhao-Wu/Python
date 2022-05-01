def dayUP(df):
    up = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            up = up * (1 - 0.01)
        else:
            up = up * (1 + df)
    return up
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))