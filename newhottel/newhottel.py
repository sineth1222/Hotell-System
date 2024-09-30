from tkinter import *
from tkinter import ttk
import PIL
import os
from PIL import Image, ImageTk



APP = Tk()
APP.geometry("500x720")


def menu():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    MENU1 = Menu()
    APP.config(menu=MENU1)


    submenu1 = Menu()

    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='____________________________________________________')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='____________________________________________________')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label="                            Home                                                ",command=menu)
    submenu1.add_command()
    submenu1.add_command(label="                           Setting                                                 ",command=setting)
    submenu1.add_command()
    submenu1.add_command(label='                         Notification',command=notification)
    submenu1.add_command()
    submenu1.add_command(label='                           About')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='Developer - sinethbethie python vertion')
    submenu1.add_command(label='3.00.0 app vertion 27.0.0 helping pycharm ')
    submenu1.add_command(label='           ______ app 1.0.52.|| ______ ')


    MENU1.add_cascade(label='___________________________________________________________________________________________________')
    MENU1.add_cascade(label='                                                             ')
    MENU1.add_cascade(label="                                      Menu                                                ",menu=submenu1)
    MENU1.add_cascade(label='___________________________________________________________________________________________________')

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Prawns Pride',command=prawnsp, fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=150)
    Label(mainF,text='RS 500.00' , fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Prawns Pride',fg = '#524F4E', bg = 'white', font = ('SimSun', 12, 'bold')).place(width=140, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=305)

    Button(mainF, text='Prawns Devil',command=prawnsd, fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=150)
    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Prawns Devil', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>',command=next1, fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='Bites', fg='white', bg='#EF930C', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Biryani',command=burimenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Rice', fg='white',command=ricemenu, bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>',command=nextmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.' ,fg='#524F4E', bg='white').place(width=500, height=15, y=695)


def next1():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f13.jpg").resize((200, 200)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f17.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Rose Chicken', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=150)
    Label(mainF,text='RS 800.00' , fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Rose Chicken',fg = '#524F4E', bg = 'white', font = ('SimSun', 12, 'bold')).place(width=140, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=305)

    Button(mainF, text='Chicken Devel', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=150)
    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Chicken Devel', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)
    Button(mainF, text='<<< Previous',command=menu, fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=560, height=30, width=100)

    Button(mainF, text='Bites', fg='white', bg='#EF930C', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Biryani',command=burimenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Rice', fg='white',command=ricemenu, bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>',command=nextNext1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.' ,fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def nextNext1():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f13.jpg").resize((200, 200)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f17.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Rose Chicken',command=prawnsp, fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=150)
    Label(mainF,text='RS 800.00' , fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Rose Chicken',fg = '#524F4E', bg = 'white', font = ('SimSun', 12, 'bold')).place(width=140, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=305)

    Button(mainF, text='Chicken Devel', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=150)
    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=450, x=10)
    Label(mainF, text='Chicken Devel', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)
    Button(mainF, text='<<< Previous', command=menu, fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=560, height=30, width=100)

    Button(mainF, text='<< Previous',command=next1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Koththu',command=kottumenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Juice', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def nextmenu():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Prawns Pride',command=prawnsp, fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=150)
    Label(mainF,text='RS 500.00' , fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Prawns Pride',fg = '#524F4E', bg = 'white', font = ('SimSun', 12, 'bold')).place(width=140, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=305)

    Button(mainF, text='Prawns Devil', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=150)
    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=450, x=10)
    Label(mainF, text='Prawns Devil', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='<< Previous',command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Koththu',command=kottumenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Juice', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

#prawns pride

def prawnsp():

    global inp

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=320, x=10)
    Label(mainF, text='Prawns Pride', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+',command=incres1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='1', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00',command=cartpp, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def cartpp():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Pride', fg='#524F4E', bg='white', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 1 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 550.00 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=orderpp, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,
                                                                                             y=695)

def orderpp():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global name
    global addres
    global number
    global acnum
    global crdtyp
    global ncc
    global msg
    name = StringVar()
    addres = StringVar()
    number = StringVar()
    acnum = StringVar()
    ncc = StringVar()
    crdtyp = StringVar()

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=name, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=number, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=addres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=acnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='#524F4E', bg='white', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=ncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=crdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=410)

    msg = Label(mainF, bg='white', border=0)
    msg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=savepp, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def savepp():
    user = name.get()
    deliad = addres.get()
    delinum = number.get()
    userAc = acnum.get()
    userncc = ncc.get()
    usecrd = crdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if user == "" or deliad == "" or userAc=="" :
        msg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(user + '\n')
        userFile.write(deliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+delinum + '\n')
        userFile.write(userAc + '\n')
        userFile.write(userncc + '\n')
        userFile.write(usecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 1' + '\n')
        userFile.write('Total Price = RS 550.00' + '\n')
        userFile.close()

        msg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id))

    notification()

def incres1():

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Pride', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-',command=prawnsp, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=incres2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='2', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00',command=cartpp1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def cartpp1():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Pride', fg='#524F4E', bg='white', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 2 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 1050.00 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=orderpp1, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def orderpp1():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global name
    global addres
    global number
    global acnum
    global crdtyp
    global ncc
    global msg
    name = StringVar()
    addres = StringVar()
    number = StringVar()
    acnum = StringVar()
    ncc = StringVar()
    crdtyp = StringVar()

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=name, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=number, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=addres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=acnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='#524F4E', bg='white', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=ncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=crdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=410)

    msg = Label(mainF, bg='white', border=0)
    msg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=savepp1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def savepp1():
    user = name.get()
    deliad = addres.get()
    delinum = number.get()
    userAc = acnum.get()
    userncc = ncc.get()
    usecrd = crdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if user == "" or deliad == "" or userAc=="" :
        msg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(user + '\n')
        userFile.write(deliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+delinum + '\n')
        userFile.write(userAc + '\n')
        userFile.write(userncc + '\n')
        userFile.write(usecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 2' + '\n')
        userFile.write('Total Price = RS 1050.00' + '\n')
        userFile.close()

        msg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

def incres2():

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Pride', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', command=incres1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=incres3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='3', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00',command=cartpp2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def cartpp2():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Pride', fg='#524F4E', bg='white', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 3 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 1550.00 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=orderpp2, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def orderpp2():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global name
    global addres
    global number
    global acnum
    global crdtyp
    global ncc
    global msg
    name = StringVar()
    addres = StringVar()
    number = StringVar()
    acnum = StringVar()
    ncc = StringVar()
    crdtyp = StringVar()

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=name, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=number, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=addres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=acnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='#524F4E', bg='white', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=ncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=crdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=410)

    msg = Label(mainF, bg='white', border=0)
    msg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=savepp2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def savepp2():
    user = name.get()
    deliad = addres.get()
    delinum = number.get()
    userAc = acnum.get()
    userncc = ncc.get()
    usecrd = crdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if user == "" or deliad == "" or userAc=="" :
        msg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(user + '\n')
        userFile.write(deliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+delinum + '\n')
        userFile.write(userAc + '\n')
        userFile.write(userncc + '\n')
        userFile.write(usecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 3' + '\n')
        userFile.write('Total Price = RS 1550.00' + '\n')
        userFile.close()

        msg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

    notification()

def incres3():

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Pride', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', command=incres2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=incres4, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='4', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00',command=cartpp3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def cartpp3():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Pride', fg='#524F4E', bg='white', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 4 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 2050.00 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=orderpp3, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def orderpp3():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global name
    global addres
    global number
    global acnum
    global crdtyp
    global ncc
    global msg
    name = StringVar()
    addres = StringVar()
    number = StringVar()
    acnum = StringVar()
    ncc = StringVar()
    crdtyp = StringVar()

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=name, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=number, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=addres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=acnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='#524F4E', bg='white', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=ncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=crdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=410)

    msg = Label(mainF, bg='white', border=0)
    msg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=savepp3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def savepp3():
    user = name.get()
    deliad = addres.get()
    delinum = number.get()
    userAc = acnum.get()
    userncc = ncc.get()
    usecrd = crdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if user == "" or deliad == "" or userAc=="" :
        msg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(user + '\n')
        userFile.write(deliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+delinum + '\n')
        userFile.write(userAc + '\n')
        userFile.write(userncc + '\n')
        userFile.write(usecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 4' + '\n')
        userFile.write('Total Price = RS 2050.00' + '\n')
        userFile.close()

        msg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

    notification()

def incres4():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Pride', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', command=incres3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='5', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00',command=cartpp4, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def cartpp4():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Pride', fg='#524F4E', bg='white', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 5 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 2550.00 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=orderpp4, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def orderpp4():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global name
    global addres
    global number
    global acnum
    global crdtyp
    global ncc
    global msg
    name = StringVar()
    addres = StringVar()
    number = StringVar()
    acnum = StringVar()
    ncc = StringVar()
    crdtyp = StringVar()

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=name, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=number, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=addres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=acnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='#524F4E', bg='white', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=ncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=crdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=410)

    msg = Label(mainF, bg='white', border=0)
    msg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=savepp4, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def savepp4():
    user = name.get()
    deliad = addres.get()
    delinum = number.get()
    userAc = acnum.get()
    userncc = ncc.get()
    usecrd = crdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if user == "" or deliad == "" or userAc=="" :
        msg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(user + '\n')
        userFile.write(deliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+delinum + '\n')
        userFile.write(userAc + '\n')
        userFile.write(userncc + '\n')
        userFile.write(usecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 5' + '\n')
        userFile.write('Total Price = RS 2550.00' + '\n')
        userFile.close()

        msg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

    notification()

def incres5():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Pride', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', command=prawnsp, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=incres1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='2', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00',command=cartpp5, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)


 # Prawns Devil

def prawnsd():

    global inp

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=320, x=10)
    Label(mainF, text='Prawns Devil', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+',command=pdincres1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='1', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 400.00',command=pdcartpp, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def pdcartpp():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Devil', fg='#524F4E', bg='white', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 1 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 450.00 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=pdorderpp, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,
                                                                                             y=695)

