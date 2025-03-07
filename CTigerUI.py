from librairy.arrera_tk import *
from CArreraTiger import *

class CTigerUI:
    def __init__(self):
        # Initialisation de la classe
        self.__arrTk = CArreraTK()
        self.__objTiger = CArreraTiger("json/tigerConf.json")
        # Creation de la fenetre
        self.__rootWin = self.__arrTk.aTK(width=800, height=600, title="Arrera Store", resizable=True)
        self.__rootWin.grid_rowconfigure(0, weight=1)
        self.__rootWin.grid_columnconfigure(0, weight=1)
        # Ajout de differents frame
        self.__fmain = self.__arrTk.createFrame(self.__rootWin)
        self.__fApp1 = self.__arrTk.createFrame(self.__fmain, bg="blue")
        self.__fApp2 = self.__arrTk.createFrame(self.__fmain, bg="blue")

        # Widgets
        # FTop
        labelTitle = self.__arrTk.createLabel(self.__fmain, text="Arrera store",
                                              ptaille=25,pstyle="bolt",
                                              ppolice="Arial")
        # Fmain
        btnPara = self.__arrTk.createButton(self.__fmain, text="Paramètres")
        btnApropos = self.__arrTk.createButton(self.__fmain, text="A Propos")

        # Configuration des colonnes et lignes
        # fmain
        self.__fmain.grid_columnconfigure(0, weight=1)
        self.__fmain.grid_columnconfigure(1, weight=1)
        self.__fmain.grid_columnconfigure(2, weight=1)
        # fApp
        self.__fApp1.grid_columnconfigure(0, weight=1)
        self.__fApp1.grid_columnconfigure(1, weight=1)
        self.__fApp1.grid_columnconfigure(2, weight=1)
        self.__fApp1.grid_rowconfigure(0, weight=1)
        self.__fApp1.grid_rowconfigure(1, weight=1)
        self.__fApp1.grid_rowconfigure(2, weight=1)

        self.__fApp2.grid_columnconfigure(0, weight=1)
        self.__fApp2.grid_columnconfigure(1, weight=1)
        self.__fApp2.grid_columnconfigure(2, weight=1)
        self.__fApp2.grid_rowconfigure(0, weight=1)
        self.__fApp2.grid_rowconfigure(1, weight=1)
        self.__fApp2.grid_rowconfigure(2, weight=1)


        # Affichage
        # Fmain
        self.__fApp1.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.__fApp2.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        labelTitle.grid(row=0, column=1, sticky="n")
        btnPara.grid(row=1, column=2, sticky="se")
        btnApropos.grid(row=1, column=0, sticky="sw")

    def start(self):
        # Affichage de frame main
        self.__fmain.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.__fmain.grid_rowconfigure(0, weight=1)

        # Affichage de la fenetre
        self.__arrTk.view()

