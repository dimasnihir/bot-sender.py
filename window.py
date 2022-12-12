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

root = Tk()
root.title('SpamBot')
root.geometry('1024x720')

t1 = Label(root, text='Enter yout text', fg='black')
t1.config(font=('Verdana',15))
t1.place(x=180,y=40)


timer = Label(root,text="00:00")
timer.config(font=('Verdana',30))
timer.place(x=190,y=600)



edit = Text(root)
edit.place(x=10,y=70, width=500,height=400)

button_start = Button(root, text = 'Start')
button_start.place(x=50,y=500,width=100,height=60)

button_stop = Button(root,text='Stop', command=start_timer)
button_stop.place(x=350,y=500,width=100,height=60)






