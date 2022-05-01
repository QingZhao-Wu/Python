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
