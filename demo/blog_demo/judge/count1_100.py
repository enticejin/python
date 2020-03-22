# 计算1加到100的和
sum1, num1, num2 = 0, 0, 100
while num1 <= num2:
    sum1 = num1 + sum1
    # num1 = num1 + 1
    num1 += 1
else:
    num1 = 0
    print("%s到%s的和是： %s" % (num1, num2, sum1))