def pdorderpp():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global name
    global addres
    global number
    global acnum
    global crdtyp
    global ncc
    global msg
    name = StringVar()
    addres = StringVar()
    number = StringVar()
    acnum = StringVar()
    ncc = StringVar()
    crdtyp = StringVar()

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=name, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=number, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=addres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=acnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='#524F4E', bg='white', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=ncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=crdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=410)

    msg = Label(mainF, bg='white', border=0)
    msg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=pdsavepp, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def pdsavepp():
    user = name.get()
    deliad = addres.get()
    delinum = number.get()
    userAc = acnum.get()
    userncc = ncc.get()
    usecrd = crdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if user == "" or deliad == "" or userAc=="" :
        msg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(user + '\n')
        userFile.write(deliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+delinum + '\n')
        userFile.write(userAc + '\n')
        userFile.write(userncc + '\n')
        userFile.write(usecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 1' + '\n')
        userFile.write('Total Price = RS 450.00' + '\n')
        userFile.close()

        msg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id))

    notification()

def pdincres1():

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Devil', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-',command=prawnsd, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=pdincres2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='2', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 400.00',command=pdcartpp1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def pdcartpp1():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Devil', fg='#524F4E', bg='white', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 2 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 850.00 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=pdorderpp1, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def pdorderpp1():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global name
    global addres
    global number
    global acnum
    global crdtyp
    global ncc
    global msg
    name = StringVar()
    addres = StringVar()
    number = StringVar()
    acnum = StringVar()
    ncc = StringVar()
    crdtyp = StringVar()

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=name, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=number, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=addres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=acnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='#524F4E', bg='white', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=ncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=crdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=410)

    msg = Label(mainF, bg='white', border=0)
    msg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=pdsavepp1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def pdsavepp1():
    user = name.get()
    deliad = addres.get()
    delinum = number.get()
    userAc = acnum.get()
    userncc = ncc.get()
    usecrd = crdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if user == "" or deliad == "" or userAc=="" :
        msg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(user + '\n')
        userFile.write(deliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+delinum + '\n')
        userFile.write(userAc + '\n')
        userFile.write(userncc + '\n')
        userFile.write(usecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 2' + '\n')
        userFile.write('Total Price = RS 850.00' + '\n')
        userFile.close()

        msg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

def pdincres2():

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Devil', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', command=pdincres1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=pdincres3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='3', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 400.00',command=pdcartpp2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def pdcartpp2():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Devil', fg='#524F4E', bg='white', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 3 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 1250.00 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=pdorderpp2, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def pdorderpp2():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global name
    global addres
    global number
    global acnum
    global crdtyp
    global ncc
    global msg
    name = StringVar()
    addres = StringVar()
    number = StringVar()
    acnum = StringVar()
    ncc = StringVar()
    crdtyp = StringVar()

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=name, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=number, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=addres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=acnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='#524F4E', bg='white', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=ncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=crdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=410)

    msg = Label(mainF, bg='white', border=0)
    msg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=pdsavepp2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def pdsavepp2():
    user = name.get()
    deliad = addres.get()
    delinum = number.get()
    userAc = acnum.get()
    userncc = ncc.get()
    usecrd = crdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if user == "" or deliad == "" or userAc=="" :
        msg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(user + '\n')
        userFile.write(deliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+delinum + '\n')
        userFile.write(userAc + '\n')
        userFile.write(userncc + '\n')
        userFile.write(usecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 3' + '\n')
        userFile.write('Total Price = RS 1550.00' + '\n')
        userFile.close()

        msg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

    notification()

def pdincres3():

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Devil', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', command=pdincres2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=pdincres4, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='4', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 400.00',command=pdcartpp3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def pdcartpp3():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Devil', fg='#524F4E', bg='white', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 4 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 1650.00 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=pdorderpp3, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def pdorderpp3():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global name
    global addres
    global number
    global acnum
    global crdtyp
    global ncc
    global msg
    name = StringVar()
    addres = StringVar()
    number = StringVar()
    acnum = StringVar()
    ncc = StringVar()
    crdtyp = StringVar()

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=name, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=number, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=addres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=acnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='#524F4E', bg='white', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=ncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=crdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=410)

    msg = Label(mainF, bg='white', border=0)
    msg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=pdsavepp3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def pdsavepp3():
    user = name.get()
    deliad = addres.get()
    delinum = number.get()
    userAc = acnum.get()
    userncc = ncc.get()
    usecrd = crdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if user == "" or deliad == "" or userAc=="" :
        msg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(user + '\n')
        userFile.write(deliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+delinum + '\n')
        userFile.write(userAc + '\n')
        userFile.write(userncc + '\n')
        userFile.write(usecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 4' + '\n')
        userFile.write('Total Price = RS 2050.00' + '\n')
        userFile.close()

        msg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

    notification()

def pdincres4():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Devil', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', command=pdincres3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='5', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 400.00',command=pdcartpp4, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def pdcartpp4():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Devil', fg='#524F4E', bg='white', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='#524F4E', bg='white', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 5 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 2050.00 ', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=pdorderpp4, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15,y=695)

def pdorderpp4():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global name
    global addres
    global number
    global acnum
    global crdtyp
    global ncc
    global msg
    name = StringVar()
    addres = StringVar()
    number = StringVar()
    acnum = StringVar()
    ncc = StringVar()
    crdtyp = StringVar()

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=name, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=number, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=addres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=acnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='#524F4E', bg='white', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=ncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=crdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=410)

    msg = Label(mainF, bg='white', border=0)
    msg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=pdsavepp4, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)

