from tkinter import *
#import actuele_vertrektijden
from Vertragingen import vertragingen
from storingen import storingen_ophalen
#import

class App:

    def __init__(self, master):

        global frame
        global frame2
        global frame3
        global frame4
        global scrollbar

        frame = Frame(master, width=250)
        frame.pack(side=LEFT)

        frame2 = Frame(master, width=250)
        frame2.pack(side=LEFT)

        frame3 = Frame(master)
        frame3.pack(side=RIGHT)

        scrollbar = Scrollbar(frame3)
        scrollbar.pack( side=RIGHT, fill=Y )

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit, bg="yellow")
        self.button.pack(side=TOP, fill=X)

        self.quentin_hoofdmenu_knop = Button(frame, text="Quentin", command=self.quentin, bg="yellow", fg="blue")
        self.quentin_hoofdmenu_knop.pack(side=TOP, fill=X)

        self.ard_jan_hoofdmenu_knop = Button(frame, text="Ard-Jan", command=self.ard_jan, bg="yellow", fg="blue")
        self.ard_jan_hoofdmenu_knop.pack(side=TOP, fill=X)

        self.vertragingen_hoofdmenu_knop = Button(frame, text="vertraging", command=self.vertraging, bg="yellow", fg="blue")
        self.vertragingen_hoofdmenu_knop.pack(side=TOP, fill=X)

        self.storingen_hoofdmenu_knop = Button(frame, text="Storingen", command=self.Storingen, bg="yellow", fg="blue")
        self.storingen_hoofdmenu_knop.pack(side=TOP, fill=X)

    def quentin(self):

        global frame
        global frame2
        global quentin

        if quentin:
            self.quentin_weghalen()
        if ard_jan:
            self.ard_jan_weghalen()
        if vertraging:
            self.vertraging_weghalen()
        if Storingen:
            self.storingen_weghalen()

        self.quentin_weghalen_knop = Button(frame2, text="hoofdmenu", fg="red", command=self.quentin_weghalen, bg="yellow")
        self.quentin_weghalen_knop.pack(side=TOP, fill=X)

        self.quentin_functie_knop = Button(frame2, text="Quentin functie", command=self.quentin_functie, bg="yellow", fg="blue")
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
        if vertraging:
            self.vertraging_weghalen()
        if Storingen:
            self.storingen_weghalen()

        self.ard_jan_weghalen_knop = Button(frame2, text="hoofdmenu", fg="red", command=self.ard_jan_weghalen, bg="yellow")
        self.ard_jan_weghalen_knop.pack(side=TOP, fill=X)

        self.ard_jan_knop = Button(frame2, text="Ard_jan functie", command=self.ard_jan_functie, bg="yellow", fg="blue")
        self.ard_jan_knop.pack(side=TOP, fill=X)

        ard_jan=True

    def ard_jan_weghalen(self):
        self.ard_jan_weghalen_knop.destroy()
        self.ard_jan_knop.destroy()

        global ard_jan
        ard_jan=False


    def ard_jan_functie(self):
        print('Ard_jan')

    def vertraging(self):

        global frame2
        global vertraging

        if quentin:
            self.quentin_weghalen()
        if ard_jan:
            self.ard_jan_weghalen()
        if vertraging:
            self.vertraging_weghalen()
        if Storingen:
            self.storingen_weghalen()

        self.vertraging_weghalen_knop = Button(frame2, text="hoofdmenu", fg="red", command=self.vertraging_weghalen, bg="yellow")
        self.vertraging_weghalen_knop.pack(side=TOP, fill=X)

        self.vertraging_functie_knop = Button(frame2, text="vertraging functie", command=self.vertraging_functie, bg="yellow", fg="blue")
        self.vertraging_functie_knop.pack(side=TOP, fill=X)

        vertraging=True

    def vertraging_weghalen(self):

        global vertraging_weergegeven

        self.vertraging_weghalen_knop.destroy()
        self.vertraging_functie_knop.destroy()
        if vertraging_weergegeven:
            self.vertraging_label.destroy()
            vertraging_weergegeven=False

        global vertraging
        vertraging=False

    def vertraging_functie(self):
        global vertraging_weergegeven
        if vertraging_weergegeven:
            self.vertraging_label.destroy()
            vertraging_weergegeven=False
        tekst='Informatie vertragingen: '
        for vertraging in vertragingen():
            tekst+='\n'+vertraging

        self.vertraging_label=Label(frame3, text=tekst)
        self.vertraging_label.pack()
        vertraging_weergegeven=True

    def Storingen(self):

        global frame2
        global Storingen

        if quentin:
            self.quentin_weghalen()
        if ard_jan:
            self.ard_jan_weghalen()
        if vertraging:
            self.vertraging_weghalen()
        if Storingen:
            self.storingen_weghalen()

        self.storingen_weghalen_knop = Button(frame2, text="hoofdmenu", fg="red", command=self.storingen_weghalen, bg="yellow")
        self.storingen_weghalen_knop.pack(side=TOP, fill=X)

        self.storingen_functie_knop = Button(frame2, text="Storingen", command=self.storingen_functie, bg="yellow", fg="blue")
        self.storingen_functie_knop.pack(side=TOP, fill=X)

        Storingen=True

    def storingen_weghalen(self):
        global storingen_weergegeven
        self.storingen_weghalen_knop.destroy()
        self.storingen_functie_knop.destroy()
        if storingen_weergegeven:
            self.storing_weergeven.destroy()
            storingen_weergegeven=False

        global Storingen
        Storingen=False

    def storingen_functie(self):
        global frame3
        global scrollbar
        global storingen_weergegeven

        storingen_weergegeven=True

        self.storing_weergeven = Canvas(frame3, yscrollcommand=scrollbar.set)#, bg='blue')
        self.storing_weergeven.config(width=1000, height=500)
        self.storing_weergeven.config(scrollregion=(500,0,1500, (250*len(storingen_ophalen()))))
        self.storing_weergeven.pack(expand=YES, padx=200)

        i=0
        for storing in storingen_ophalen():
            i+=1
            self.storing_weergeven.create_text(500, i*250, text=storing)
        scrollbar.config(command=self.storing_weergeven.yview)

quentin=False
ard_jan=False
vertraging=False
vertraging_weergegeven=False
Storingen=False
storingen_weergegeven=False

root = Tk()

app = App(root)

root.mainloop()
