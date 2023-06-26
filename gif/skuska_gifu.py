from tkinter import *
import time
import os
root = Tk()

frames = [PhotoImage(file='trava.gif',format = 'gif -index %i' %(i)) for i in range(3)]
print(frames)
def update(ktory):
    frame = frames[ktory]
    ktory += 1
    label.configure(image=frame)
    if ktory ==3:
        ktory =0
    root.after(500, update,ktory)
label = Label(root)
label.pack()
root.after(500, update,0)
root.mainloop()