def pdsavepp4():
    user = name.get()
    deliad = addres.get()
    delinum = number.get()
    userAc = acnum.get()
    userncc = ncc.get()
    usecrd = crdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if user == "" or deliad == "" or userAc=="" :
        msg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(user + '\n')
        userFile.write(deliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+delinum + '\n')
        userFile.write(userAc + '\n')
        userFile.write(userncc + '\n')
        userFile.write(usecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 5' + '\n')
        userFile.write('Total Price = RS 2550.00' + '\n')
        userFile.close()

        msg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

    notification()

def pdincres5():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Devil', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', command=pdprawnsp, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=pdincres1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='2', fg='#524F4E', bg='white', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 400.00',command=pdcartpp5, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)



def burimenu():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f20.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f16.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Special Biryani', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=170)
    Label(mainF,text='RS 500.00' , fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Special Biryani',fg = '#524F4E', bg = 'white', font = ('SimSun', 12, 'bold')).place(width=160, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=305)

    Button(mainF, text='Mango Sawan', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Mango Sawan', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='Bites',command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Biryani', fg='white', bg='#EF930C', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Rice',command=ricemenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', command=burinextmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)
def burinextmenu():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f20.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f16.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)

    Button(mainF, text='Special Biryani', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=90, height=50, width=170)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=220, x=10)
    Label(mainF, text='Special Biryani', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=160,height=20, y=240,x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=305)

    Button(mainF, text='Mango Sawan', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Mango Sawan', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=490, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='<< Previous',command=burimenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Koththu',command=kottumenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Juice', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)


def ricemenu():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f15.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f21.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Vegitable Rice', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=170)
    Label(mainF,text='RS 300.00' , fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Vegitable Rice',fg = '#524F4E', bg = 'white', font = ('SimSun', 12, 'bold')).place(width=160, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=305)

    Button(mainF, text='Chicken Rice', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Chicken Rice', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='Bites',command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Biryani',command=burimenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Rice', fg='white', bg='#EF930C', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', command=ricenextmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)
def ricenextmenu():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f15.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f21.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)

    Button(mainF, text='Vegitable Rice', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=90, height=50, width=170)
    Label(mainF, text='RS 300.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=220, x=10)
    Label(mainF, text='Vegitable Rice', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=160,height=20, y=240,x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=305)

    Button(mainF, text='Chicken Rice', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Chicken Rice', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=490, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='<< Previous',command=ricemenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Koththu',command=kottumenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Juice', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)


def kottumenu():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f8.jpeg").resize((200, 200)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f12.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Chicken Kottu', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=170)
    Label(mainF,text='RS 300.00' , fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Chicken Kottu',fg = '#524F4E', bg = 'white', font = ('SimSun', 12, 'bold')).place(width=160, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=305)

    Button(mainF, text='Mix Kottu', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Mix Kottu', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='<< Previous', command=kottunextmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Koththu', fg='white', bg='#EF930C', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Juice', fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)


    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)
def kottunextmenu():
    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f8.jpeg").resize((200, 200)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f12.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)

    Button(mainF, text='Chicken Kottu', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=90, height=50, width=170)
    Label(mainF, text='RS 300.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=220, x=10)
    Label(mainF, text='Chicken Kottu', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=160,height=20, y=240,x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=305)

    Button(mainF, text='Mix Kottu', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Mix Kottu', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=490, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='Bites', command=menu, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Biryani', command=burimenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Rice', command=ricemenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>',command=kottumenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='#524F4E', bg='white').place(width=500, height=15, y=695)



def setting():
    global msg

    mainF = Frame(APP, bg='white')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("s2.png").resize((75, 75)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=75, width=75, x=190, y=80)

    img = ImageTk.PhotoImage(Image.open("d7.jpg").resize((50, 50)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=50, width=50, x=30, y=270)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Setting', fg='#524F4E', bg='white', font=('SimSun', 15, 'bold')).place(width=120, height=20,y=185, x=170)




    btn1 = Button(mainF, text='ON',command=nightON, fg='black', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('Consolas', 10, 'bold'))#.place(x=300, y=50, height=50, width=50)
    btn1.place(x=300, y=270, height=50, width=50)
    btn2 = Button(mainF, text='OFF', command=nightoff, fg='black', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 10, 'bold'))  # .place(x=300, y=50, height=50, width=50)
    btn2.place(x=360, y=270, height=50, width=50)
    Label(mainF, text='Night Mode', bg='white', fg='black', font=('Consolas', 10, 'bold')).place(x=100, y=270, height=50, width=100)
    Button(mainF, text='Back',command=back, fg='black', bg='white', border=0, font=('Consolas', 10, 'bold')).place(x=50, y=500, height=50, width=200)
    #Button(mainF, text='Exit', fg='black', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('Consolas', 10, 'bold')).place(x=150, y=230, height=50, width=200)
    #Button(mainF, text='Settings', fg='black', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 10, 'bold')).place(x=150, y=290, height=50, width=200)

    msg = Label(mainF,bg='white')
    msg.place(x=150, y=400, height=50,width=200)

def notification():


    mainF = Frame(APP, bg='#D0D7D7')
    mainF.place(width=500, height=160)

    global msg1
    global msg4

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=5)

    Label(mainF,text='NOTIFICATION', fg='#524F4E', bg='#D0D7D7').place(width=100, height=10, y=15,x=175)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=35)

    msg1 = Label(mainF, bg='#D0D7D7', border=0)
    msg1.place(x=100, y=60)

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=155)
    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=158)

    try:
        user = name.get()
        deliad = addres.get()

        msg1.config(fg='black', text='Suscessfull Your Oder !\n'+user+'\n'+deliad+'\nThank You ...\nPlease Come Back')

    except:
        msg1.config(fg='red', text='Not notification\nFirst you Oder Your Choice ... ')

        pass

def blacknotification():


    mainF = Frame(APP, bg='#D0D7D7')
    mainF.place(width=500, height=160)

    global msg1

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=5)

    Label(mainF,text='NOTIFICATION', fg='#524F4E', bg='#D0D7D7').place(width=100, height=10, y=15,x=175)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=35)

    msg1 = Label(mainF, bg='#D0D7D7', border=0)
    msg1.place(x=100, y=60)

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=155)
    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=158)

    try:
        buser = bname.get()
        bdeliad = baddres.get()

        msg1.config(fg='black', text='Suscessfull Your Oder !\n'+buser+'\n'+bdeliad+'\nThank You ...\nPlease Come Back')

    except:
        msg1.config(fg='red', text='Not notification\nFirst you Oder Your Choice ... ')

        pass


