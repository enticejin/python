f = open(R"D:\work\pointinfo_solve.csv")
#f = open("D:/work/pointinfo_solve.csv")
#print(f.read())

with open("D:/work/pointinfo_solve.csv") as x:
    x_read = x.read()
    print(x_read)
x.close()
