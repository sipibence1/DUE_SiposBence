import random
from tkinter import *

def lotto_no():
    seged1 = random.randint(1, 49);
    seged2 = random.randint(1, 49);
    seged3 = random.randint(1, 49);
    seged4 = random.randint(1, 49);
    seged5 = random.randint(1, 49);
    genelso.set(seged1)
    genmasodik.set(seged2)
    genharmadik.set(seged3)
    gennegyedik.set(seged4)
    genotodik.set(seged5)
    return

# grafikus ablak létrehozása
lotto = Tk()

# grafikus ablak méretezése
lotto.geometry('800x360')
frame = Frame(lotto)
frame.pack()

lotto.title("Lottó");

genelso = StringVar()
genmasodik = StringVar()
genharmadik = StringVar()
gennegyedik = StringVar()
genotodik = StringVar()

var = StringVar()
var.set("Generált Lottószámok")
frame1 = Frame(lotto)
frame1.pack(side=TOP)
label = Label(frame1, textvariable=var, font=("Arial", 48), width=24)
label.pack(side=TOP)
label = Label(frame1, textvariable="", width=24)
label.pack(side=TOP)
label = Label(frame1, textvariable="", width=24)
label.pack(side=TOP)

frame2 = Frame(lotto)
frame2.pack(side=TOP)
txtDisplay = Entry(frame2, textvariable=genelso, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=genmasodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=genharmadik, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                   width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=gennegyedik, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                   width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=genotodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay.pack(side=LEFT)

frame3 = Frame(lotto)
frame3.pack(side=TOP)

button1 = Button(frame3, padx=8, width=18, pady=8, bd=8, font=("Arial", 26), text="Lotto Generator", command=lotto_no)
button1.pack(side=TOP)

lotto.mainloop()
