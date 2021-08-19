def judge(num):
    try:
        if num % 2 == 0:
            return (num,"是偶数")
        else:
            return (num,"是奇数")
    except (TypeError, ValueError):
        pass

print(judge(20))