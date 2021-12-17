############################################### METADATA ################################################
"""

Github :-
https://github.com/Vanshaj712/Pronounceller

reference:-
http://enquiry.pronounceller@gmail.com

Copyright (c)
all rights reserved

"""





import io
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as sct
import Apis.PDF_Speech_Reader_API
import pygame
import ctypes
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk
from Apis.PDF_Speech_Reader_API import *
import Apis.PDF_Speech_Reader_API as pd
import random as rd
import googletrans
import Apis.tts as t
import pygame.mixer as m

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(3)

except EXCEPTION as ex:

    pass

__version__ = '0.1.0'

__features = ['Text to speech', 'One language to other translation', 'Reading a PDF']


def sel_tts():
    notebook.select(tb2)


def sel_trans():
    notebook.select(tab3)


def sel_pdf():
    notebook.select(tb4)


def home():
    notebook.select(tab1)


def say():
    m.init()
    t.say(text=lb2.get('1.0', 'end-1c'))
    t.play()


def setvol(*args):
    m.init()
    m.music.set_volume(sc.get())


def stp():
    t.delete()


def event():
    global root

    if os.path.exists(t.file):
        t.delete()
        root.destroy()
    else:
        root.destroy()


def trans_fnc(*args):
    tr = googletrans.Translator()
    data = str(txt.get('1.0', 'end-1c'))
    try:

        a = tr.translate(data, src=tv1.get(), dest=tv6.get())
        txt1['state'] = 'normal'
        txt1.delete(1.0, tk.END)
        txt1.insert(1.0, a.text)
        txt1['state'] = 'disabled'
    except Exception as er:
        print(er)


def exp():

    _file = asksaveasfilename(parent=root, initialfile='transcript.txt', defaultextension=".txt"
                              , filetypes=[("All Files", "*.*"),
                                           ("Text Documents", "*.txt")])
    if _file:
        _file = io.open(_file, 'w', encoding='utf-8')
        _file.write(txt1.get(1.0, END))
        _file.close()


def audio():
    save_as_audio(tv9.get())


def files():
    global file

    try:
        file = filedialog.askopenfilename(defaultextension=".pdf",
                                          filetypes=[("PDF files", "*.pdf")])

        if file is None:
            tv12.set('Open a PDF to read')
        recog(file)
        tv8.set(recog.pdf.getNumPages())
        tv12.set(file)


    except Exception:
        pass

def sel_fol():
    pd.fol = filedialog.askdirectory(title='Select Folder for saving Audio')


def red():
    starter.setProperty('rate', 160)
    read_selected_page(tv9.get())


def ter():
    Apis.PDF_Speech_Reader_API.starter.stop()