def nightON():

    global msgblack

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("s2.png").resize((75, 75)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=75, width=75, x=190, y=80)

    img = ImageTk.PhotoImage(Image.open("d7.jpg").resize((50, 50)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=50, width=50, x=30, y=270)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='Setting', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20,
                                                                                              y=185, x=170)

    MENU1 = Menu()
    APP.config(menu=MENU1)
    # MENU1.place(width=100, height=200)

    submenu1 = Menu()

    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='____________________________________________________')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='____________________________________________________')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label="                            Home                                                ",command=nightmenu)
    submenu1.add_command()
    submenu1.add_command(label="                           Setting                                                 ",command=blacksetting)
    submenu1.add_command()
    submenu1.add_command(label='                         Notification',command=blacknotification)
    submenu1.add_command()
    submenu1.add_command(label='                           About')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='Developer - sinethbethie python vertion')
    submenu1.add_command(label='3.00.0 app vertion 27.0.0 helping pycharm ')
    submenu1.add_command(label='           ______ app 1.0.52.|| ______ ')

    MENU1.add_cascade(label='___________________________________________________________________________________________________')
    MENU1.add_cascade(label='                                                             ')
    MENU1.add_cascade(label="                                      Menu                                                ",menu=submenu1)
    MENU1.add_cascade(label='___________________________________________________________________________________________________')

    btn = Button(mainF, text='ON', command=nightON1, fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 10, 'bold'))  # .place(x=300, y=50, height=50, width=50)
    btn.place(x=300, y=270, height=50, width=50)
    btn2 = Button(mainF, text='OFF', command=nightoff, fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 10, 'bold'))  # .place(x=300, y=50, height=50, width=50)
    btn2.place(x=360, y=270, height=50, width=50)
    Label(mainF, text='Night Mode', bg='black', fg='white', font=('Consolas', 10, 'bold')).place(x=100, y=270, height=50,width=100)
    Button(mainF, text='Back', command=nightback, fg='white', bg='black', border=0, font=('Consolas', 10, 'bold')).place(x=50, y=500, height=50, width=200)

    msgblack = Label(mainF, bg='black')
    msgblack.place(x=150, y=400, height=50, width=200)

    msgblack.config(fg='yellow', text='Night Mode ON')
    notification()
    msg1.config(fg='red', text='Night Mode is ON')


def nightON1():
    msgblack.config(fg='red', text='Night Mode is ON')
    #notification()
    msg1.config(fg='red', text='Night Mode is ON')

def nightoff():
    setting()
    msg.config(fg='yellow', text='Night Mode OFF')

    MENU1 = Menu()
    APP.config(menu=MENU1)

    submenu1 = Menu()

    submenu1.image_names()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='____________________________________________________')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='____________________________________________________')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label="                            Home                                                ",command=menu)
    submenu1.add_command()
    submenu1.add_command(label="                           Setting                                                 ", command=setting)
    submenu1.add_command()
    submenu1.add_command(label='                            About')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='Developer - sinethbethie python vertion')
    submenu1.add_command(label='3.00.0 app vertion 27.0.0 helping pycharm ')
    submenu1.add_command(label='           ______ app 1.0.52.|| ______ ')

    MENU1.add_cascade(label='___________________________________________________________________________________________________')
    MENU1.add_cascade(label='                                                             ')
    MENU1.add_cascade( label="                                      Menu                                                ",menu=submenu1)
    MENU1.add_cascade(label='___________________________________________________________________________________________________')

def nightback():
    nightmenu()



def nightmenu():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=100)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=350)



    MENU1 = Menu()
    APP.config(menu=MENU1)
    # MENU1.place(width=100, height=200)

    submenu1 = Menu()

    submenu1.image_names()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='____________________________________________________')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='____________________________________________________')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label="                            Home                                                ",command=nightmenu)
    submenu1.add_command()
    submenu1.add_command(label="                           Setting                                                 ",command=blacksetting)
    submenu1.add_command()
    submenu1.add_command(label='                         Notification',command=blacknotification)
    submenu1.add_command()
    submenu1.add_command(label='                           About')
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command()
    submenu1.add_command(label='Developer - sinethbethie python vertion')
    submenu1.add_command(label='3.00.0 app vertion 27.0.0 helping pycharm ')
    submenu1.add_command(label='           ______ app 1.0.52.|| ______ ')

    MENU1.add_cascade(label='___________________________________________________________________________________________________')
    MENU1.add_cascade(label='                                                             ')
    MENU1.add_cascade( label="                                      Menu                                                ",menu=submenu1)
    MENU1.add_cascade(label='___________________________________________________________________________________________________')

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)

    Button(mainF, text='Prawns Pride',command=blackprawnsp, fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Simsun', 15, 'bold')).place(x=20, y=90, height=50, width=150)
    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=220, x=10)
    Label(mainF, text='Prawns Pride', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=240, x=10)

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=305)

    Button(mainF, text='Prawns Devil',command=blackprawnsd, fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Simsun', 15, 'bold')).place(x=20, y=340, height=50, width=150)
    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=470, x=10)
    Label(mainF, text='Prawns Devil', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF,fg='white', bg='white').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', command=nightnext1, fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='Bites', fg='white', bg='#EF930C', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Biryani', command=nightburimenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Rice', fg='white', command=nightricemenu, bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', command=nightnextmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='white', bg='black').place(width=500, height=15,y=695)


def nightnext1():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f13.jpg").resize((200, 200)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f17.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Rose Chicken', fg='white', bg='black', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=150)
    Label(mainF,text='RS 800.00' , fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Rose Chicken',fg='white', bg='black', font = ('SimSun', 12, 'bold')).place(width=140, height=20, y=240, x=10)

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=305)

    Button(mainF, text='Chicken Devel', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=150)
    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Chicken Devel', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)
    Button(mainF, text='<<< Previous',command=nightmenu, fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=560, height=30, width=100)

    Button(mainF, text='Bites', fg='white', bg='#EF930C', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Biryani',command=nightburimenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Rice', fg='white',command=nightricemenu, bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>',command=nightnextNext1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.' ,fg='white', bg='black').place(width=500, height=15, y=695)

def nightnextNext1():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f13.jpg").resize((200, 200)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f17.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Rose Chicken', fg='white', bg='black', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=150)
    Label(mainF,text='RS 800.00' , fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Rose Chicken',fg='white', bg='black', font = ('SimSun', 12, 'bold')).place(width=140, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=305)

    Button(mainF, text='Chicken Devel', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=150)
    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=450, x=10)
    Label(mainF, text='Chicken Devel', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)
    Button(mainF, text='<<< Previous', command=nightmenu, fg='white', bg='black', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=560, height=30, width=100)

    Button(mainF, text='<< Previous',command=nightnext1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Koththu',command=nightkottumenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Juice', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='white', bg='black').place(width=500, height=15, y=695)

