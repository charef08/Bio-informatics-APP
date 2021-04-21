import sys
import functions as fct

class Obj:
    
    #adn, arn, proteine, freq_base_adn, taux_gc, inverse, freq_codons, epissage, liste_motif, matrice_profile, masse_proteique
    def __init__(self, adn):
        self.adn = adn
        self.arn = None
        self.proteine = None
        self.freq_base_adn = None
        self.taux_gc = None
        self.inverse = None
        self.freq_codons = None
        self.masse_proteique = None 
        self.epissage = None
        self.liste_motif = {}

    def set_adn(self, length):
        self.adn = fct.Generate_adn(length)
    
    def set_mutation(self, num):
        self.adn = fct.mutationAleatoire(self.adn, num)
    
    def set_arn(self):
        self.arn = fct.Transcription(self.adn)
    
    def set_proteine(self):
        self.proteine = fct.Traduction(self.arn)
    
    def set_freq_base_adn(self):
        self.freq_base_adn = fct.Count_nucleotide_ADN(self.adn)
    
    def set_taux_gc(self):
        self.taux_gc = fct.Taux_GC(self.adn)
    
    def set_inverse(self):
        self.inverse = fct.Cmplt_inverse(self.adn)
    
    def set_freq_cod(self):
        self.freq_codons = fct.Codons_freq(self.arn)
    
    def set_masse_proteique(self):
        self.masse_proteique = fct.Masse_Proteique(self.proteine)
    
    def set_liste_motif(self, motif):
        lst = fct.motif_ADN(self.adn, motif)
        if len(lst)>0:
            self.liste_motif[motif] = lst
    
    def set_epissage(self, fichier):
        self.epissage = fct.Epissage_ARN(self.adn, fichier)


