from librairy.arrera_tk import *
from CArreraTiger import *

class CTigerUI:
    def __init__(self):
        # Initialisation de la classe
        self.__arrTk = CArreraTK()
        self.__objTiger = CArreraTiger("json/tigerConf.json")
        # Creation de la fenetre
        self.__rootWin = self.__arrTk.aTK(width=800, height=600, title="Arrera Tiger")

    def start(self):
        # Affichage de la fenetre
        self.__arrTk.view()

