import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')
value = False
e1 = tk.Entry(window, show='*', font=('Arial', 14))
e2 = tk.Entry(window, show=None, font=('Arial', 14))


def changeText():
    global value
    global e1
    global e2
    if value == False:
        value = True
        e1 = e2
    else:
        value = False
        e1 = e1


# 在图形页面设定输入框控件entry放置

b1 = tk.Button(window, text="显示铭文", bg='red', width=12, height=1, command=changeText)

e1.pack()
b1.pack()
e2.pack()

window.mainloop()
