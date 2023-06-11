def fun(num):
    num.append(7)
    print("inside fun num: ", num)


num = [8]
fun(num)

print("outside fun num: ", num)
