from random import randint

# FONCTION QUI GENERE UNE CHAINE D'ADN D'AU PLUS NUMBER NUCLEOTIDES
def Generate_adn(number: int) -> str:
    """Genere une seq d'adn aleatoire de taille number"""
    ADN = ''
    i=1
    while i <= number :
        ADN += 'AGCT'[randint(0, 3)]
        i+= 1


    return ADN

#-------------------------------------------------------------------------------------------------------

# FONCTION QUI VERIFIE LA VALDITE DE LA CHAINE D'ADN GENEREE
def Validate_adn(ADN: str) -> bool:
    """verifie la validite d'une seq d'adn"""
    if len(ADN) > 0:
        ADN = ADN.upper()
        for i in ADN:
            if i not in ['A', 'C', 'G', 'T']:
                return False
        return True
    else:
        return False

#-------------------------------------------------------------------------------------------------------

# FONCTION QUI LIT UN FICHIER FASTE
def generate_fasta(fasta_file : str) -> str:
    """ Recupere les seq d'adn dans un fichier fasta """
    with open(fasta_file, 'r') as f:
        data = {}
        ind = ""
        adn = ""
        for line in f:
            if line[0] == ">":
                if len(adn) > 1 and len(ind) > 1:
                    if Validate_adn(adn):
                        data[ind] = adn
                ind = line.strip()
                adn = ""
            else:
                adn = adn + line.strip()
        else:
            if Validate_adn(adn):
                data[ind] = adn
    return data
#-------------------------------------------------------------------------------------------------------

# FONCTION QUI VERIFIE LA VALDITE D'UNE SEQUENCE D'ARN
def Validate_arn(ARN):
    if len(ARN) > 0 :
        ARN = ARN.upper()
        for i in ARN:
            if i not in ['A', 'C', 'G', 'U']:
                return False
        return True
    else:
        return False

#-------------------------------------------------------------------------------------------------------

# CALCUL DES FREQUENCES DES BASES NUCLEIQUES DANS LA FREQUENCE D'ADN 
def Count_nucleotide_ADN(ADN : str) -> dict:
    """ retourne un dictionnaire des frequences des nucleotides d'une seq d'adn """
    ADN = ADN.upper()
    if Validate_adn(ADN):
        return { 
          'A' : ADN.count('A'), 
          'C' : ADN.count('C'),
          'G' : ADN.count('G'),
          'T' : ADN.count('T')
        }
    else: 
        print(" LA CHAINE EN ENTREE N'EST PAS VALIDE ")

#-------------------------------------------------------------------------------------------------------

def Count_nucleotide_ARN(ARN):
    ARN = ARN. upper()
    if Validate_arn(ARN):
        return {
            'A' : ARN.count('A'), 
            'C' : ARN.count('C'),
            'G' : ARN.count('G'),
            'U' : ARN.count('U')
        }
    else:
        print(" LA CHAINE EN ENTREE N'EST PAS VALIDE ")

#-------------------------------------------------------------------------------------------------------

# TRANSCRIPTION ADN ===> ARN
def Transcription(seq : str)-> str:
    """ - retourne une seq d'arn \n
        - remplace les T par U de la seq d'adn en entree """
    seq=seq.upper()
    ARN=seq.replace('T','U')
    return ARN

#-------------------------------------------------------------------------------------------------------

# TRADUCTION ARN ===> PROTEINE
def Traduction(ARN: str) -> str:
    """ - Traduit une seq d'arn en proteine en utilisant la table des codons """
    # TABLE DES CODONS D'ARN
    RNA_codon_table = {'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys', 'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
    'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---', 'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Urp',
    'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg', 'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
    'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg', 'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
    'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser', 'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
    'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg', 'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
    'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly', 'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
    'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly', 'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'}
    ARN = ARN.upper()
    if Validate_arn(ARN):
        i = ARN.find('AUG')
        prtn = ''
        while i<len(ARN)-2 :
            tmp = ''
            tmp += ARN[i:i+3]
            try:
              x = RNA_codon_table[tmp]
              prtn += x[0]
              i+=3
            except:
                i+=1
        i=0 
        # S'arreter au premier vide 

        # prtn2 = ''
        # while i<len(prtn) :
        #     if prtn[i] != '-' :
        #         prtn2 += prtn[i]
        #         i += 1
        #     else :
        #         break
        # return prtn2
        return prtn
    else: 
        print(" LA CHAINE D'ARN EN ENTREE N'EST PAS VALIDE")

