from tkinter import *
from tkinter.ttk import Progressbar
import time


def step():
    for i in range(5):
        app.update_idletasks()
        pb['value'] += 20
        time.sleep(1)
        txt['text']=pb['value'],'%'

app = Tk()
app.title('ProgressBar - MustafaXD')
app.geometry('200x150')
app.config(bg='#000000')


pb = Progressbar(
    app,
    orient = HORIZONTAL,
    length = 100,
    mode = 'determinate'
    )

pb.place(x=40, y=20)

txt = Label(
    app,
    text = '0%',
    bg = '#345',
    fg = '#fff'

)

txt.place(x=150 ,y=20 )

Button(
    app,
    text='Start',
    command=step
).place(x=40, y=50)

app.mainloop()
