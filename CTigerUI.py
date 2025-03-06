from librairy.arrera_tk import *
from CArreraTiger import *

class CTigerUI:
    def __init__(self):
        # Initialisation de la classe
        self.__arrTk = CArreraTK()
        self.__objTiger = CArreraTiger("json/tigerConf.json")
        # Creation de la fenetre
        self.__rootWin = self.__arrTk.aTK(width=800, height=600, title="Arrera Tiger", resizable=True)
        self.__rootWin.grid_rowconfigure(0, weight=1)
        self.__rootWin.grid_rowconfigure(1, weight=10)
        self.__rootWin.grid_columnconfigure(0, weight=1)
        # Ajout de differents frame
        fTop = self.__arrTk.createFrame(self.__rootWin, bg="blue")
        self.__fmain = self.__arrTk.createFrame(self.__rootWin,bg="red")

        # Widgets
        # FTop
        labelTitle = self.__arrTk.createLabel(fTop, text="Arrera store", ptaille=25,pstyle="bolt",ppolice="Arial",justify="left")
        # Fmain
        btnPara = self.__arrTk.createButton(self.__fmain, text="Paramètres")
        btnApropos = self.__arrTk.createButton(self.__fmain, text="A Propos")

        # Affichage
        # Fmain
        fTop.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        labelTitle.grid(row=0, column=0, sticky="nw")
        btnPara.grid(row=1, column=1, sticky="se")
        btnApropos.grid(row=1, column=0, sticky="sw")

    def start(self):
        # Affichage de frame main
        self.__fmain.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.__fmain.grid_rowconfigure(0, weight=1)
        self.__fmain.grid_columnconfigure(0, weight=1)
        # Affichage de la fenetre
        self.__arrTk.view()