def nightnextmenu():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Prawns Pride',command=blackprawnsp, fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=150)
    Label(mainF,text='RS 500.00' , fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Prawns Pride',fg = '#524F4E', bg = 'white', font = ('SimSun', 12, 'bold')).place(width=140, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=305)

    Button(mainF, text='Prawns Devil', fg='#524F4E', bg='white', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=150)
    Label(mainF, text='RS 400.00', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=450, x=10)
    Label(mainF, text='Prawns Devil', fg='#524F4E', bg='white', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='<< Previous',command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Koththu',command=nightkottumenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Juice', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.',fg='white', bg='black').place(width=500, height=15, y=695)


#Black Prawns Pride

def blackprawnsp():

    global inp

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=320, x=10)
    Label(mainF, text='Prawns Pride', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+',command=blackincres1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='1', fg='white', bg='black', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00',command=blackcartpp, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

def blackcartpp():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Pride',fg='white', bg='black', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF,fg='white', bg='white').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 500.00',  fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 1 ',  fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 550.00 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=blackorderpp, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

def blackorderpp():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global bname
    global baddres
    global bnumber
    global bacnum
    global bcrdtyp
    global bncc
    global bmsg
    bname = StringVar()
    baddres = StringVar()
    bnumber = StringVar()
    bacnum = StringVar()
    bncc = StringVar()
    bcrdtyp = StringVar()

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=bname, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=bnumber, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=baddres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=bacnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='white', bg='black', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=bncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=bcrdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=410)

    bmsg = Label(mainF, bg='black', border=0)
    bmsg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=blacksavepp, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

def blacksavepp():
    buser = bname.get()
    bdeliad = baddres.get()
    bdelinum = bnumber.get()
    buserAc = bacnum.get()
    buserncc = bncc.get()
    busecrd = bcrdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if buser == "" or bdeliad == "" or buserAc=="" :
        bmsg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(buser + '\n')
        userFile.write(bdeliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+bdelinum + '\n')
        userFile.write(buserAc + '\n')
        userFile.write(buserncc + '\n')
        userFile.write(busecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 1' + '\n')
        userFile.write('Total Price = RS 550.00' + '\n')
        userFile.close()

        bmsg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

    blacknotification()

def blackincres1():

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Pride',fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-',command=blackprawnsp, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=blackincres2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='2', fg='white', bg='black', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00',command=blackcartpp1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

def blackcartpp1():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Pride', fg='white', bg='black', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 2 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 1050.00 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=blackorderpp1, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

def blackorderpp1():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global bname
    global baddres
    global bnumber
    global bacnum
    global bcrdtyp
    global bncc
    global bmsg
    bname = StringVar()
    baddres = StringVar()
    bnumber = StringVar()
    bacnum = StringVar()
    bncc = StringVar()
    bcrdtyp = StringVar()

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact',fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=bname, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=bnumber, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=baddres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=bacnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='white', bg='black', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=bncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=bcrdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=410)

    bmsg = Label(mainF, bg='black', border=0)
    bmsg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=blacksavepp1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

def blacksavepp1():
    buser = bname.get()
    bdeliad = baddres.get()
    bdelinum = bnumber.get()
    buserAc = bacnum.get()
    buserncc = bncc.get()
    busecrd = bcrdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if buser == "" or bdeliad == "" or buserAc=="" :
        bmsg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(buser + '\n')
        userFile.write(bdeliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+bdelinum + '\n')
        userFile.write(buserAc + '\n')
        userFile.write(buserncc + '\n')
        userFile.write(busecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 2' + '\n')
        userFile.write('Total Price = RS 1050.00' + '\n')
        userFile.close()

        bmsg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

    blacknotification()

def blackincres2():

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Pride', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', command=blackincres1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=blackincres3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='3', fg='white', bg='black', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00',command=blackcartpp2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

def blackcartpp2():

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Pride', fg='white', bg='black', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 3 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 1550.00 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=blackorderpp2, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

def blackorderpp2():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global bname
    global baddres
    global bnumber
    global bacnum
    global bcrdtyp
    global bncc
    global bmsg
    bname = StringVar()
    baddres = StringVar()
    bnumber = StringVar()
    bacnum = StringVar()
    bncc = StringVar()
    bcrdtyp = StringVar()

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=bname, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=bnumber, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=baddres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=bacnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='white', bg='black', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=bncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=bcrdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=410)

    bmsg = Label(mainF, bg='black', border=0)
    bmsg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=blacksavepp2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

def blacksavepp2():
    buser = bname.get()
    bdeliad = baddres.get()
    bdelinum = bnumber.get()
    buserAc = bacnum.get()
    buserncc = bncc.get()
    busecrd = bcrdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if buser == "" or bdeliad == "" or buserAc=="" :
        bmsg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(buser + '\n')
        userFile.write(bdeliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+bdelinum + '\n')
        userFile.write(buserAc + '\n')
        userFile.write(buserncc + '\n')
        userFile.write(busecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 3' + '\n')
        userFile.write('Total Price = RS 1550.00' + '\n')
        userFile.close()

        bmsg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

    blacknotification()

def blackincres3():

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Pride', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', command=blackincres2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=blackincres4, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='4', fg='white', bg='black', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00',command=blackcartpp3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

def blackcartpp3():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Pride', fg='white', bg='black', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total',fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 500.00',fg='white', bg='black' , font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 4 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 2050.00 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=blackorderpp3, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

def blackorderpp3():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global bname
    global baddres
    global bnumber
    global bacnum
    global bcrdtyp
    global bncc
    global bmsg
    bname = StringVar()
    baddres = StringVar()
    bnumber = StringVar()
    bacnum = StringVar()
    bncc = StringVar()
    bcrdtyp = StringVar()

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact',fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=bname, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=bnumber, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=baddres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=bacnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ',fg='white', bg='black', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=bncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=bcrdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=410)

    bmsg = Label(mainF, bg='black', border=0)
    bmsg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=blacksavepp3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

def blacksavepp3():
    buser = bname.get()
    bdeliad = baddres.get()
    bdelinum = bnumber.get()
    buserAc = bacnum.get()
    buserncc = bncc.get()
    busecrd = bcrdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if buser == "" or bdeliad == "" or buserAc=="" :
        bmsg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\'+str(new_id),'w')
        userFile.write(buser + '\n')
        userFile.write(bdeliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94'+bdelinum + '\n')
        userFile.write(buserAc + '\n')
        userFile.write(buserncc + '\n')
        userFile.write(busecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 4' + '\n')
        userFile.write('Total Price = RS 2050.00' + '\n')
        userFile.close()

        bmsg.config(fg='green', text='Suscessfull Oder\nYour Order ID - '+str(new_id) )

    blacknotification()

def blackincres4():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=320, x=10)
    Label(mainF, text='Prawns Pride', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=340, x=10)

    Button(mainF, text='-', command=blackincres3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='5', fg='white', bg='black', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00',command=blackcartpp4, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550, height=50, width=450)

def blackcartpp4():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f11.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=30)

    Label(mainF, text='Prawn Pride', fg='white', bg='black', font=('SimSun', 15,'bold')).place(width=120, height=20, y=320,x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20,y=370, x=10)
    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20,y=370, x=380)

    Label(mainF, text='Delivery Fee', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20,y=390, x=10)
    Label(mainF, text=' RS 50.00  ', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20,y=390, x=380)

    Label(mainF, text='Items count', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=410, x=10)
    Label(mainF, text=' 5 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20,y=410, x=380)

    Label(mainF, text='Total ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=430, x=10)
    Label(mainF, text=' RS 2550.00 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=430,x=380)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=blackorderpp4, fg='white', bg='orange', border=0,activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,height=50, width=450)

def blackorderpp4():

    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global bname
    global baddres
    global bnumber
    global bacnum
    global bcrdtyp
    global bncc
    global bmsg
    bname = StringVar()
    baddres = StringVar()
    bnumber = StringVar()
    bacnum = StringVar()
    bncc = StringVar()
    bcrdtyp = StringVar()

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40, y=30)

    Label(mainF, text='Contact', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90, x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=bname, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=bnumber, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=baddres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280, x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=bacnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='white', bg='black', font=('SimSun', 50)).place(width=7, height=35,y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF,textvariable=bncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=bcrdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=410)

    bmsg = Label(mainF, bg='black', border=0)
    bmsg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE',command=blacksavepp4, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500, height=50, width=450)
    Button(mainF, text='Cansle', command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

def blacksavepp4():
    buser = bname.get()
    bdeliad = baddres.get()
    bdelinum = bnumber.get()
    buserAc = bacnum.get()
    buserncc = bncc.get()
    busecrd = bcrdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if buser == "" or bdeliad == "" or buserAc == "":
        bmsg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\' + str(new_id), 'w')
        userFile.write(buser + '\n')
        userFile.write(bdeliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94' + bdelinum + '\n')
        userFile.write(buserAc + '\n')
        userFile.write(buserncc + '\n')
        userFile.write(busecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 4' + '\n')
        userFile.write('Total Price = RS 2050.00' + '\n')
        userFile.close()

        bmsg.config(fg='green', text='Suscessfull Oder\nYour Order ID - ' + str(new_id))

    blacknotification()




#Black Prawns Devil

def blackprawnsd():
    global inp

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,
                                                                                              y=320, x=10)
    Label(mainF, text='Prawns Devil', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,
                                                                                                 y=340, x=10)

    Button(mainF, text='-', fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511',
           font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=blackincrespd1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='1', fg='white', bg='black', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 400.00', command=blackcartpd, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,
                                                                                                      height=50,
                                                                                                      width=450)

def blackcartpd():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='Prawn Devil', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20,
                                                                                                y=320, x=170)

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20, y=370, x=10)
    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20, y=370,
                                                                                      x=380)

    Label(mainF, text='Delivery Fee', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20, y=390,
                                                                                         x=10)
    Label(mainF, text=' RS 50.00  ', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20, y=390,
                                                                                        x=380)

    Label(mainF, text='Items count', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,
                                                                                                y=410, x=10)
    Label(mainF, text=' 1 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=410,
                                                                                        x=380)

    Label(mainF, text='Total ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=430,
                                                                                           x=10)
    Label(mainF, text=' RS 450.00 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20,
                                                                                                y=430, x=380)

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=blackorderpd, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,
                                                                                                      height=50,
                                                                                                      width=450)

def blackorderpd():
    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global bname
    global baddres
    global bnumber
    global bacnum
    global bcrdtyp
    global bncc
    global bmsg
    bname = StringVar()
    baddres = StringVar()
    bnumber = StringVar()
    bacnum = StringVar()
    bncc = StringVar()
    bcrdtyp = StringVar()

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='Contact', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90,
                                                                                            x=170)

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=bname, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=bnumber, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=baddres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280,
                                                                                            x=170)

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=bacnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='white', bg='black', font=('SimSun', 50)).place(width=7, height=35, y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF, textvariable=bncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=bcrdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='white', bg='white').place(width=500, height=1, y=410)

    bmsg = Label(mainF, bg='black', border=0)
    bmsg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE', command=blacksavepd, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500,
                                                                                                      height=50,
                                                                                                      width=450)
    Button(mainF, text='Cansle', command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

def blacksavepd():
    buser = bname.get()
    bdeliad = baddres.get()
    bdelinum = bnumber.get()
    buserAc = bacnum.get()
    buserncc = bncc.get()
    busecrd = bcrdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if buser == "" or bdeliad == "" or buserAc == "":
        bmsg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\' + str(new_id), 'w')
        userFile.write(buser + '\n')
        userFile.write(bdeliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94' + bdelinum + '\n')
        userFile.write(buserAc + '\n')
        userFile.write(buserncc + '\n')
        userFile.write(busecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 1' + '\n')
        userFile.write('Total Price = RS 550.00' + '\n')
        userFile.close()

        bmsg.config(fg='green', text='Suscessfull Oder\nYour Order ID - ' + str(new_id))

    blacknotification()

def blackincrespd1():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,
                                                                                              y=320, x=10)
    Label(mainF, text='Prawns Devil', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,
                                                                                                 y=340, x=10)

    Button(mainF, text='-', command=blackprawnsd, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=blackincrespd2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='2', fg='white', bg='black', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 400.00', command=blackcartpd1, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,
                                                                                                      height=50,
                                                                                                      width=450)

def blackcartpd1():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='Prawn Devil', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20,
                                                                                                y=320, x=170)

    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20, y=370, x=10)
    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20, y=370,
                                                                                      x=380)

    Label(mainF, text='Delivery Fee', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20, y=390,
                                                                                         x=10)
    Label(mainF, text=' RS 50.00  ', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20, y=390,
                                                                                        x=380)

    Label(mainF, text='Items count', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,
                                                                                                y=410, x=10)
    Label(mainF, text=' 2 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=410,
                                                                                        x=380)

    Label(mainF, text='Total ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=430,
                                                                                           x=10)
    Label(mainF, text=' RS 850.00 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20,
                                                                                                 y=430, x=380)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=blackorderpd1, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,
                                                                                                      height=50,
                                                                                                      width=450)

