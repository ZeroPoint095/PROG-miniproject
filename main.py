from tkinter import *

from Vertragingen import vertragingen
from actueleVertrektijden.actuele_vertrektijden import actuele_vertrekinformatie
from reisplanner import reisplanner
from reisplanner.intercitystations import returnStations
from storingen import storingen_ophalen_gepland
from storingen import storingen_ophalen_ongepland

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

        frame4 = Frame(frame3)
        frame4.pack(side=RIGHT)

        scrollbar = Scrollbar(frame3)
        scrollbar.pack( side=RIGHT, fill=Y )

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit, bg="yellow")
        self.button.pack(side=TOP, fill=X)

        self.reisplanner_hoofdmenu_knop = Button(frame, text="Reisplanner", command=self.reisplanner, bg="yellow", fg="blue")
        self.reisplanner_hoofdmenu_knop.pack(side=TOP, fill=X)

        self.actuele_vertrektijden_hoofdmenu_knop = Button(frame, text="Actuele Vertrektijden", command=self.actuele_vertrektijden, bg="yellow", fg="blue")
        self.actuele_vertrektijden_hoofdmenu_knop.pack(side=TOP, fill=X)

        self.vertragingen_hoofdmenu_knop = Button(frame, text="Vertraging", command=self.vertraging, bg="yellow", fg="blue")
        self.vertragingen_hoofdmenu_knop.pack(side=TOP, fill=X)

        self.storingen_hoofdmenu_knop = Button(frame, text="Storingen", command=self.Storingen, bg="yellow", fg="blue")
        self.storingen_hoofdmenu_knop.pack(side=TOP, fill=X)

    def reisplanner(self):

        global frame2
        global reisplanner

        if reisplanner:
            self.reisplanner_weghalen()
        if actuele_vertrektijden:
            self.actuele_vertrektijden_weghalen()
        if vertraging:
            self.vertraging_weghalen()
        if Storingen:
            self.storingen_weghalen()

        self.reisplanner_weghalen_knop = Button(frame2, text="Hoofdmenu", fg="red", command=self.reisplanner_weghalen, bg="yellow")
        self.reisplanner_weghalen_knop.pack(side=TOP, fill=X)

        self.reisplanner_functie_knop = Button(frame2, text="Reisplanner", command=self.reisplanner_functie, bg="yellow", fg="blue")
        self.reisplanner_functie_knop.pack(side=TOP, fill=X)

        reisplanner=True

    def reisplanner_weghalen(self):
        self.reisplanner_weghalen_knop.destroy()
        self.reisplanner_functie_knop.destroy()

        global reisplanner
        reisplanner=False

    def stationsweergeven(self, stationsletter):
        global reisplanner_stationsweergegeven
        global frame4

        ICDICT=returnStations()

        if reisplanner_stationsweergegeven:
            for station in ICDICT[stationsletter]:
                self.station_knop.destroy()

        reisplanner_stationsweergegeven=True

        for station in ICDICT[stationsletter]:
            self.station_knop = Button(frame4, text=station, fg="red", bg="yellow", command=reisplanner('Utrecht Centraal', station))
            self.station_knop.pack(side=TOP, padx=250)

    def reisplanner_functie(self):

        global reisplanner_weergegeven
        global frame3

        letters=["A", "B", "C", "D", "E", "G", "H", "L", "M", "N", "O", "R", "S", "T", "V", "W", "Z"]

        if reisplanner_weergegeven:
            for letter in letters:
                self.letter_knop.destroy()

        for letter in letters:
            self.letter_knop = Button(frame3, text=letter, fg="red", bg="yellow", command=self.stationsweergeven(letter))
            self.letter_knop.pack(side=TOP, padx=250)

        reisplanner_weergegeven=True

    def actuele_vertrektijden(self):

        global frame2
        global actuele_vertrektijden

        if reisplanner:
            self.reisplanner_weghalen()
        if actuele_vertrektijden:
            self.actuele_vertrektijden_weghalen()
        if vertraging:
            self.vertraging_weghalen()
        if Storingen:
            self.storingen_weghalen()

        self.actuele_vertrektijden_weghalen_knop = Button(frame2, text="Hoofdmenu", fg="red", command=self.actuele_vertrektijden_weghalen, bg="yellow")
        self.actuele_vertrektijden_weghalen_knop.pack(side=TOP, fill=X)

        self.actuele_vertrektijden_knop = Button(frame2, text="Actuele vertrektijden", command=self.actuele_vertrektijden_functie, bg="yellow", fg="blue")
        self.actuele_vertrektijden_knop.pack(side=TOP, fill=X)

        actuele_vertrektijden=True

    def actuele_vertrektijden_weghalen(self):
        global actuele_vertrektijden_weergegeven
        self.actuele_vertrektijden_weghalen_knop.destroy()
        self.actuele_vertrektijden_knop.destroy()
        if actuele_vertrektijden_weergegeven:
            self.actuele_vertrektijden_label.destroy()
            actuele_vertrektijden_weergegeven=False

        global actuele_vertrektijden
        actuele_vertrektijden=False

    def actuele_vertrektijden_functie(self):
        global scrollbar
        global actuele_vertrektijden_weergegeven
        if actuele_vertrektijden_weergegeven:
            self.actuele_vertrektijden_label.destroy()
            actuele_vertrektijden_weergegeven=False
        tekst=''
        self.actuele_vertrektijden_label=Text(frame3, width=500, height=600)
        for vertrektijd in actuele_vertrekinformatie():
            self.actuele_vertrektijden_label.insert(END, vertrektijd)
        self.actuele_vertrektijden_label.pack(fill=BOTH)

        actuele_vertrektijden_weergegeven=True
        scrollbar.config(command=self.actuele_vertrektijden_label.yview)

    def vertraging(self):

        global frame2
        global vertraging

        if reisplanner:
            self.reisplanner_weghalen()
        if actuele_vertrektijden:
            self.actuele_vertrektijden_weghalen()
        if vertraging:
            self.vertraging_weghalen()
        if Storingen:
            self.storingen_weghalen()

        self.vertraging_weghalen_knop = Button(frame2, text="Hoofdmenu", fg="red", command=self.vertraging_weghalen, bg="yellow")
        self.vertraging_weghalen_knop.pack(side=TOP, fill=X)

        self.vertraging_functie_knop = Button(frame2, text="Vertragingen", command=self.vertraging_functie, bg="yellow", fg="blue")
        self.vertraging_functie_knop.pack(side=TOP, fill=X)

        vertraging=True

    def vertraging_weghalen(self):

        global vertraging_weergegeven

        self.vertraging_weghalen_knop.destroy()
        self.vertraging_functie_knop.destroy()
        if vertraging_weergegeven:
            self.vertraging_weergeven.destroy()
            vertraging_weergegeven=False

        global vertraging
        vertraging=False

    def vertraging_functie(self):

        global frame3
        global vertraging_weergegeven

        if vertraging_weergegeven:
            self.vertraging_weergeven.destroy()
            vertraging_weergegeven=False

        self.vertraging_weergeven = Text(frame3, width=500, height=600)
        for vertraging in vertragingen():
            self.vertraging_weergeven.insert(END, vertraging)
        self.vertraging_weergeven.pack()

        vertraging_weergegeven=True

        scrollbar.config(command=self.storingen_weergeven.yview)

    def Storingen(self):

        global frame2
        global Storingen

        if reisplanner:
            self.reisplanner_weghalen()
        if actuele_vertrektijden:
            self.actuele_vertrektijden_weghalen()
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
            self.storingen_weergeven.destroy()
            storingen_weergegeven=False

        global Storingen
        Storingen=False

    def storingen_functie(self):
        global storingen_weergegeven

        if storingen_weergegeven:
            self.storingen_weergeven.destroy()
            storingen_weergegeven=False

        self.storingen_weergeven = Text(frame3, width=500, height=600)
        for storing in storingen_ophalen_gepland():
            self.storingen_weergeven.insert(END, storing)
        for storing in storingen_ophalen_ongepland():
            self.storingen_weergeven.insert(END, storing)
        self.storingen_weergeven.pack()

        storingen_weergegeven=True

        scrollbar.config(command=self.storingen_weergeven.yview)

reisplanner=False
reisplanner_weergegeven=False
reisplanner_stationsweergegeven=False
actuele_vertrektijden=False
actuele_vertrektijden_weergegeven=False
vertraging=False
vertraging_weergegeven=False
Storingen=False
storingen_weergegeven=False

root = Tk()

app = App(root)

root.mainloop()
