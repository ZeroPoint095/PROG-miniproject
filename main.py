from tkinter import *
#import actuele_vertrektijden
#import vertragingen
#import
#import

class App:

    def __init__(self, master):

        global frame
        global frame2

        frame = Frame(master, width=250)
        frame.pack(side=LEFT)

        frame2 = Frame(master, width=250)
        frame2.pack(side=LEFT)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=TOP, fill=X)

        self.quentin_hoofdmenu_knop = Button(frame, text="Quentin", command=self.quentin)
        self.quentin_hoofdmenu_knop.pack(side=TOP, fill=X)

        self.ard_jan_hoofdmenu_knop = Button(frame, text="Ard-Jan", command=self.ard_jan)
        self.ard_jan_hoofdmenu_knop.pack(side=TOP, fill=X)

        self.roel_hoofdmenu_knop = Button(frame, text="Roel", command=self.roel)
        self.roel_hoofdmenu_knop.pack(side=TOP, fill=X)

        self.hans_hoofdmenu_knop = Button(frame, text="Hans", command=self.hans)
        self.hans_hoofdmenu_knop.pack(side=TOP, fill=X)

    def quentin(self):

        global frame
        global frame2
        global quentin

        if quentin:
            self.quentin_weghalen()
        if ard_jan:
            self.ard_jan_weghalen()
        if roel:
            self.roel_weghalen()
        if hans:
            self.hans_weghalen()

        self.quentin_weghalen_knop = Button(frame2, text="hoofdmenu", fg="red", command=self.quentin_weghalen)
        self.quentin_weghalen_knop.pack(side=TOP, fill=X)

        self.quentin_functie_knop = Button(frame2, text="Quentin functie", command=self.quentin_functie)
        self.quentin_functie_knop.pack(side=TOP, fill=X)

        quentin=True

    def quentin_weghalen(self):
        self.quentin_weghalen_knop.destroy()
        self.quentin_functie_knop.destroy()

        global quentin
        quentin=False

    def quentin_functie(self):
        print('Quentin')

    def ard_jan(self):

        global frame
        global frame2
        global ard_jan

        if quentin:
            self.quentin_weghalen()
        if ard_jan:
            self.ard_jan_weghalen()
        if roel:
            self.roel_weghalen()
        if hans:
            self.hans_weghalen()

        self.ard_jan_weghalen_knop = Button(frame2, text="hoofdmenu", fg="red", command=self.ard_jan_weghalen)
        self.ard_jan_weghalen_knop.pack(side=TOP, fill=X)

        self.ard_jan_knop = Button(frame2, text="Ard_jan functie", command=self.ard_jan_functie)
        self.ard_jan_knop.pack(side=TOP, fill=X)

        ard_jan=True

    def ard_jan_weghalen(self):
        self.ard_jan_weghalen_knop.destroy()
        self.ard_jan_knop.destroy()

        global ard_jan
        ard_jan=False


    def ard_jan_functie(self):
        print('Ard_jan')

    def roel(self):

        global frame
        global frame2
        global roel

        if quentin:
            self.quentin_weghalen()
        if ard_jan:
            self.ard_jan_weghalen()
        if roel:
            self.roel_weghalen()
        if hans:
            self.hans_weghalen()

        self.roel_weghalen_knop = Button(frame2, text="hoofdmenu", fg="red", command=self.roel_weghalen)
        self.roel_weghalen_knop.pack(side=TOP, fill=X)

        self.roel_functie_knop = Button(frame2, text="Roel functie", command=self.roel_functie)
        self.roel_functie_knop.pack(side=TOP, fill=X)
        roel=True

    def roel_weghalen(self):
        self.roel_weghalen_knop.destroy()
        self.roel_functie_knop.destroy()

        global hans
        roel=False

    def roel_functie(self):
        print('Roel')

    def hans(self):

        global frame
        global frame2
        global hans

        if quentin:
            self.quentin_weghalen()
        if ard_jan:
            self.ard_jan_weghalen()
        if roel:
            self.roel_weghalen()
        if hans:
            self.hans_weghalen()

        self.hans_weghalen_knop = Button(frame2, text="hoofdmenu", fg="red", command=self.hans_weghalen)
        self.hans_weghalen_knop.pack(side=TOP, fill=X)

        self.hans_functie_knop = Button(frame2, text="Hans functie", command=self.hans_functie)
        self.hans_functie_knop.pack(side=TOP, fill=X)

        hans=True

    def hans_weghalen(self):
        self.hans_weghalen_knop.destroy()
        self.hans_functie_knop.destroy()

        global hans
        hans=False

    def hans_functie(self):
        print('Hans')

quentin=False
ard_jan=False
roel=False
hans=False

root = Tk()

app = App(root)

root.mainloop()