if __name__ == '__main__':

    pixel = 37.7953
    screen_length = 19.4 * pixel
    screen_width = 15 * pixel
    file1 = None

    root = Tk()
    root.geometry('800x640+10+10')
    root.resizable(False, False)
    root.title('Pronounceller')
    root.config(bg='white')
    root.iconbitmap(r"icon1.ico")

    style = ttk.Style()
    style.layout('TNotebook.Tab', [])

    notebook = ttk.Notebook(root, width=700, height=10)
    ttk.Style().configure('Tnotebook')
    tab1 = Frame(notebook, bg='')
    notebook.add(tab1)
    tb2 = ttk.Frame(notebook)
    notebook.add(tb2)
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3)
    notebook.pack(expand=True, fill=tk.BOTH)
    tb4 = ttk.Frame(notebook)
    notebook.add(tb4)
    tb5 = ttk.Frame(notebook)
    notebook.add(tb5)
    # tb6 = ttk.Frame(notebook)
    # notebook.add(tb6, text='Pro Coins')
    notebook.select(tab1)

    bg_path = ["statics\hmc1.jpeg"
        , "statics\hm2.jpg"
        , "statics\hm7.jpg"
        , "statics\hm10.jpg"
        , "statics\hm11.jpg"
        , "statics\hm12.jpg"
        , "statics\hm13.jpeg"]

    interface_bg = [r"statics\blur-background-6z-1280x720.jpg"
        , r"statics\i01_images.jpeg"
        , r"statics\abstract-blur-background-vector.jpg"
        , r"statics\clean-clean-background-blur-background.jpg"]

    image = r''
    shuffle = rd.randint(1, 7)

    if shuffle == 1:
        image = bg_path[0]
    elif shuffle == 2:
        image = bg_path[1]
    elif shuffle == 3:
        image = bg_path[2]
    elif shuffle == 4:
        image = bg_path[3]
    elif shuffle == 5:
        image = bg_path[4]
    elif shuffle == 6:
        image = bg_path[5]
    else:
        image = bg_path[6]

    bg_img = Image.open(image)
    images = ImageTk.PhotoImage(bg_img)
    bg = Label(tab1, image=images, height=2 * screen_width, width=screen_length)
    bg.pack(fill='both')

    tabs = Frame(tab1, bg='white', borderwidth=1, bd='10', highlightcolor='black')
    tabs.place(x=220, y=90,
               height=330, width=330)

    tit = Label(tabs, text='Available Tabs', font=('Arial', 20), bg='white')
    tit.place(x=8, y=5)

    tts = Button(tabs, text='Text To Speech', bg='#87CEEB', command=sel_tts, font=('Arial', 15))
    tts.place(x=60, y=80, height=50, width=200)

    sep1 = ttk.Separator(tabs, orient='horizontal').pack()

    trans = Button(tabs, text='Translator', command=sel_trans, bg='#2e8b57', font=('Arial', 15))
    trans.place(x=60, y=140, height=50, width=200)

    sep2 = ttk.Separator(tabs, orient='horizontal').pack()

    pdf = Button(tabs, text='PDF Reader', command=sel_pdf, bg='thistle1', font=('Arial', 15))
    pdf.place(x=60, y=200, height=50, width=200)

    bgim = Image.open(interface_bg[0])
    bgi = ImageTk.PhotoImage(bgim)
    pygame.init()
    back = Label(tb2, image=bgi)
    back.pack(fill='both')
    lb1 = Label(tb2, text='Text to speech ', font=("Bold", 25))
    tv = StringVar()
    lb1.place(x=280, y=0)

    stpim = Image.open(r"statics\images.jpg")
    stpi = ImageTk.PhotoImage(image=stpim)

    f1 = Frame(tb2, height=300, width=450)
    f1.config(bg='cyan2')
    f1.place(x=160, y=70)

    f2 = Frame(tb2, height=100, width=100)
    f2.config(bg='red')
    f2.place(x=640, y=410)

    lb2 = sct.ScrolledText(f1, font=('Arial', 15), height=7, width=37, padx=6, pady=5)
    lb2.place(x=10, y=20)
    lb2.insert(1.0, 'Enter Text Here..')

    tv4 = StringVar()
    tv5 = StringVar(value='Result:')
    tv2 = StringVar()
    root.protocol('WM_DELETE_WINDOW', event)

    b1 = Button(f1, text='Pronounce', command=say, font=('Arial', 15), bd=6, bg='coral1')
    b1.place(x=130, y=200, height=50, width=200)

    sep = ttk.Separator(tb2, orient='horizontal').pack()
    sep3 = ttk.Separator(tb2, orient='horizontal').pack()

    ext = lb2.get('1.0', 'end-1c')
    v1 = DoubleVar()
    v2 = StringVar()

    lab = Label(tb2, text='Set Volume:', font=("Arial", 15))
    lab.place(x=0, y=410)

    sc = Scale(tb2, variable=v1, from_=0.1, to=1.0, orient=VERTICAL, command=setvol, resolution=0.1)
    sc.place(x=150, y=410, )

    ret = Button(tb2, text='←', command=home, font=('Arial', 15))
    ret.place(x=0, y=0)

    m.init()

    var1 = StringVar(tb2, '1')

    tv3 = StringVar()

    but1 = Button(f2, image=stpi, command=stp)

    but1.pack()

    img1 = Image.open(interface_bg[1])
    image1 = ImageTk.PhotoImage(img1)
    bg1 = Label(tab3, image=image1)
    bg1.pack(fill='both')

    fol = None

    tv1 = StringVar()
    tv6 = StringVar()
    tv7 = StringVar(value='Result shown here')

    label = Label(tab3, text='TRANSLATOR', font=('Arial', 20))
    label.place(x=295, y=0)

    ret1 = Button(tab3, text='←', command=home, font=('Arial', 15))
    ret1.place(x=0, y=0)

    txt = sct.ScrolledText(tab3, font=('Arial', 15), height=10, width=50, padx=6, pady=5)
    txt.insert(1.0, 'Enter Text To Translate')
    txt.place(x=110, y=42)

    but1 = Button(tab3, text='Translate', command=trans_fnc, font=('Arial', 15), padx=1, pady=1, bd=4)
    but1.place(x=280, y=345, height=50, width=200)

    txt3 = Label(tab3, text='From', font=('Arial', 19))
    txt.place(x=110, y=42)

    com = Entry(tab3, textvariable=tv1, font=('Arial', 12))
    com.place(x=120, y=330 - 30, height=30)
    txt3.place(x=30, y=330 - 30)

    txt2 = Label(tab3, text='TO', font=('Arial', 19))
    com2 = Entry(tab3, textvariable=tv6, font=('Arial', 12))

    com2.place(x=560, y=330 - 30, height=30)
    txt2.place(x=490, y=330 - 30)

    b2 = Button(tab3, text='Export', command=exp, font=('Arial', 15), bd=3)
    b2.place(x=700, y=350, height=60)

    txt1 = sct.ScrolledText(tab3, font=('Arial', 15), height=9, width=50)
    txt1.place(x=115, y=410)
    txt1.insert(1.0, 'Result shown here')
    txt1['state'] = 'disabled'

    mg2 = Image.open(interface_bg[2])
    image2 = ImageTk.PhotoImage(mg2)
    bg2 = Label(tb4, image=image2)
    bg2.pack(fill='both')

    file = None

    tv8 = StringVar(value='Number of Pages')
    tv9 = IntVar()
    tv10 = IntVar()
    tv11 = DoubleVar()
    tv12 = StringVar(value='Path shown here')
    tv13 = StringVar()
    ret1 = Button(tb4, text='←', command=home, font=('Arial', 15))
    ret1.place(x=0, y=0)

    lab1 = ttk.Label(tb4, text='PDF READER', font=('Arial', 20))
    lab1.place(x=290, y=0)

    lab4 = ttk.Label(tb4, textvariable=tv12, font=('Arial', 20))
    lab4.place(x=265, y=120)

    but1 = Button(tb4, text='Open PDF', command=files, font=('Arial', 15))
    but1.place(x=280 + 10, y=250 - 40, height=50, width=200)

    lab5 = Label(tb4, textvariable=tv8, font=('Arial', 15))
    lab5.place(x=30, y=330 - 30)

    ent2 = Entry(tb4, textvariable=tv9, font=('Arial', 15))
    ent2.place(x=400, y=330 - 30)

    but2 = Button(tb4, text='Set Pages To read', command=red)
    but2.place(x=650, y=300)

    ch = Button(tb4, text='Save audio', height=5, width=15, command=audio,
                font=('Arial', 15))
    ch.place(x=300, y=380)

    but3 = Button(tb4,text='Select Folder',command=sel_fol,height=2,width=10,font=('Arial',16))
    but3.place(x=650,y=420)

    image3 = Image.open(interface_bg[3])
    img3 = ImageTk.PhotoImage(image3)
    bg3 = Label(tb5, image=img3)
    bg3.pack(fill='both')

    lab7 = Label(tb5, text='This Feature would be available soon...', font=('Arial', 20))
    lab8 = Label(tb5, text=r'For more information mail us to - enquiry.pronounceller@gmail.com', font=('Arial', 10))
    lab7.place(x=150, y=200)
    lab8.place(x=170, y=450)
    root.mainloop()
