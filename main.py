import tkinter
from PIL import Image, ImageTk
import webbrowser
import random

def thing():
    for i in range(50):
        w = tkinter.Toplevel()
        app(w)
    w.protocol("WM_DELETE_WINDOW", lambda: thing())
    w.mainloop()

def app(w):
    global thing
    def thing2(w):
        thing()
        w.destroy()
    w.title('CONGRATULATIONS!')
    w.resizable(0, 0)
    label1 = tkinter.Label(text="Congratulations, you are our lucky winner!")
    label1.grid(row=0, column=0, columnspan=4)
    load = Image.open("carp1.png")
    render = ImageTk.PhotoImage(load)
    img = tkinter.Label(w, image=render, cursor="heart")
    img.image = render
    img.grid(row=1, column=0, columnspan=4)
    link1 = tkinter.Label(w, text=str(bin(random.randint(2**50, 2**51))[2:]), fg="blue", cursor="hand2")
    link1.grid(row=2, column=0, columnspan=4)
    link1.bind("<Button-1>", lambda e: webbrowser.open_new("https://puginarug.com"))
    b1 = tkinter.Button(w, text='View Black Crime Statistics', command=lambda: webbrowser.open_new("https://www.ojjdp.gov/ojstatbb/crime/ucr.asp?table_in=2&selYrs=2019&rdoGroups=1&rdoData=c&export=yes"))
    b2 = tkinter.Button(w, text='Ok', command=lambda: thing2(w))
    b1.grid(row=4, column = 0, columnspan=3, sticky=tkinter.NSEW)
    b2.grid(row=4, column=3, sticky=tkinter.NSEW)
    

w = tkinter.Tk()
app(w)
w.protocol("WM_DELETE_WINDOW", lambda: thing())
w.mainloop()

