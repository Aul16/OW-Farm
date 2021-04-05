import os
try:
    import pyautogui as pa
    import time
    import tkinter as tk
    from tkinter import *
except:
    os.system('pip install pyautogui')
    os.system('pip install tkinter')
    import pyautogui as pa
    import time
    import tkinter as tk
    from tkinter import *


running = False
idx = 0  # loop index

def start():
    """Enable scanning by setting the global flag to True."""
    btnStart.config(state=DISABLED)
    btnStop.config(state=NORMAL)
    global running
    running = True

def stop():
    """Stop scanning by setting the global flag to False."""
    btnStop.config(state=DISABLED)
    btnStart.config(state=NORMAL)
    global running
    running = False


root = Tk()
root.title("OWFarm")

window_height = 140
window_width = 310

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry("{}x{}".format(window_width, window_height))

app = Frame(root)
app.grid()

btnStart = Button(app, padx=150, text="START", bg='green', command= lambda: start())
btnStop = Button(app, padx=150, text="STOP", bg='red', command= lambda: stop())

btnStart.pack()
btnStop.pack(side=BOTTOM)

btnStart.config(height=4, width=1)
btnStop.config(height=4, width=1, state=DISABLED)

while True:
    if idx % 500 == 0:
        root.update()

    if running:
        pa.keyDown('s')
        pa.press('a')
        time.sleep(.500)
