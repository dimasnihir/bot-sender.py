from tkinter import*
from datetime import datetime

temp = 0
after_id = ''
def tick():
    global temp,after_id
    after_id = root.after(1000,tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    timer.configure(text = (str(f_temp)))
    temp+=1
def start_timer():
    tick()
def stop_timer():
    root.after_cancel(after_id)


# <----------Window------------->
root = Tk()
root.title('SpamBot')
root.geometry('1264x720')
root.resizable(width=False, height=False)
root.image = PhotoImage(file=("pictures/backgraund.png"))
bg = Label(root, image=root.image)
bg.grid(row=0, column=0)


# <----------Top Name-------------->
t1 = Label(root, text='Enter yout text here:', fg='white', background='#2c2c2c')
t1.config(font=('Comic Sans MS', 20))
t1.place(x=365, y=20)


# <----------Timer-------------->
timer = Label(root, text="00:00", fg="white", background='#2c2c2c')
timer.config(font=('Verdana', 30))
timer.place(x=450, y=500)


# <----------Text edit-------------->
edit = Text(root)
edit.config(font=('Comic Sans MS', 15), fg='white', background='#646363')
edit['border'] = 0
edit.place(x=265, y=75, width=500, height=400)


# <----------Button Start-------------->
button_start_images = PhotoImage(file=("pictures/button_start.png"))
button_start = Button(root, image=button_start_images, command=start_timer)
button_start.config(background="#2c2c2c", activebackground="#2c2c2c")
button_start["border"] = 0
button_start.place(x=314, y=500, width=100, height=60)


# <----------Button Stop-------------->
button_stop_images = PhotoImage(file=("pictures/button_stop.png"))
button_stop = Button(root, image=button_stop_images, command=stop_timer)
button_stop.config(background="#2c2c2c", activebackground="#2c2c2c")
button_stop["border"] = 0
button_stop.place(x=614, y=500, width=100, height=60)


# <----------Status massages-------------->
status_massages_true = Label(root, text="Successfully sent: 123")
status_massages_true.config(font=('Georgia', 15), fg="#6ec261", background='#2c2c2c')
status_massages_true.place(x=314, y=640)
status_massages_false = Label(root, text = "Failed sent: 32")
status_massages_false.config(font = ('Georgia', 15), fg="red", background='#2c2c2c')
status_massages_false.place(x=314, y=680)


# <----------View ancket-------------->
quantity_anket = 2
count = 0
coordinate_y = 6
Name_ankets = ["Sirena","Anjelika"]
if quantity_anket > 0:
    for i in range(quantity_anket):
        bd_color = Frame(root, highlightbackground="#6ec261", highlightthickness=2, bd=0)
        view_ankets = Button(bd_color, text=str(Name_ankets[int(count)]), background="#646363", activebackground="#646363")
        view_ankets.config(font=('Comic Sans MS', 15), fg='white')
        view_ankets.place(width=220, height=60)
        bd_color.place(x=7, y=coordinate_y, width=224, height=64)
        coordinate_y += 70
        count += 1


# <----------View men online-------------->
man_online = Label(root, text="Men Online: 129")
man_online.config(font=('Georgia', 15), fg="#6ec261", background='#2c2c2c')
man_online.place(x=15, y=640)


# <----------View balance-------------->
view_balance = Label(root, text="Balance: 99$")
view_balance.config(font=('Comic Sans MS', 15), fg="#6ec261", background='#2c2c2c')
view_balance.place(x=15, y=680)


# <----------Logi-------------->
logi_text_lable = Text(root)
logi_text_lable.config(font=('Comic Sans MS', 15), fg='white', background='#646363')
logi_text_lable['border'] = 0
logi_text_lable.place(x=800, y=10, width=455, height=700)
