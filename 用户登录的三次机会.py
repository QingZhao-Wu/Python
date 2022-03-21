sum = 0
while True:
    account = input()
    password = eval(input())
    if account == "Kate" and password == 666666:
        print("登录成功！")
        break
    else:
        sum += 1
        if sum == 3:
            print("3次用户名或者密码均有误！退出程序。")
            break