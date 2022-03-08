#温度转换.py
TempStr = input("请输入带有F或是C的温度值:")
if TempStr[-1] in ['f','F']:
    C=(eval(TempStr[0:-1]) - 32) / 1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F=1.8*eval(TempStr[0:-1])
    print("转换厚度的温度是{:.2f}F".format(F))
else:
    print("您输入格式错误")