from tkinter import*


root = Tk()
root.title('SpamBot')
root.geometry('1024x720')

t1 = Label(root, text='Enter yout text', fg='black')
t1.config(font=('Verdana',15))
t1.place(x=170,y=40)



edit = Text(root)
edit.place(x=10,y=70, width=500,height=400)

button_start = Button(root, text = 'Start')
button_start.place(x=50,y=500,width=100,height=60)

button_stop = Button(root,text='Stop')
button_stop.place(x=350,y=500,width=100,height=60)




root.mainloop()

