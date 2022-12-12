from tkinter import*
from datetime import datetime

temp=0
after_id=''
def tick():
    global temp,after_id
    after_id=root.after(1000,tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    timer.configure(text=(str(f_temp)))
    temp+=1
def start_timer():
    tick()

def stop_timer():
    root.after_cancel(after_id)


# <----------Window------------->
root = Tk()
root.title('SpamBot')
root.geometry('1264x720')
root.resizable(width=False,height=False)
root.image = PhotoImage(file=("pictures/backgraund.png"))
bg= Label(root, image=root.image)
bg.grid(row=0, column=0)


# <----------Top Name-------------->
t1 = Label(root, text='Enter yout text here:', fg='white', background='#2c2c2c')
t1.config(font=('Comic Sans MS',20))
t1.place(x=365,y=20)


# <----------Timer-------------->
timer = Label(root,text="00:00",fg="white",background='#2c2c2c')
timer.config(font=('Verdana',30))
timer.place(x=450,y=600)



# <----------Text edit-------------->
edit = Text(root)
edit.config(font=('Comic Sans MS',15),fg='white',background='#646363')
edit['border'] = 0
edit.place(x=265,y=75, width=500,height=400)


# <----------Button Start-------------->
button_start_images = PhotoImage(file=("pictures/button_start.png"))
button_start = Button(root, image=button_start_images)
button_start.config(background="#2c2c2c")
button_start["border"] = 0
button_start.place(x=314,y=500,width=100,height=60)


# <----------Button Stop-------------->
button_stop_images = PhotoImage(file=("pictures/button_stop.png"))
button_stop = Button(root,image=button_stop_images, command=start_timer)
button_stop.config(background="#2c2c2c")
button_stop["border"] = 0
button_stop.place(x=614,y=500,width=100,height=60)