def blackorderpd1():
    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global bname
    global baddres
    global bnumber
    global bacnum
    global bcrdtyp
    global bncc
    global bmsg
    bname = StringVar()
    baddres = StringVar()
    bnumber = StringVar()
    bacnum = StringVar()
    bncc = StringVar()
    bcrdtyp = StringVar()

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='Contact', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90,
                                                                                            x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=bname, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=bnumber, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=baddres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280,
                                                                                            x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=bacnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='white', bg='black', font=('SimSun', 50)).place(width=7, height=35, y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF, textvariable=bncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=bcrdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=410)

    bmsg = Label(mainF, bg='black', border=0)
    bmsg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE', command=blacksavepd1, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500,
                                                                                                      height=50,
                                                                                                      width=450)
    Button(mainF, text='Cansle', command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

def blacksavepd1():
    buser = bname.get()
    bdeliad = baddres.get()
    bdelinum = bnumber.get()
    buserAc = bacnum.get()
    buserncc = bncc.get()
    busecrd = bcrdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if buser == "" or bdeliad == "" or buserAc == "":
        bmsg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\' + str(new_id), 'w')
        userFile.write(buser + '\n')
        userFile.write(bdeliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94' + bdelinum + '\n')
        userFile.write(buserAc + '\n')
        userFile.write(buserncc + '\n')
        userFile.write(busecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 2' + '\n')
        userFile.write('Total Price = RS 1050.00' + '\n')
        userFile.close()

        bmsg.config(fg='green', text='Suscessfull Oder\nYour Order ID - ' + str(new_id))

    blacknotification()

def blackincrespd2():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,
                                                                                              y=320, x=10)
    Label(mainF, text='Prawns Devil', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,
                                                                                                 y=340, x=10)

    Button(mainF, text='-', command=blackincrespd1, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=blackincrespd3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='3', fg='white', bg='black', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00', command=blackcartpd2, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,
                                                                                                      height=50,
                                                                                                      width=450)

def blackcartpd2():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='Prawn Devil', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20,
                                                                                                y=320, x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20, y=370, x=10)
    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20, y=370,
                                                                                      x=380)

    Label(mainF, text='Delivery Fee', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20, y=390,
                                                                                         x=10)
    Label(mainF, text=' RS 50.00  ', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20, y=390,
                                                                                        x=380)

    Label(mainF, text='Items count', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,
                                                                                                y=410, x=10)
    Label(mainF, text=' 3 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=410,
                                                                                        x=380)

    Label(mainF, text='Total ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=430,
                                                                                           x=10)
    Label(mainF, text=' RS 1250.00 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20,
                                                                                                 y=430, x=380)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=blackorderpd2, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,
                                                                                                      height=50,
                                                                                                      width=450)

