from tkinter import *

velocity = 0
run = True
window = Tk()
window.title("Enter value")
window.geometry("200x80")
window.resizable(width=0 , height=0)
label = Label(window)
entry = Entry(window)
entry.place(y=25,x=75 , width=100 , height=30)

def confirm():
     global velocity
     global run
     value = int(entry.get())
     velocity = value
     window.destroy()
     run = False
     

def main():
     confirm_button = Button(window , text="Confirm" , width=6 , height=3 , command=confirm)
     confirm_button.pack()
     confirm_button.place(x=2,y=14)
     label.configure(text="Enter the snake velocity : ")
     label.place(x=60,y=8)
     window.mainloop()
