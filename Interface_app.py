from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import functions as fct
import Object as Obt

class Ui_Form(object):

    def setup_msgbox(self, info1, info2):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText(info1)
        self.msg.setInformativeText(info2)
        self.msg.setWindowTitle("Message d'erreur")
        self.msg.show()
   
    def setupUi(self, Form):
        self.output_str = ""
        self.liste = []
        self.html_string = ""
        self.matrice_profile = None
        self.liste_mot = []

        Form.setObjectName("Form")
        Form.setFixedSize(1400, 950)
        Form.setStyleSheet(""" 
        QWidget.MainWindow{
            background-color: #DAF6FA;
        }
        QPushButton{
            border : 2px solid black;
            background-color: #488D99;
            color:#CDCBCC;
            border-radius : 18px;
            font-size: 17px;
            font-weight: semi-bold;
        }
        QPushButton::disabled{
            border : 0.5px solid black;
            background-color: #007F88;
            color:#CDCBCC;
            border-radius : 18px;
            font-size: 17px;
            font-weight: semi-bold;
        }
        QPushButton::hover{
            border : 4px solid black;
            background-color: #DC741D;
            color:black;
            border-radius : 18px;
            font-weight: bold;
        }
        QLabel{
            color: #322F36;
            background-color: #B6CED1;

        }
        QLineEdit{
            border : 2px solid black;
            border-radius : 20px;
            padding : 5px;
            background-color: #B6CED1;
        }
        QTextBrowser{
            background-color: #B6CED1;
            border : 2px solid black;
        }
        QScrollArea{
            background-color: #B6CED1;
            border : 2px solid black;
        }
        """
        )



        self.output = QtWidgets.QTextBrowser(Form)
        self.output.setGeometry(QtCore.QRect(270, 10, 850, 510))
        self.output.setLineWrapMode(0)

        self.label_adn = QtWidgets.QLabel(Form)
        self.label_adn.setGeometry(QtCore.QRect(10, 505, 250, 30))
        self.label_adn.setStyleSheet("font-weight: bold; font-size: 10pt; background-color: #DAF6FA;")
        self.label_adn.setObjectName("label_seq")

        self.cadre = QtWidgets.QScrollArea(Form)
        self.cadre.setGeometry(QtCore.QRect(10, 540, 1380, 395))
        self.cadre.setWidgetResizable(True)

        self.text = QtWidgets.QLabel()
        self.text.setTextFormat(QtCore.Qt.RichText)
        self.text.setGeometry(QtCore.QRect(10, 505, 1380, 395)) 
        self.text.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.text.setStyleSheet("padding: 10px;")

        self.cadre.setWidget(self.text)

        
        # Clear
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 10, 80, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.clicked.connect(self.clear)  #FUNCTION

        # SAUVEGARDER
        self.pushButton_22 = QtWidgets.QPushButton(Form)
        self.pushButton_22.setGeometry(QtCore.QRect(100, 10, 160, 50))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.setEnabled(False)
        self.pushButton_22.clicked.connect(self.add_save)  #FUNCTION

        #--------------------------------------------------------------------------------------------------------
        # COMPLEMENT INVERSE D'UNE SEQUENCE D'ADN
        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setGeometry(QtCore.QRect(1135, 160, 250, 48))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.setEnabled(False)
        self.pushButton_20.clicked.connect(self.add_inverse)  #FUNCTION

        # TRANSCRIPTION ADN ==> ARN
        self.pushButton_19 = QtWidgets.QPushButton(Form)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.setGeometry(QtCore.QRect(1135, 218, 250, 48))
        self.pushButton_19.setEnabled(False)
        self.pushButton_19.clicked.connect(self.add_arn)  #FUNCTION
 
        # EPISSAGE DE L'ARN
        self.pushButton_18 = QtWidgets.QPushButton(Form)
        self.pushButton_18.setGeometry(QtCore.QRect(1135, 276, 250, 48))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.setEnabled(False)
        self.pushButton_18.clicked.connect(self.add_epissage)  #FUNCTION

        # FREQUENCES DES CODONS
        self.pushButton_24 = QtWidgets.QPushButton(Form)
        self.pushButton_24.setGeometry(QtCore.QRect(1135, 334, 250, 48))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.setEnabled(False)
        self.pushButton_24.clicked.connect(self.add_freq_codon)  #FUNCTION

        # TRADUCTION ARN ==> PROTEINE
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(1135, 392, 250, 48))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.clicked.connect(self.add_pro)  #FUNCTION

        # MASSE PROTEIQUE
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(1135, 450, 250, 48))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.clicked.connect(self.add_masse_pro)  #FUNCTION

        #-------------------------------------------------------------------------------------------------------------

        # FREQUENCE DES BASES
        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 80, 250, 48))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.setEnabled(False)
        self.pushButton_17.clicked.connect(self.add_freq_base)  #FUNCTION

        # TAUX DE GC
        self.pushButton_21 = QtWidgets.QPushButton(Form)
        self.pushButton_21.setGeometry(QtCore.QRect(10, 138, 250, 48))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.setEnabled(False)
        self.pushButton_21.clicked.connect(self.add_taux_gc)  #FUNCTION

        # RECHERCHER UN MOTIF
        self.label_motif = QtWidgets.QLabel(Form)
        self.label_motif.setGeometry(QtCore.QRect(10, 196, 250, 20))
        self.label_motif.setStyleSheet("font-weight: bold; font-size: 8pt; background-color: #DAF6FA;")
        self.label_motif.setObjectName("label_motif")
        self.champ_motif = QtWidgets.QLineEdit(Form)
        self.champ_motif.setGeometry(QtCore.QRect(10, 221, 250, 40))
        self.champ_motif.setEnabled(False)

        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 266, 250, 48))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.clicked.connect(self.add_motif)  #FUNCTION

        # MATRICE PROFIL D'ADN
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 324, 250, 48))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.clicked.connect(self.add_matrice_profil)  #FUNCTION

        # MUTATION DE L'ADN
        self.label_mutation = QtWidgets.QLabel(Form)
        self.label_mutation.setGeometry(QtCore.QRect(10, 382, 250, 20))
        self.label_mutation.setStyleSheet("font-weight: bold; font-size: 8pt; background-color: #DAF6FA;")
        self.label_mutation.setObjectName("label_motif")
        self.champ_mutation = QtWidgets.QLineEdit(Form)
        self.champ_mutation.setGeometry(QtCore.QRect(10, 407, 250, 40))
        self.champ_mutation.setEnabled(False)

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 452, 250, 48))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.clicked.connect(self.add_mutation)  #FUNCTION


        #----------------------------------------------------------------------------------------------------------------

        # AJOUTER UNE SEQUENCE
        self.label_lng = QtWidgets.QLabel(Form)
        self.label_lng.setGeometry(QtCore.QRect(1300, 5, 50, 40))
        self.label_lng.setStyleSheet("font: 8pt; background-color: #DAF6FA;")
        self.label_lng.setObjectName("label_lng")

        self.champ_seq_lng = QtWidgets.QLineEdit(Form)
        self.champ_seq_lng.setGeometry(QtCore.QRect(1300, 40, 40, 35))

        self.label_nbr = QtWidgets.QLabel(Form)
        self.label_nbr.setGeometry(QtCore.QRect(1350, 5, 50, 40))
        self.label_nbr.setStyleSheet("font: 8pt; background-color: #DAF6FA;")
        self.label_nbr.setObjectName("label_seq")

        self.champ_seq_nbr = QtWidgets.QLineEdit(Form)
        self.champ_seq_nbr.setGeometry(QtCore.QRect(1350, 40, 40, 35))

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1125, 10, 165, 65))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add_adn)  #FUNCTION

        # LIRE SEQUENCES A PARTIR DE FICHIER FASTA
        self.pushButton_23 = QtWidgets.QPushButton(Form)
        self.pushButton_23.setGeometry(QtCore.QRect(1125, 80, 265, 60))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(self.add_fasta)  #FUNCTION


        # LIGNE DE SEPARATION
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 60, 270, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(1120, 140, 275, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def clear(self):
        self.text.setText("") 
        self.output_str = ''
        del self.liste_mot[:]
        self.matrice_profile = None
        self.output.setText(self.output_str)
        del self.liste[:]
        self.pushButton_22.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_19.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.pushButton_21.setEnabled(False)
        self.pushButton_20.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_18.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_24.setEnabled(False)
        self.champ_motif.setEnabled(False)
        self.champ_mutation.setEnabled(False)

    def affichage(self):
        self.output_str = ''
        for obj in self.liste:
            i = 1
            # AFFICHAGE DE L'ADN
            if obj.adn != None:
                self.output_str = self.output_str + (str(i) + "--La chaine d'ADN : \n     " + obj.adn + "\n")
            # AFFICHAE DES FREQUENCES DES BASES D'ADN
            if obj.freq_base_adn != None:
                i+=1
                self.output_str = self.output_str + (str(i) + "--LES FREQUENCES DES BASES : \n     " + str(obj.freq_base_adn) + "\n")
            # AFFICHAGE DU TAUX DE GC
            if obj.taux_gc != None:
                i+=1
                self.output_str = self.output_str + (str(i) + "--LE TAUX DE GC : \n     " + str(obj.taux_gc) + "\n")
            #AFFICHAGE DE L'INVERSE DE L'ADN
            if obj.inverse != None:
                i+=1
                self.output_str = self.output_str + (str(i) + "--LE COMPLEMENT INVERSE DE LA SEQUENCE : \n     " + obj.inverse + "\n")
            # AFFICHAGE DE L'ARN 
            if obj.arn != None:
                i+=1
                self.output_str = self.output_str + (str(i) + "--TRADUCTION : ADN ==> ARN  : \n     " + obj.arn + "\n")
            # AFFICHAGE DE L'EPISSAGE DE L'ADN
            if obj.epissage != None:
                i+=1
                self.output_str = self.output_str + (str(i) + "--L'EPISSAGE DE CET ADN EST : \n     "+ str(obj.epissage) + "\n")
            # AFFICHAGE DE LA PROTEINE
            if obj.proteine != None:
                i+=1
                self.output_str = self.output_str + (str(i) + "--LA SEQUENCE DE PROTEINE : \n     " + obj.proteine + "\n")
            # AFFICHAGE DES FREQUENCES DES CODONS
            if obj.freq_codons != None:
                i+=1
                self.output_str = self.output_str + (str(i) + "--LA FREQUENCE DES CODONS  : \n     " + str(obj.freq_codons) + "\n")
            # AFFICHAGE DE LA MASSE PROTEIQUE
            if obj.masse_proteique != None:
                i+=1
                self.output_str = self.output_str + (str(i) + "--LA MASSE DE LA PROTEINE EST  : \n     " + str(obj.masse_proteique) + "\n")
            # AFFICHAGE DE LA LISTE DES MOTIFS
            if len(obj.liste_motif) != 0:
                i+=1
                self.output_str = self.output_str + (str(i) + "--LA LISTE DES MOTIFS RECHERCHES  : \n     " + str(obj.liste_motif) + "\n")

            self.output_str = self.output_str + ("\n-----------------------------------------------------------------------------------------------------------" + "\n")
            self.output_str = self.output_str + ("-----------------------------------------------------------------------------------------------------------" + "\n")

        # AFFICHAGE DE LA MATRICE PROFIL ET DU CONSENSUS
        if self.matrice_profile != None:
            self.output_str = self.output_str + ("LE CONSENSUS  :  \n     " + \
            str(self.matrice_profile[0]) + "\n" + \
                "LA MATRICE PROFIL : \n     " + \
                    'A' + str(self.matrice_profile[1]['A']) + \
                        "\n     C" + str(self.matrice_profile[1]['C']) + \
                            "\n     T" + str(self.matrice_profile[1]['T']) \
                                + "\n     G" + str(self.matrice_profile[1]['G']) + "\n")
        self.output.setText(self.output_str)

    def add_adn(self):
        try:
            x = self.champ_seq_lng.text()
            nbr = self.champ_seq_nbr.text()
            if (int(x)>0 and int(x)<150 and int(nbr)>0 and int(nbr)<50):
                i =0
                while i< int(nbr) :
                    object = Obt.Obj(fct.Generate_adn(int(x)))
                    self.liste.append(object)
                    i += 1
                self.champ_seq_lng.setText('')
                self.champ_seq_nbr.setText('')           
                self.graph_adn()
                self.affichage()

                self.champ_motif.setEnabled(True)
                self.champ_mutation.setEnabled(True)

                self.pushButton_22.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_19.setEnabled(True)
                self.pushButton_17.setEnabled(True)
                self.pushButton_21.setEnabled(True)
                self.pushButton_20.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.pushButton_10.setEnabled(True)
                self.pushButton_9.setEnabled(True)
                self.pushButton_18.setEnabled(True)

                self.pushButton_11.setEnabled(False)
                self.pushButton_24.setEnabled(False)
                self.pushButton_12.setEnabled(False)
            else:
                self.setup_msgbox("Veuillez inserer le nombre (nbr) de sequences et leur longueur (len)", "1<len<50 && 1<nbr<50")
                self.champ_seq_lng.setText('')
                self.champ_seq_nbr.setText('') 
        except:
            self.setup_msgbox("Veuillez inserer le nombre (nbr) de sequences et leur longueur (len)", " nbr et len doivent etre des entiers \n 1<len<150 && 1<nbr<50")
            self.champ_seq_lng.setText('')
            self.champ_seq_nbr.setText('') 
        
    def add_arn(self):
        self.pushButton_11.setEnabled(True)
        self.pushButton_24.setEnabled(True)
        for i in range(len(self.liste)):
            if self.liste[i].adn != None:
                self.liste[i].set_arn()
        self.affichage()

    def add_pro(self):
        self.pushButton_12.setEnabled(True)
        for obj in self.liste:
            if obj.arn != None:
                obj.set_proteine()
        self.affichage()
    
    def add_freq_base(self):
        #self.listView.clear()
        for obj in self.liste:
            if obj.adn != None:
                obj.set_freq_base_adn()
        self.affichage()
    
    def add_taux_gc(self):
        for obj in self.liste:
            if obj.adn != None:
                obj.set_taux_gc()
        self.affichage()
    
    def add_inverse(self):
        for obj in self.liste:
            if obj.adn != None:
                obj.set_inverse()
        self.affichage()
    
    def add_masse_pro(self):
        for obj in self.liste:
            if obj.proteine != None:
                obj.set_masse_proteique()
        self.affichage()

    def add_motif(self):
        try:
            mot = self.champ_motif.text()
            mot = mot.upper()
            self.liste_mot.append(mot)
            for obj in self.liste:
                if obj.adn != None:
                    obj.set_liste_motif(mot)
            self.champ_motif.setText('')
            self.affichage()
        except:
            self.champ_motif.setText('')
            self.setup_msgbox("Motif incorrecte", " Veuillez entrer une chaine de caractere du motif a rechercher")

    def add_mutation(self):
        try:
            x = int(self.champ_mutation.text())
            if x>0 and x<21 :
                for obj in self.liste:
                    if obj.adn != None:
                        obj.set_mutation(x)
                        if obj.arn != None:
                            obj.set_arn()
                        if obj.proteine != None:
                            obj.set_proteine()
                            if obj.masse_proteique != None:
                                obj.set_masse_proteique()
                        if obj.freq_base_adn != None:
                            obj.set_freq_base_adn()
                        if obj.taux_gc != None:
                            obj.set_taux_gc()
                        if obj.inverse != None:
                            obj.set_inverse()
                        if obj.freq_codons != None:
                            obj.set_freq_cod()
                        obj.epissage = None

                        if len(self.liste_mot) != 0:
                            obj.liste_motif={}
                            for elt in self.liste_mot:
                                obj.set_liste_motif(elt)

                        lstt = []
                        if self.matrice_profile != None:
                            for obj in self.liste:
                                if obj.adn != None:
                                    lstt.append(obj.adn)
                if len(lstt) != 0 :
                    self.matrice_profile = None
                    self.matrice_profile = fct.profile_consensus(lstt)
                
                self.champ_mutation.setText('')
                self.graph_adn()
                self.affichage()
            else:
                self.champ_mutation.setText('')
                self.setup_msgbox("Entree Eronee", "Veuillez entrer un nombre de mutation entre 1 et 20")
        except:
            self.champ_mutation.setText('')
            self.setup_msgbox("Entree Eronee", "Veuillez entrer le nombre de mutation")

    def add_freq_codon(self):
        for obj in self.liste:
            if obj.arn != None:
                obj.set_freq_cod()
        self.affichage()

    def add_matrice_profil(self):
        lstt = []
        for obj in self.liste:
            if obj.adn != None:
                lstt.append(obj.adn)
        self.matrice_profile = fct.profile_consensus(lstt)
        self.affichage()
    
    def add_epissage(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        try:
            for obj in self.liste:
                if obj.adn != None:
                    obj.set_epissage(filename)
            self.affichage()
        except:
            self.setup_msgbox("Entree Eronee", "Veuillez choisir un fichier FASTA contenant les introns")
    
    def add_save(self):
        try:
            f = open("data.txt", 'w')
            f.write(self.output_str)
            f.close()
            self.setup_msgbox("Sauvegarde avec succees", "Verifier le fichier DATA.txt")
        except:
            pass

    def add_fasta(self):
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName()
            if len(filename) > 0 :
                fich = fct.generate_fasta(filename[0])
                if len(fich) > 0 :
                    for adn in fich.values():
                        self.liste.append(Obt.Obj(adn))
                    # print(lst)
                    self.affichage()
                    self.graph_adn()

                    self.champ_motif.setEnabled(True)
                    self.champ_mutation.setEnabled(True)

                    self.pushButton_22.setEnabled(True)
                    self.pushButton_9.setEnabled(True)
                    self.pushButton_7.setEnabled(True)
                    self.pushButton_19.setEnabled(True)
                    self.pushButton_17.setEnabled(True)
                    self.pushButton_21.setEnabled(True)
                    self.pushButton_20.setEnabled(True)
                    self.pushButton_8.setEnabled(True)
                    self.pushButton_10.setEnabled(True)
                    self.pushButton_18.setEnabled(True)

                    self.pushButton_11.setEnabled(False)
                    self.pushButton_24.setEnabled(False)
                    self.pushButton_12.setEnabled(False)
        except:
            self.setup_msgbox("Fichier choisi errone", "Veuillez choisir un autre fichier Fasta")
    
    def graph_adn(self):
        self.html_string = ""
        num = 1
        for elt in self.liste:
            val = str(num) + "-- "
            string = "<html><head/><body style=\"padding: 5px 10px; color: black;  font-size: 22px; line-height:20%;\">" + \
              val
            for base in elt.adn:
                if base == 'A':
                    string = string + "<span style=\" color: #FFFFFF; background-color: red;\"> A </span>"
                if base == 'T':
                    string = string + "<span style=\" color: #FFFFFF; background-color: green;\"> T </span>"
                if base == 'C':
                    string = string + "<span style=\" color: #FFFFFF; background-color: blue;\"> C </span>"
                if base == 'G':
                    string = string + "<span style=\" color: #FFFFFF; background-color:orange;\"> G </span>"
            string = string + "<p></body></html>"

            self.html_string = self.html_string + string
            num = num + 1
        self.text.setText(self.html_string)               

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BIO-INFORMATIC APP"))
        self.pushButton_7.setText(_translate("Form", "Clear"))
        self.pushButton_22.setText(_translate("Form", "Sauvegarder"))
        self.pushButton_23.setText(_translate("Form", "Lire un fichier Fasta"))
        self.pushButton_19.setText(_translate("Form", "Transcription"))
        self.pushButton_18.setText(_translate("Form", "L\'epissage d\'ARN"))
        self.pushButton_11.setText(_translate("Form", "Traduction"))
        self.pushButton_12.setText(_translate("Form", "La masse proteique"))
        self.pushButton_17.setText(_translate("Form", "Frequences des Bases"))
        self.pushButton_21.setText(_translate("Form", "Taux de GC"))
        self.pushButton_20.setText(_translate("Form", "Complement inverse"))
        self.label_mutation.setText(_translate("Form", "Nombre de mutation : "))
        self.pushButton_8.setText(_translate("Form", "Mutation"))
        self.label_motif.setText(_translate("Form", "Motif a rechercher : "))
        self.pushButton_9.setText(_translate("Form", "Rechercher un motif"))
        self.pushButton_10.setText(_translate("Form", "La matrice profil d\'ADN"))
        self.label_lng.setText(_translate("Form", "len :"))
        self.label_nbr.setText(_translate("Form", "nbr :"))
        self.pushButton_2.setText(_translate("Form", "Sequences aleatoire"))
        self.pushButton_24.setText(_translate("Form", "Frequences des codons"))
        self.label_adn.setText(_translate("Form", " Les sequences d'ADN : "))


