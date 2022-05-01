from math import sqrt
def getNum(): #获取用户输入
    nums = []
    iNumStr = input("输入数字（回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("输入数字（回车退出）：")
    return nums

def mean(numbers): #计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers, mean): #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return sqrt(sdev / (len(numbers)-1))

def median(numbers): #计算中位数
    new = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (new[size//2-1] + new[size//2])/2
    else:
        med = new[size//2]
    return med

def max(numbers): #求最大值
    max = numbers[0]
    for i in numbers:
        if i > max: max = i
    return max

def min(numbers): #求最小值
    min = numbers[0]
    for i in numbers:
        if i < min: min = i
    return min

n = getNum()  #主体函数
m = mean(n)
print("平均值:{},标准差:{:.2f}, 中位数:{},最大值:{}, 最小值:{}".format(m, dev(n, m), median(n),max(n), min(n)))