def blackorderpd2():
    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global bname
    global baddres
    global bnumber
    global bacnum
    global bcrdtyp
    global bncc
    global bmsg
    bname = StringVar()
    baddres = StringVar()
    bnumber = StringVar()
    bacnum = StringVar()
    bncc = StringVar()
    bcrdtyp = StringVar()

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='Contact', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90,
                                                                                            x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=bname, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=bnumber, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=baddres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280,
                                                                                            x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=bacnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='white', bg='black', font=('SimSun', 50)).place(width=7, height=35, y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF, textvariable=bncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=bcrdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=410)

    bmsg = Label(mainF, bg='black', border=0)
    bmsg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE', command=blacksavepd2, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500,
                                                                                                      height=50,
                                                                                                      width=450)
    Button(mainF, text='Cansle', command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

def blacksavepd2():
    buser = bname.get()
    bdeliad = baddres.get()
    bdelinum = bnumber.get()
    buserAc = bacnum.get()
    buserncc = bncc.get()
    busecrd = bcrdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if buser == "" or bdeliad == "" or buserAc == "":
        bmsg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\' + str(new_id), 'w')
        userFile.write(buser + '\n')
        userFile.write(bdeliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94' + bdelinum + '\n')
        userFile.write(buserAc + '\n')
        userFile.write(buserncc + '\n')
        userFile.write(busecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 3' + '\n')
        userFile.write('Total Price = RS 1550.00' + '\n')
        userFile.close()

        bmsg.config(fg='green', text='Suscessfull Oder\nYour Order ID - ' + str(new_id))

    blacknotification()

def blackincrespd3():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,
                                                                                              y=320, x=10)
    Label(mainF, text='Prawns Devil', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,
                                                                                                 y=340, x=10)

    Button(mainF, text='-', command=blackincrespd2, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', command=blackincrespd4, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='4', fg='white', bg='black', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00', command=blackcartpd3, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,
                                                                                                      height=50,
                                                                                                      width=450)

def blackcartpd3():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='Prawn Devil', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20,
                                                                                                y=320, x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20, y=370, x=10)
    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20, y=370,
                                                                                      x=380)

    Label(mainF, text='Delivery Fee', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20, y=390,
                                                                                         x=10)
    Label(mainF, text=' RS 50.00  ', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20, y=390,
                                                                                        x=380)

    Label(mainF, text='Items count', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,
                                                                                                y=410, x=10)
    Label(mainF, text=' 4 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=410,
                                                                                        x=380)

    Label(mainF, text='Total ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=430,
                                                                                           x=10)
    Label(mainF, text=' RS 1650.00 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20,
                                                                                                 y=430, x=380)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=blackorderpd3, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,
                                                                                                      height=50,
                                                                                                      width=450)

def blackorderpd3():
    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global bname
    global baddres
    global bnumber
    global bacnum
    global bcrdtyp
    global bncc
    global bmsg
    bname = StringVar()
    baddres = StringVar()
    bnumber = StringVar()
    bacnum = StringVar()
    bncc = StringVar()
    bcrdtyp = StringVar()

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='Contact', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90,
                                                                                            x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=bname, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=bnumber, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=baddres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280,
                                                                                            x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=bacnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='white', bg='black', font=('SimSun', 50)).place(width=7, height=35, y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF, textvariable=bncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=bcrdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=410)

    bmsg = Label(mainF, bg='black', border=0)
    bmsg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE', command=blacksavepd3, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500,
                                                                                                      height=50,
                                                                                                      width=450)
    Button(mainF, text='Cansle', command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

def blacksavepd3():
    buser = bname.get()
    bdeliad = baddres.get()
    bdelinum = bnumber.get()
    buserAc = bacnum.get()
    buserncc = bncc.get()
    busecrd = bcrdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if buser == "" or bdeliad == "" or buserAc == "":
        bmsg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\' + str(new_id), 'w')
        userFile.write(buser + '\n')
        userFile.write(bdeliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94' + bdelinum + '\n')
        userFile.write(buserAc + '\n')
        userFile.write(buserncc + '\n')
        userFile.write(busecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 4' + '\n')
        userFile.write('Total Price = RS 2050.00' + '\n')
        userFile.close()

        bmsg.config(fg='green', text='Suscessfull Oder\nYour Order ID - ' + str(new_id))

    blacknotification()

def blackincrespd4():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,
                                                                                              y=320, x=10)
    Label(mainF, text='Prawns Devil', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,
                                                                                                 y=340, x=10)

    Button(mainF, text='-', command=blackincrespd3, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('Consolas', 20, 'bold')).place(x=120, y=390, height=50, width=50)
    Button(mainF, text='+', fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511',
           font=('Consolas', 20, 'bold')).place(x=320, y=390, height=50, width=50)

    inp = Label(mainF, text='5', fg='white', bg='black', font=('SimSun', 20, 'bold'))
    inp.place(width=50, height=50, y=390, x=225)

    Button(mainF, text='ADD TO CART : RS 500.00', command=blackcartpd4, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,
                                                                                                      height=50,
                                                                                                      width=450)

def blackcartpd4():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f10.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=150, y=100)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='Prawn Devil', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20,
                                                                                                y=320, x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=350)

    Label(mainF, text='Sub Total', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20, y=370, x=10)
    Label(mainF, text='RS 400.00', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20, y=370,
                                                                                      x=380)

    Label(mainF, text='Delivery Fee', fg='white', bg='black', font=('SimSun', 12)).place(width=120, height=20, y=390,
                                                                                         x=10)
    Label(mainF, text=' RS 50.00  ', fg='white', bg='black', font=('SimSun', 12)).place(width=100, height=20, y=390,
                                                                                        x=380)

    Label(mainF, text='Items count', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,
                                                                                                y=410, x=10)
    Label(mainF, text=' 5 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20, y=410,
                                                                                        x=380)

    Label(mainF, text='Total ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=430,
                                                                                           x=10)
    Label(mainF, text=' RS 2050.00 ', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=100, height=20,
                                                                                                 y=430, x=380)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=470)

    Button(mainF, text='PLACE ORDER', command=blackorderpd4, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=550,
                                                                                                      height=50,
                                                                                                      width=450)

def blackorderpd4():
    try:
        os.mkdir('newhottels')
    except:
        pass

    idfile = open('newhottels\\1000', 'w')
    idfile.close()

    global bname
    global baddres
    global bnumber
    global bacnum
    global bcrdtyp
    global bncc
    global bmsg
    bname = StringVar()
    baddres = StringVar()
    bnumber = StringVar()
    bacnum = StringVar()
    bncc = StringVar()
    bcrdtyp = StringVar()

    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,
                                                                                                                  y=30)

    Label(mainF, text='Contact', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=90,
                                                                                            x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=115)

    e_1 = Entry(mainF, textvariable=bname, border=0, bg='#dddddd', fg='#929292')
    e_1.place(width=200, height=35, x=50, y=125)
    e_1.insert(0, 'Name')

    e_2 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_2.place(width=50, height=35, x=50, y=170)
    e_2.insert(0, '+94 |')

    e_3 = Entry(mainF, textvariable=bnumber, border=0, bg='#dddddd', fg='#929292')
    e_3.place(width=150, height=35, x=101, y=170)
    e_3.insert(0, 'Phone Number')

    e_4 = Entry(mainF, textvariable=baddres, border=0, bg='#dddddd', fg='#929292')
    e_4.place(width=400, height=35, x=50, y=215)
    e_4.insert(0, 'Adress')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=260)

    Label(mainF, text='Payment', fg='white', bg='black', font=('SimSun', 15, 'bold')).place(width=120, height=20, y=280,
                                                                                            x=170)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=310)

    e_5 = Entry(mainF, textvariable=bacnum, border=0, bg='#dddddd', fg='#929292')
    e_5.place(width=200, height=35, x=50, y=320)
    e_5.insert(0, 'Account Number')

    e_6 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_6.place(width=50, height=35, x=350, y=320)
    e_6.insert(0, 'MM')

    Label(mainF, text=' / ', fg='white', bg='black', font=('SimSun', 50)).place(width=7, height=35, y=320, x=402)

    e_7 = Entry(mainF, border=0, bg='#dddddd', fg='#929292')
    e_7.place(width=50, height=35, x=412, y=320)
    e_7.insert(0, 'YY')

    e_8 = Entry(mainF, textvariable=bncc, border=0, bg='#dddddd', fg='#929292')
    e_8.place(width=70, height=35, x=350, y=365)
    e_8.insert(0, 'Ncc')

    e_9 = Entry(mainF, textvariable=bcrdtyp, border=0, bg='#dddddd', fg='#929292')
    e_9.place(width=200, height=35, x=50, y=365)
    e_9.insert(0, 'Card Type')

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=410)

    bmsg = Label(mainF, bg='black', border=0)
    bmsg.place(x=180, y=425)

    Button(mainF, text='SAVE AND CONTINUE', command=blacksavepd4, fg='white', bg='orange', border=0,
           activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=500,
                                                                                                      height=50,
                                                                                                      width=450)
    Button(mainF, text='Cansle', command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 12, 'bold')).place(x=20, y=570, height=50, width=450)

