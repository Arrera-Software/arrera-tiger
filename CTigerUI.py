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
        self.__rootWin.grid_rowconfigure(1, weight=10)
        self.__rootWin.grid_columnconfigure(0, weight=1)
        # Ajout de differents frame
        fTop = self.__arrTk.createFrame(self.__rootWin)
        self.__fmain = self.__arrTk.createFrame(self.__rootWin)
        self.__fPara = self.__arrTk.createFrame(self.__rootWin)
        self.__fInstalled = self.__arrTk.createFrame(self.__rootWin)
        self.__fApp1 = self.__arrTk.createFrame(self.__fmain)
        self.__fApp2 = self.__arrTk.createFrame(self.__fmain)

        # Widgets
        # FTop
        labelTitle = self.__arrTk.createLabel(fTop, text="Arrera store",
                                              ptaille=25,pstyle="bolt",
                                              ppolice="Arial")
        self.__btnInstall = self.__arrTk.createButton(fTop, text="Application installer")
        # Fmain
        btnPara = self.__arrTk.createButton(self.__fmain, text="Paramètres",command=self.__activePara)
        btnApropos = self.__arrTk.createButton(self.__fmain, text="A Propos", command=self.__apropos)
        # FPara
        lableTitlePara = self.__arrTk.createLabel(self.__fPara, text="Parametre",
                                                  ppolice="Arial",ptaille=25,pstyle="bold")
        btnSetEmplacement = self.__arrTk.createButton(self.__fPara, text="Emplacement de application Arrera")
        btnBackAcceuilPara = self.__arrTk.createButton(self.__fPara, text="Retour", command=self.__backMain)

        # Configuration des colonnes et lignes
        # fmain
        self.__fmain.grid_columnconfigure(0, weight=1)
        self.__fmain.grid_columnconfigure(1, weight=1)
        self.__fmain.grid_rowconfigure(0, weight=10)
        self.__fmain.grid_rowconfigure(1, weight=1)
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
        # fTop
        fTop.grid_columnconfigure(0, weight=1)
        fTop.grid_columnconfigure(1, weight=1)
        fTop.grid_columnconfigure(2, weight=1)
        # FPara
        self.__fPara.grid_columnconfigure(0, weight=1)
        self.__fPara.grid_columnconfigure(1, weight=10)
        self.__fPara.grid_columnconfigure(2, weight=1)
        self.__fPara.grid_rowconfigure(0, weight=1)
        self.__fPara.grid_rowconfigure(1, weight=1)
        self.__fPara.grid_rowconfigure(2, weight=1)


        # Affichage
        # Fmain
        fTop.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.__fApp1.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.__fApp2.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        btnPara.grid(row=1, column=1, sticky="se")
        btnApropos.grid(row=1, column=0, sticky="sw")
        # FTop
        labelTitle.grid(row=0, column=0, sticky="nw")
        self.__btnInstall.grid(row=0, column=1, sticky="nsew")
        # FPara
        lableTitlePara.grid(row=0, column=1, sticky="n")
        btnSetEmplacement.grid(row=1, column=1)
        btnBackAcceuilPara.grid(row=2, column=1, sticky="se")

    def start(self):
        # Affichage de frame main
        self.__backMain()
        # Affichage de la fenetre
        self.__arrTk.view()

    def __backMain(self):
        self.__fPara.grid_forget()
        self.__fInstalled.grid_forget()
        self.__fmain.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    def __apropos(self):
        self.__arrTk.aproposWindows("Arrera Store",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "")

    def __activePara(self):
        self.__fPara.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.__fInstalled.grid_forget()
        self.__fmain.grid_forget()

