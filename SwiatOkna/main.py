from tkinter import *
from SwiatOkna.HexSwiat import *
import sys
if __name__ == '__main__':
    def nowa():
        window.destroy()
        inputX()
        Swiat(x, y)
    def kontynuuj():
        window.destroy()
        Swiat()
    def kontynuujHex():
        window.destroy()
        HexSwiat()
    def wyjdz():
        window.destroy()
        sys.exit()
    def nowyHex():
        window.destroy()
        inputX()
        HexSwiat(x, y)

    def ustawX():
        global x
        x = int(Entry.get(e))
        print(str(x))
        if x < 5:
            windowX.destroy()
            inputX()
        else:
            windowX.destroy()
            inputY()

    def ustawY():
        global y
        y = int(Entry.get(e))
        print(str(y))
        windowY.destroy()

    def inputY():
        global windowY
        windowY = Tk()
        width = windowY.winfo_screenwidth()
        height = windowY.winfo_screenheight()
        x = (width / 2) - 150
        y = (height / 2) - 200
        windowY.geometry(f'280x300+{int(x)}+{int(y)}')
        windowY.title("Symulator świata")
        windowY.config(background="green")
        windowY.resizable(FALSE, FALSE)
        global e
        e = Entry(windowY, width=450)
        e.pack()
        but = Button(windowY, text="Ustaw wysokość mapy",
                     command=ustawY,
                     fg="black",
                     bg="white",
                     font=("Arial Black", 10),
                     activeforeground="black",
                     activebackground="white",
                     state=ACTIVE)
        but.place(x=50, y=50)
        windowY.mainloop()

    def inputX():
        global windowX
        windowX = Tk()
        width = windowX.winfo_screenwidth()
        height = windowX.winfo_screenheight()
        x = (width / 2) - 150
        y = (height / 2) - 200
        windowX.geometry(f'280x300+{int(x)}+{int(y)}')
        windowX.title("Symulator świata")
        windowX.config(background="green")
        windowX.resizable(FALSE, FALSE)
        global e
        e = Entry(windowX, width=450)
        e.pack()
        but = Button(windowX, text="Ustaw szerokość mapy",
                     command=ustawX,
                     fg="black",
                     bg="white",
                     font=("Arial Black", 10),
                     activeforeground="black",
                     activebackground="white",
                     state=ACTIVE)
        but.place(x=50, y=50)
        windowX.mainloop()

    def menu():
        global window
        window = Tk()
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        x = (width / 2) - 220
        y = (height / 2) - 250
        window.geometry(f'400x440+{int(x)}+{int(y)}')
        window.title("Symulator Świata")
        window.config(background="purple")
        window.resizable(FALSE, FALSE)
        button1 = Button(window, text="Nowa symulacja",
                        command=nowa,
                        fg="black",
                        bg="white",
                        font=("Arial Black", 15),
                        activeforeground="black",
                        activebackground="white",
                        state=ACTIVE)
        button1.place(x=98, y=50)

        button2 = Button(window, text="Kontynuuj",
                        command=kontynuuj,
                        fg="black",
                        bg="white",
                        font=("Arial Black", 15),
                        activeforeground="black",
                        activebackground="white",
                        state=ACTIVE)
        button2.place(x=130, y=170)

        button3 = Button(window, text="Wyjdź",
                        command=wyjdz,
                        fg="black",
                        bg="white",
                        font=("Arial Black", 15),
                        activeforeground="black",
                        activebackground="white",
                        state=ACTIVE)
        button3.place(x=155, y=290)

        button4 = Button(window, text="Nowa Symulacja w Hexie",
                        command=nowyHex,
                        fg="black",
                        bg="white",
                        font=("Arial Black", 15),
                        activeforeground="black",
                        activebackground="white",
                        state=ACTIVE)
        button4.place(x=45, y=110)

        button5 = Button(window, text="Kontynuuj w Hexie",
                        command=kontynuujHex,
                        fg="black",
                        bg="white",
                        font=("Arial Black", 15),
                        activeforeground="black",
                        activebackground="white",
                        state=ACTIVE)
        button5.place(x=85, y=230)

        window.mainloop()

    menu()