#-------------------------------------------------------------------------------------------------------

# FONCTION QUI CALCULE LE COMPLEMENT INVERSE D'UNE CHAINE D'ADN
def Cmplt_inverse(ADN : str) -> str:
    """ - Elle inverse une seq d'ADN selon le dictionnaire d'inverse """
    ADN = ADN.upper()
    if Validate_adn(ADN):
        dict_inverse = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        inv = ''
        liste = []
        i = len(ADN)-1
        while i >= 0:
            liste.append(dict_inverse[ADN[i]])
            i -= 1
        for j in liste:
            inv += j
        return inv
    else:
        print("LA CHAINE D'ADN EN ENTREE N'EST PAS VALIDE")

#-------------------------------------------------------------------------------------------------------

# FONCTION QUI CALCULE LE TAUX DE 'GC' DANS UNE SEQUENCE D'ADN 
def Taux_GC(ADN : str) -> float:
    """ - Calcule le pourcentage de G et C dans une seq d'ADN """
    ADN = ADN.upper()
    if Validate_adn(ADN):
        x = ADN.count('G')
        x += ADN.count('C')
        return (x/len(ADN))*100
    else:
        print("LA CHAINE D'ADN EN ENTREE N'EST PAS VALIDE")

#-------------------------------------------------------------------------------------------------------

# FONCTION QUI CALCULE LES FREQUENCES DE CODONS DANS UNE CHAINE D'ADN
def Codons_freq(ARN: str)-> dict:
    """ - Calcule les frequences de codons dans une sequence d'ARN """
    ARN = ARN.upper()
    RNA_codon_table = {'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys', 'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
    'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---', 'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Urp',
    'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg', 'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
    'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg', 'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
    'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser', 'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
    'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg', 'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
    'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly', 'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
    'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly', 'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'}
    freq_cod = {}
    if Validate_arn(ARN):
        i=0
        while i<len(ARN)-2 :
            tmp = ''
            tmp += ARN[i:i+3]
            try:
                if tmp in RNA_codon_table:
                    if tmp in freq_cod:
                        freq_cod[tmp] +=1
                    else:
                        freq_cod[tmp] = 1
                i+=3
            except:
                i+=1
        return freq_cod
    else:
        print(" LA CHAINE D'ARN EN ENTREE N'EST PAS VALIDE")

#-------------------------------------------------------------------------------------------------------

# FONCTION QUI FAIT DES MUTATIONS ALEATOIRES
def mutationAleatoire(ADN : str, n : int):
    """ - change la valeur de n nucleotides de la seq d'ADN \n
        - les nucleotides sont differents selon la position  """
    ADN = ADN.upper()
    if Validate_adn(ADN):
        ADN = ADN.upper()
        t = []
        l = []
        x = 1
        i = 0
        for nucleotide in ADN:
            l.append(nucleotide)
        t.append(randint(0, len(ADN) - 1))
        while x < n:
            randPos = randint(0, (len(ADN) - 1))
            if randPos not in t:
                t.append(randPos)
                x = x + 1
        while i < (len(t)):
            choice = 'AGCT'[randint(0, 3)]
            if (choice != l[t[i]]):
                l[t[i]] = choice
                i = i + 1
        ADNmut = "".join(l)
        return ADNmut
    else: print("LA CHAINE D'ADN ENTREE N'EST PAS VALIDE")

#-------------------------------------------------------------------------------------------------------

