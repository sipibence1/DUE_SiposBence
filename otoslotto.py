import random
from tkinter import *

# lottószámgenerálás
def lotto_no():
    a = False
    while a = True:
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

def nyertesszamok():
    .

    lotto_no()

    # Üres sor
    frame4 = Frame(lotto)
    frame4.pack(side=TOP)
    label4 = Label(frame4, font=("Arial", 20), width=24, text="")
    label4.pack(side=LEFT)

    frame5 = Frame(lotto)
    frame5.pack(side=TOP)

    label1 = Label(frame5, font=("Arial", 20), width=24, text="A nyertes Lottószámok:")
    label1.pack(side=LEFT)
    genszamok = Entry(frame5, textvariable=genelso, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3, state=DISABLED)
    genszamok.pack(side=LEFT)
    genszamok = Entry(frame5, textvariable=genmasodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3, state=DISABLED)
    genszamok.pack(side=LEFT)
    genszamok = Entry(frame5, textvariable=genharmadik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3, state=DISABLED)
    genszamok.pack(side=LEFT)
    genszamok = Entry(frame5, textvariable=gennegyedik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3, state=DISABLED)
    genszamok.pack(side=LEFT)
    genszamok = Entry(frame5, textvariable=genotodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3, state=DISABLED)
    genszamok.pack(side=LEFT)

    #Eredmény

    frame5 = Frame(lotto)
    frame5.pack(side=TOP)
    label5 = Label(frame5, font=("Arial", 20), width=24, text="")
    label5.pack(side=LEFT)

    ered = 1
    frame6 = Frame(lotto)
    frame6.pack(side=TOP)
    label6 = Label(frame6, font=("Arial", 20), width=15, text="Eltalált számok: ")
    label6.pack(side=LEFT)
    label6 = Label(frame6, font=("Arial", 20), width=5, text=ered)
    label6.pack(side=LEFT)

    return

# ablak létrehozása
lotto = Tk()

# ablak méretezése
lotto.geometry('1000x600')
frame = Frame(lotto)
frame.pack()

# ablak cím megadása
lotto.title("Ötöslottó");

# lottószámok változoi
genelso = StringVar()
genmasodik = StringVar()
genharmadik = StringVar()
gennegyedik = StringVar()
genotodik = StringVar()

#Kérem és saját számok megadása

sajatelso = StringVar()
sajatmasodik = StringVar()
sajatharmadik = StringVar()
sajatnegyedik = StringVar()
sajatotodik = StringVar()


frame1 = Frame(lotto)
frame1.pack(side=TOP)
label1 = Label(frame1, font=("Arial", 20), width=24, text="Kérem adja meg a számait:")
label1.pack(side=LEFT)

sajatszamok = Entry(frame1, textvariable=sajatelso, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok.pack(side=LEFT)
sajatszamok = Entry(frame1, textvariable=sajatmasodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok.pack(side=LEFT)
sajatszamok = Entry(frame1, textvariable=sajatharmadik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok.pack(side=LEFT)
sajatszamok = Entry(frame1, textvariable=sajatnegyedik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok.pack(side=LEFT)
sajatszamok = Entry(frame1, textvariable=sajatotodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok.pack(side=LEFT)

#Üres sor
frame2 = Frame(lotto)
frame2.pack(side=TOP)
label2 = Label(frame2, font=("Arial", 20), width=24, text="")
label2.pack(side=LEFT)


#Ötöslottó sorsolás  gomb

frame3 = Frame(lotto)
frame3.pack(side=TOP)

button1 = Button(frame3, padx=8, width=10, pady=2, bd=8, font=("Arial", 26), text="SORSOLÁS", command=nyertesszamok)
button1.pack(side=TOP)


lotto.mainloop()
