import random
from tkinter import *

def lottoszamok():
    button1["state"] = DISABLED


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

    frame5 = Frame(lotto)
    frame5.pack(side=TOP)

    label1 = Label(frame5, font=("Arial", 20), width=24, text="A nyertes Lottószámok:")
    label1.pack(side=LEFT)
    genszamok = Entry(frame5, textvariable=genelso, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3,
                      state=DISABLED)
    genszamok.pack(side=LEFT)
    genszamok = Entry(frame5, textvariable=genmasodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                      width=3, state=DISABLED)
    genszamok.pack(side=LEFT)
    genszamok = Entry(frame5, textvariable=genharmadik, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                      width=3, state=DISABLED)
    genszamok.pack(side=LEFT)
    genszamok = Entry(frame5, textvariable=gennegyedik, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                      width=3, state=DISABLED)
    genszamok.pack(side=LEFT)
    genszamok = Entry(frame5, textvariable=genotodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                      width=3, state=DISABLED)
    genszamok.pack(side=LEFT)

    sajatelsoo = StringVar()
    sajatmasodikk = StringVar()
    sajatharmadikk = StringVar()
    sajatnegyedikk = StringVar()
    sajatotodikk = StringVar()
    sajatelsoo.set(sajatszamok1.get())

    frame6 = Frame(lotto)
    frame6.pack(side=TOP)
    label1 = Label(frame6, font=("Arial", 20), width=24, text="Kérem adja meg a számait:")
    label1.pack(side=LEFT)

    sajatszamok11 = Entry(frame6, textvariable=sajatelsoo, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                         width=3)
    sajatszamok11.pack(side=LEFT)
    sajatszamok22 = Entry(frame6, textvariable=sajatmasodikk, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                         width=3)
    sajatszamok22.pack(side=LEFT)
    sajatszamok33 = Entry(frame6, textvariable=sajatharmadikk, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                         width=3)
    sajatszamok33.pack(side=LEFT)
    sajatszamok44 = Entry(frame6, textvariable=sajatnegyedikk, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                         width=3)
    sajatszamok44.pack(side=LEFT)
    sajatszamok55 = Entry(frame6, textvariable=sajatotodikk, bd=20, insertwidth=1, font=("Arial", 30), justify="center",
                         width=3)
    sajatszamok55.pack(side=LEFT)


















# ablak létrehozása
lotto = Tk()

# ablak méretezése
lotto.geometry('1000x600')
frame = Frame(lotto)
frame.pack()

# ablak cím megadása
lotto.title("Ötöslottó");

# lottószámok változói

genelso = StringVar()
genmasodik = StringVar()
genharmadik = StringVar()
gennegyedik = StringVar()
genotodik = StringVar()

#sajátszámok változói


sajatelso = StringVar()
sajatmasodik = StringVar()
sajatharmadik = StringVar()
sajatnegyedik = StringVar()
sajatotodik = StringVar()

frame1 = Frame(lotto)
frame1.pack(side=TOP)
label1 = Label(frame1, font=("Arial", 20), width=24, text="Kérem adja meg a számait:")
label1.pack(side=LEFT)

sajatszamok1 = Entry(frame1, textvariable=sajatelso, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok1.pack(side=LEFT)
sajatszamok2 = Entry(frame1, textvariable=sajatmasodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok2.pack(side=LEFT)
sajatszamok3 = Entry(frame1, textvariable=sajatharmadik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok3.pack(side=LEFT)
sajatszamok4 = Entry(frame1, textvariable=sajatnegyedik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok4.pack(side=LEFT)
sajatszamok5 = Entry(frame1, textvariable=sajatotodik, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=3)
sajatszamok5.pack(side=LEFT)

print(sajatelso)
frame3 = Frame(lotto)
frame3.pack(side=TOP)

button1 = Button(frame3, padx=8, width=10, pady=2, bd=8, font=("Arial", 26), text="SORSOLÁS", command=lottoszamok)
button1.pack(side=TOP)

lotto.mainloop()