# FONCTION QUI CHERCHE UN MOTIF DANS UNE CHAINE ADN
def motif_ADN(s1 : str, s2 : str):
    """ - cherche les positions de s2 dans s1 \n
        - retourne la liste des positions """
    s1 = s1.upper()
    s2 = s2.upper()
    if Validate_adn(s1) and Validate_adn(s2):
            l= []
            for i in range(len(s1)):
                if s2 == s1[i: i+len(s2)]:
                    l.append(i+1)
            return(l)
    else: print("CHAINES EN ENTREE INVALIDES")

#-------------------------------------------------------------------------------------------------------

# FONCTION QUI CALCULE LA MASSE PROTEIQUE
def Masse_Proteique(P: str)-> float:
    """ - Calcule la masse proteique d'une seq proteique en utilisant le dictionnaire des masses """
    mass_table={"A":   71.03711, "C":   103.00919, "D":   115.02694,
    "E":   129.04259, "F":   147.06841, "G":    57.02146,
    "H":   137.05891, "I":   113.08406, "K":   128.09496,
    "L":   113.08406, "M":   131.04049, "N":   114.04293,
    "P":   97.05276,  "Q":   128.05858, "R":   156.10111,
    "S":   87.03203,  "T":   101.04768, "V":   99.06841,
    "W":   186.07931, "Y":   163.06333 }
    P=P.upper()
    Masse=0
    for i in P:
        try: 
            Masse+=mass_table[i]
        except:
            Masse+=0
    return Masse

#-------------------------------------------------------------------------------------------------------

# FONCTION QUI GENERE LA MATRICE PROFIL ET LE CONCENSUS
def profile_consensus(l):
    ''' - Recoit une liste de sequence d'adn en entree \n
        - Retourne une matrice profil des sequences en entree \n
        - Genere un string du consensus resultant de la matrice profle '''
    i=1
    taille = len(l[0])
    while i < len(l):
        if len(l[i])> taille:
            taille = len(l[i])
        i+=1
    i=0
    while i < len(l):
        j = len(l[i])
        while j<taille:
            l[i] +='-'
            j+=1
        i+=1
    k=[]
    for i in range(0, len(l)):
        q = l[i]
        list_of_letters = list(q)
        k.append(list_of_letters)
    A = [0 for x in range(len(l[0]))]
    C = [0 for x in range(len(l[0]))]
    T = [0 for x in range(len(l[0]))]
    G = [0 for x in range(len(l[0]))]

    for j in range(len(l[0])):
        for i in range(len(l)):
            if (l[i][j] == 'A'):
                A[j] = A[j] + 1
            if (l[i][j] == 'C'):
                C[j] = C[j] + 1
            if (l[i][j] == 'T'):
                T[j] = T[j] + 1
            if (l[i][j] == 'G'):
                G[j] = G[j] + 1
        j = j + 1
    # print("La matrice profile: \n")
    # print("A", A)
    # print("C", C)
    # print("T", T)
    # print("G", G)
    list2 = {'A': A, 'C': C, 'G':G, 'T':T}
    Consensus = []
    for a in range(taille):
        m = max(A[a], C[a], T[a], G[a])
        if (m == A[a]):
            Consensus.append('A')
        elif (m == C[a]):
            Consensus.append('C')
        elif (m == T[a]):
            Consensus.append('T')
        elif (m == G[a]):
            Consensus.append('G')
    S = "".join(Consensus)
    #S=0
    return(S, list2)
#-------------------------------------------------------------------------------------------------------

# FONCTION D'EPISSAGE
def Epissage_ARN(ADN : str, filename)->str:
    """ - Recoit une sequence d'adn et un fichier fasta qui contient la liste des introns \n
        - Elle supp les introns puis transcrit et traduit les exons en proteine """
    ch3=ADN
    l=[]
    if len(filename) > 0 :
        fich = generate_fasta(filename[0])
        if len(fich) > 0 :
            for adn in fich.values():
                l.append(adn)
    for i in range(len(l)):
        ch3 = ch3.replace(l[i], "")
        i = i + 1
    return(Traduction(Transcription(ch3)))



