up = 1.0
dayfactor = 0.01
for i in range(365):#计次循环365次
    if i % 7 in [6, 0]:#判断是否为7天内的某两天
        up = up * (1-dayfactor)#计算向下值
    else:#否则
        up = up * (1+dayfactor)#计算向上值
print("工作日的力量：{:.2f}".format(up))#打印当前up的值