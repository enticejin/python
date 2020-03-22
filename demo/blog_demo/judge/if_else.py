# 猜数字游戏
number = 20
guess = -1
while guess != number:
    guess = float(input("输入你心里想的数字"))
    if guess == number:
        print("猜对了！！Game over")
        break
    elif guess < number:
        print("小了，小了！！")
        continue
    elif guess > number:
        print("大了大了")
        continue
