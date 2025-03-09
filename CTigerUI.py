from librairy.arrera_tk import *
from CArreraTiger import *
import tkinter.filedialog as fd
import tkinter.messagebox as mbox
import socket
import shutil
import threading as th

class CTigerUI:
    def __init__(self):
        # Initialisation de la classe
        self.__arrTk = CArreraTK()
        self.__objTiger = CArreraTiger("json/tigerConf.json")
        self.__theardAction = th.Thread()
        # Emplacement de l'icon
        dectOS = OS()
        if (dectOS.osWindows()==True):
            iconWin = "img/arrera-tiger.ico"
        else :
            iconWin = "img/arrera-tiger.png"
        # Creation de la fenetre
        self.__rootWin = self.__arrTk.aTK(width=800, height=600,
                                          title="Arrera Store",
                                          resizable=True, icon=iconWin)
        # Ajout de la fonction de fermeture
        self.__rootWin.protocol("WM_DELETE_WINDOW",self.__closeTiger)
        self.__rootWin.grid_rowconfigure(0, weight=1)
        self.__rootWin.grid_rowconfigure(1, weight=10)
        self.__rootWin.grid_columnconfigure(0, weight=1)
        # Ajout de differents frame
        fTop = self.__arrTk.createFrame(self.__rootWin)
        self.__fmain = self.__arrTk.createFrame(self.__rootWin)
        self.__fPara = self.__arrTk.createFrame(self.__rootWin)
        self.__fInstalled = self.__arrTk.createFrame(self.__rootWin)
        self.__fAppAssistant = self.__arrTk.createFrame(self.__fmain)
        self.__fAppOtherApp = self.__arrTk.createFrame(self.__fmain)
        self.__fAppInfo = self.__arrTk.createFrame(self.__rootWin,bg="red")
        self.__fInstall = self.__arrTk.createFrame(self.__rootWin)
        # Initilisation des icon
        imagePara = self.__arrTk.createImage(pathLight="img/settings.png",
                                             pathDark="img/settings.png",
                                             tailleY=35,tailleX=35)
        imageapropos = self.__arrTk.createImage(pathLight="img/apropos.png",
                                             pathDark="img/apropos.png",
                                             tailleY=35,tailleX=35)
        # Widgets
        # FTop
        labelTitle = self.__arrTk.createLabel(fTop, text="Arrera store",
                                              ptaille=25,pstyle="bolt",
                                              ppolice="Arial")
        self.__btnInstall = self.__arrTk.createButton(fTop)
        # Fmain
        btnPara = self.__arrTk.createButton(self.__fmain,command=self.__activePara,
                                            bg="#e0e0e0", hoverbg="#949494",
                                            width=35,height=35,image=imagePara)
        btnApropos = self.__arrTk.createButton(self.__fmain, command=self.__apropos,
                                               bg="#e0e0e0", hoverbg="#949494",
                                               width=35,height=35,image=imageapropos)
        # FPara
        lableTitlePara = self.__arrTk.createLabel(self.__fPara, text="Parametre",
                                                  ppolice="Arial",ptaille=25,pstyle="bold")
        btnSetEmplacement = self.__arrTk.createButton(self.__fPara,
                                                      text="Emplacement de application Arrera",
                                                      command=self.__setEmplacement)
        btnBackAcceuilPara = self.__arrTk.createButton(self.__fPara, text="Retour", command=self.__backMain)
        # fInstalled
        labelTitleInstalled = self.__arrTk.createLabel(self.__fInstalled, text="Application installer",
                                                       ppolice="Arial",ptaille=25,pstyle="bold")
        # fInstall
        self.__labelLoad = self.__arrTk.createLabel(self.__fInstall)

        # fAppAssistant
        self.__listBTNAppAssistant = []
        # fAppOtherApp
        self.__listBTNAppOtherApp = []

        #fAppInfo
        self.__labelTitleAppInfo = self.__arrTk.createLabel(self.__fAppInfo)
        self.__labelIMGAppInfo = self.__arrTk.createLabel(self.__fAppInfo)
        self.__btnInstallUnistallAppInfo = self.__arrTk.createButton(self.__fAppInfo)
        self.__btnMajAppInfo = self.__arrTk.createButton(self.__fAppInfo,text="Mettre à jour")
        self.__btnBackAppInfo = self.__arrTk.createButton(self.__fAppInfo, text="Retour", command=lambda : self.__backMain())
        # Configuration des colonnes et lignes
        # fmain
        self.__fmain.grid_columnconfigure(0, weight=1)
        self.__fmain.grid_columnconfigure(1, weight=1)
        self.__fmain.grid_rowconfigure(0, weight=10)
        self.__fmain.grid_rowconfigure(1, weight=1)
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
        # FInstalled
        self.__fInstalled.grid_columnconfigure(0, weight=1)
        self.__fInstalled.grid_columnconfigure(1, weight=10)
        self.__fInstalled.grid_columnconfigure(2, weight=1)
        self.__fInstalled.grid_rowconfigure(0, weight=1)
        self.__fInstalled.grid_rowconfigure(1, weight=1)
        self.__fInstalled.grid_rowconfigure(2, weight=1)
        # fAppInfo
        self.__fAppInfo.grid_columnconfigure(0, weight=1)
        self.__fAppInfo.grid_columnconfigure(1, weight=1)
        self.__fAppInfo.grid_columnconfigure(2, weight=1)
        self.__fAppInfo.grid_rowconfigure(0, weight=1)
        self.__fAppInfo.grid_rowconfigure(1, weight=1)
        self.__fAppInfo.grid_rowconfigure(2, weight=1)
        # fAppAssistant
        self.__fAppAssistant.columnconfigure(0, weight=1)
        # fAppOtherApp
        self.__fAppOtherApp.columnconfigure(0, weight=1)
        # fInstall
        self.__fInstall.grid_rowconfigure(0, weight=1)
        self.__fInstall.grid_columnconfigure(0, weight=1)


        # Affichage
        # Fmain
        fTop.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        btnPara.grid(row=1, column=1, sticky="se")
        btnApropos.grid(row=1, column=0, sticky="sw")
        # FTop
        labelTitle.grid(row=0, column=0, sticky="nw")
        self.__btnInstall.grid(row=0, column=1, sticky="nsew")
        # FPara
        lableTitlePara.grid(row=0, column=1, sticky="n")
        btnSetEmplacement.grid(row=1, column=1)
        btnBackAcceuilPara.grid(row=2, column=1, sticky="se")
        # fInstalled
        labelTitleInstalled.grid(row=0, column=1, sticky="n")
        # fAppInfo
        self.__labelTitleAppInfo.grid(row=0, column=1, sticky="n")
        self.__labelIMGAppInfo.grid(row=1, column=0)
        self.__btnInstallUnistallAppInfo.grid(row=2, column=2, sticky="n")
        self.__btnBackAppInfo.grid(row=2, column=2)
        # fAppAssistant
        self.__fAppAssistant.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        # fAppOtherApp
        self.__fAppOtherApp.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        # fInstall
        self.__labelLoad.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def start(self):
        # Affichage de frame main
        self.__backMain()
        # teste si le pc est connecter a internet
        internet = self.__testConnectInternet()
        if (internet == False):
            mbox.showerror("Erreur", "Pas de connexion internet")
            self.__rootWin.quit()
            return
        # Chargement des depots
        if (self.__objTiger.loadDepots("https://arrera-software.fr/depots.json") == False):
            mbox.showerror("Erreur", "Erreur lors du chargement des dépôts")
            self.__rootWin.quit()
            return
        # Chargement de l'emplacement
        sortieFolder = self.__objTiger.loadEmplacementFile()
        if (sortieFolder == False):
            self.__setEmplacement()
        self.__viewBTNApp()
        # Affichage de la fenetre
        self.__arrTk.view()

    def __viewBTNApp(self):
        listSoftAssistant = ["arrera-interface","six","arrera-copilote","ryley"]
        listSoft = self.__objTiger.getSoftAvailable()

        for i in range(len(listSoft)):
            if (listSoft[i] in listSoftAssistant):
                self.__listBTNAppAssistant.append(self.__arrTk.createButton(
                    self.__fAppAssistant,
                    text=self.__formatTexte(listSoft[i]),
                    command= lambda software=listSoft[i]: self.__viewInfoApp(software)))
            else:
                if listSoft[i] != "arrera-tiger":
                    self.__listBTNAppAssistant.append(self.__arrTk.createButton(
                        self.__fAppOtherApp,
                        text=self.__formatTexte(listSoft[i]),
                        command= lambda software=listSoft[i]: self.__viewInfoApp(software)))

        for i in range(len(self.__listBTNAppAssistant)):
            self.__listBTNAppAssistant[i].grid(row=i, column=0, padx=5, pady=15, sticky="ew")

        for i in range(len(self.__listBTNAppOtherApp)):
            self.__listBTNAppAssistant[i].grid(row=i, column=0, padx=5, pady=15, sticky="ew")



    def __backMain(self):
        self.__fPara.grid_forget()
        self.__fAppInfo.grid_forget()
        self.__fInstalled.grid_forget()
        self.__fInstall.grid_forget()
        self.__fmain.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.__btnInstall.configure(text="Application installer"
                                    ,command=self.__activeInstalled)

    def __apropos(self):
        self.__arrTk.aproposWindows("Arrera Store",
                                    "img/arrera-tiger.png",
                                    "",
                                    "Copyright Arrera Software by Baptiste P 2023-2025",
                                    "https://github.com/Arrera-Software/arrera-tiger",
                                    "https://arrera-software.fr/")

    def __activePara(self):
        self.__fPara.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.__fInstalled.grid_forget()
        self.__fmain.grid_forget()
        self.__fAppInfo.grid_forget()

    def __activeInstalled(self):
        self.__fPara.grid_forget()
        self.__fAppInfo.grid_forget()
        self.__fInstalled.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.__btnInstall.configure(text="Application",command=self.__backMain)
        self.__fmain.grid_forget()

    def __setEmplacement(self):
        mbox.showinfo("Information",
                      "Sélectionnez l'emplacement où vous souhaitez installer les logiciels Arrera Software.")
        directory = fd.askdirectory()
        while directory == "":
            mbox.showerror("Erreur", "Veuillez sélectionner un emplacement valide.")
            directory = fd.askdirectory()

        sortieFolder = self.__objTiger.setEmplacementArreraSoft(directory)
        if (sortieFolder == True):
            mbox.showinfo("Information", "Emplacement enregistré.")
        else:
            mbox.showerror("Erreur", "Erreur lors de l'enregistrement de l'emplacement.")

    def __testConnectInternet(self):
        try:
            # Tente de se connecter au serveur
            socket.setdefaulttimeout(3)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8",53))
            return True
        except socket.error:
            return False

    def __viewInfoApp(self,soft:str):
        listSoftInstalled = self.__objTiger.getSoftInstall()
        listSoftUpdated = self.__objTiger.checkUpdate()
        self.__fAppInfo.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.__fPara.grid_forget()
        self.__fInstalled.grid_forget()
        self.__fmain.grid_forget()
        self.__labelTitleAppInfo.configure(text=self.__formatTexte(soft))
        self.__labelIMGAppInfo.configure(image=self.__getImageSoft(soft),text="")
        if soft in listSoftInstalled:
            self.__btnInstallUnistallAppInfo.configure(text="Désinstaller",command=lambda : self.__viewUninstall(soft))
        else :
            self.__btnInstallUnistallAppInfo.configure(text="Installer",command=lambda : self.__viewInstall(soft))

        if (len(listSoftUpdated) !=0):
            if soft in listSoftUpdated:
                self.__btnMajAppInfo.configure(command=lambda : self.__viewMaj(soft))
                self.__btnMajAppInfo.grid(row=2, column=0, sticky="n")
            else :
                self.__btnMajAppInfo.grid_forget()


    def __formatTexte(self,texte:str):
        texte = texte.replace("-"," ")
        mots = texte.split(" ")
        mots_maj = [mot.capitalize() for mot in mots]
        texte_maj = " ".join(mots_maj)
        return texte_maj

    def __getImageSoft(self, nameSoft):
        file_path = f"img/tmp/{nameSoft}.png"
        url = self.__objTiger.getIMGSoft(nameSoft)

        response = requests.get(url)
        if response.status_code != 200:
            return self.__arrTk.createImage("img/arrera-tiger.png",tailleX=250,tailleY=250)
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            response = requests.get(url, stream=True)
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return self.__arrTk.createImage(file_path,tailleX=250,tailleY=250)

        except requests.exceptions.RequestException as e:
            return self.__arrTk.createImage("img/arrera-tiger.png",tailleX=250,tailleY=250)

    def __closeTiger(self):
        self.__rootWin.quit()
        self.__rootWin.destroy()
        try:
            if os.path.exists("img/tmp"):
                shutil.rmtree("img/tmp")
                return True
            return False
        except Exception as e:
            return False

    def __installApp(self,soft):
        self.theardAction = th.Thread(target=self.__objTiger.install,args=(soft,))
        self.theardAction.start()

    def __viewInstall(self,soft):
        self.__fPara.grid_forget()
        self.__fInstalled.grid_forget()
        self.__fmain.grid_forget()
        self.__fAppInfo.grid_forget()
        self.__fInstall.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.__labelLoad.configure(text=f"Installation de {soft} en cours ...")
        self.__installApp(soft)
        self.__rootWin.after(100, self.__checkInstall)

    def __checkInstall(self):
        if (self.theardAction.is_alive()):
            self.__rootWin.after(100, self.__checkInstall)
        else:
            mbox.showinfo("Information", "Installation terminée")
            del self.theardAction
            self.theardAction = None
            self.__backMain()

    def __uninstallApp(self,soft):
        self.theardAction = th.Thread(target=self.__objTiger.uninstall,args=(soft,))
        self.theardAction.start()

    def __viewUninstall(self,soft):
        self.__fPara.grid_forget()
        self.__fInstalled.grid_forget()
        self.__fmain.grid_forget()
        self.__fAppInfo.grid_forget()
        self.__fInstall.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.__labelLoad.configure(text=f"Désinstallation de {soft} en cours ...")
        self.__uninstallApp(soft)
        self.__rootWin.after(100, self.__checkUninstall())

    def __checkUninstall(self):
        if (self.theardAction.is_alive()):
            self.__rootWin.after(100, self.__checkUninstall)
        else:
            mbox.showinfo("Information", "Désinstallation terminée")
            del self.theardAction
            self.theardAction = None
            self.__backMain()

    def __majApp(self,soft):
        self.theardAction = th.Thread(target=self.__objTiger.update,args=(soft,))
        self.theardAction.start()

    def __viewMaj(self,soft):
        self.__fPara.grid_forget()
        self.__fInstalled.grid_forget()
        self.__fmain.grid_forget()
        self.__fAppInfo.grid_forget()
        self.__fInstall.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.__labelLoad.configure(text=f"Mise a jour de {soft} en cours ...")
        self.__majApp(soft)
        self.__rootWin.after(100, self.__checkMaj)

    def __checkMaj(self):
        if (self.theardAction.is_alive()):
            self.__rootWin.after(100, self.__checkMaj)
        else:
            mbox.showinfo("Information", "Mise a jour terminée")
            del self.theardAction
            self.theardAction = None
            self.__backMain()