def blacksavepd4():
    buser = bname.get()
    bdeliad = baddres.get()
    bdelinum = bnumber.get()
    buserAc = bacnum.get()
    buserncc = bncc.get()
    busecrd = bcrdtyp.get()

    all_ids = os.listdir('newhottels')
    num = len(all_ids) - 1
    get_id = all_ids[num]
    new_id = int(get_id) + 1

    if buser == "" or bdeliad == "" or buserAc == "":
        bmsg.config(fg='red', text='Fill All')


    else:
        userFile = open('newhottels\\' + str(new_id), 'w')
        userFile.write(buser + '\n')
        userFile.write(bdeliad + '\n')
        userFile.write(str(new_id) + '\n')
        userFile.write('+94' + bdelinum + '\n')
        userFile.write(buserAc + '\n')
        userFile.write(buserncc + '\n')
        userFile.write(busecrd + '\n')
        userFile.write('Prawn Pride' + '\n')
        userFile.write('Iterm Count = 4' + '\n')
        userFile.write('Total Price = RS 2050.00' + '\n')
        userFile.close()

        bmsg.config(fg='green', text='Suscessfull Oder\nYour Order ID - ' + str(new_id))

    blacknotification()



def nightburimenu():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f20.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f16.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Special Biryani', fg='white', bg='black', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=170)
    Label(mainF,text='RS 500.00' , fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Special Biryani',fg='white', bg='black', font = ('SimSun', 12, 'bold')).place(width=160, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=305)

    Button(mainF, text='Mango Sawan', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Mango Sawan', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>',fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='Bites',command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Biryani', fg='white', bg='#EF930C', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Rice',command=nightricemenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', command=nightburinextmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='white', bg='black').place(width=500, height=15, y=695)
def nightburinextmenu():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f20.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f16.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)

    Button(mainF, text='Special Biryani', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=90, height=50, width=170)
    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=220, x=10)
    Label(mainF, text='Special Biryani', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=160,height=20, y=240,x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=305)

    Button(mainF, text='Mango Sawan', fg='white', bg='black', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Mango Sawan', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=490, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='<< Previous',command=nightburimenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Koththu',command=nightkottumenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Juice', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='white', bg='black').place(width=500, height=15, y=695)


def nightricemenu():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f15.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f21.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Vegitable Rice', fg='white', bg='black', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=170)
    Label(mainF,text='RS 300.00' , fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Vegitable Rice',fg='white', bg='black', font = ('SimSun', 12, 'bold')).place(width=160, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=305)

    Button(mainF, text='Chicken Rice', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Chicken Rice', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='Bites',command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Biryani',command=nightburimenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Rice', fg='white', bg='#EF930C', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', command=nightricenextmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='white', bg='black').place(width=500, height=15, y=695)
def nightricenextmenu():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f15.jpg").resize((300, 300)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f21.jpg").resize((250, 250)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)

    Button(mainF, text='Vegitable Rice', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=90, height=50, width=170)
    Label(mainF, text='RS 300.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=220, x=10)
    Label(mainF, text='Vegitable Rice', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=160,height=20, y=240,x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=305)

    Button(mainF, text='Chicken Rice', fg='white', bg='black', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Chicken Rice',fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=490, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='<< Previous',command=nightricemenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Koththu',command=nightkottumenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Juice', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='white', bg='black').place(width=500, height=15, y=695)


def nightkottumenu():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f8.jpeg").resize((200, 200)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f12.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)


    Button(mainF, text='Chicken Kottu', fg='white', bg='black', border=0, activebackground='#F3F7D7', activeforeground='#F85511',font=('SimSun', 15, 'bold')).place( x=20,y=90, height=50, width=170)
    Label(mainF,text='RS 300.00' , fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=220,x=10)
    Label(mainF, text='Chicken Kottu',fg='white', bg='black', font = ('SimSun', 12, 'bold')).place(width=160, height=20, y=240, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=305)

    Button(mainF, text='Mix Kottu', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Mix Kottu', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20, y=490, x=10)

    Label(mainF, fg='#524F4E', bg='white').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='<< Previous', command=nightkottunextmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Koththu', fg='white', bg='#EF930C', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Juice', fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>', fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)


    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='white', bg='black').place(width=500, height=15, y=695)
def nightkottunextmenu():
    mainF = Frame(APP, bg='black')
    mainF.place(width=500, height=720)

    img = ImageTk.PhotoImage(Image.open("f8.jpeg").resize((200, 200)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=80)

    img = ImageTk.PhotoImage(Image.open("f12.jpg").resize((350, 350)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=200, width=200, x=300, y=330)


    Label(mainF, text="|| Hotell Sethie's Garden ||", bg='orange', fg='white', font=('SimSun', 20, 'bold')).place(x=40,y=10)

    Button(mainF, text='Chicken Kottu', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=90, height=50, width=170)
    Label(mainF, text='RS 300.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20,y=220, x=10)
    Label(mainF, text='Chicken Kottu', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=160,height=20, y=240,x=10)

    Label(mainF, fg='#524F4E', bg='black').place(width=500, height=1, y=305)

    Button(mainF, text='Mix Kottu', fg='white', bg='black', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 15, 'bold')).place(x=20, y=340, height=50, width=160)
    Label(mainF, text='RS 500.00', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=120, height=20, y=470, x=10)
    Label(mainF, text='Mix Kottu', fg='white', bg='black', font=('SimSun', 12, 'bold')).place(width=140, height=20,y=490, x=10)

    Label(mainF, fg='#524F4E', bg='black').place(width=500, height=1, y=555)

    Button(mainF, text='next >>>', fg='white', bg='black', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=400, y=560, height=30, width=100)

    Button(mainF, text='Bites', command=nightmenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=20, y=600, height=50, width=100)
    Button(mainF, text='Biryani', command=nightburimenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7', activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=140, y=600, height=50, width=100)
    Button(mainF, text='Rice', command=nightricemenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=260, y=600, height=50, width=100)
    Button(mainF, text='Next >>',command=nightkottumenu, fg='white', bg='orange', border=0, activebackground='#F3F7D7',activeforeground='#F85511', font=('SimSun', 10, 'bold')).place(x=380, y=600, height=50, width=100)

    Label(mainF, text='Vertion 0V.12.22 powerd by pycharm.', fg='white', bg='black').place(width=500, height=15, y=695)



def blacksetting():
    nightON()
def back():
    menu()

menu()
APP.mainloop()