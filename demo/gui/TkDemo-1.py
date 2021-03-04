# 使用GUI引入tkinter
import tkinter as tk

# 实例化object  建立窗口window
window = tk.Tk()

# 给可视化窗口起名字
window.title('这个窗体')

# 设定窗口大小(长*宽)
window.geometry('500x300')  # 这里的乘是小x
# 自定义标签值
var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
# 在图形界面设定标签
l = tk.Label(window, textvariable=var, bg='red', font=('Arial', 12), width=30, height=2)
l.pack()
# 默认不点击
on_hit = False

# 定义方法
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('你点击了我')
    else:
        on_hit = False
        var.set('')


b = tk.Button(window, text="点击我", bg='green', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()
# 主窗口循环显示
window.mainloop()
