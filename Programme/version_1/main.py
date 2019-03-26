# coding: utf-8

#création d'une liste de liste de dépendances fonctionelles de test
def createDF(cas):
    df = []
    if cas == 0:
        for i in range(0,10):
            df.append([["A", "B"] , ["C",]])
    #cas 1 de l'article
    if cas == 1:
        df.append([["F",] , ["C","A"]])
        df.append([["F", "R"] , ["C",]])
        df.append([["F", "C"] , ["C",]]) #dépendance triviale supprimée à la première itération
        #df.append([[None] , ["C",]]) #dépendance avec une absence d'attribut à la main gauche 
    #cas 2 de l'article
    if cas == 2:
        df.append([["A",] , ["B",]])
        df.append([["B",] , ["A",]])    
        df.append([["B",] , ["C",]])
    #cas 3 de l'article,
    #S = ssn, F = first, L = last, A = address, O = office, P = phone, B = fax
    if cas == 3:
        df.append([["S",] , ["F", "L", "A"]])
        df.append([["F", "L"] , ["S",]])
        df.append([["S", "O"] , ["P", "B"]])
    #cas 4 de l'article : Négatif
    if cas == 4:
        df.append([["A",] , ["B",]])
        df.append([["B",] , ["A",]])
    #cas 5 de l'article : Négatif
    if cas == 5:
        df.append([["A",] , ["B",]])
        df.append([["C",] , ["D",]])
    if cas == 6:
        df.append([[None,] , ["B",]])
        df.append([["A",] , [None,]]) #attention, provoque une erreur, quand on supprimera l'existance d'un attribut, il faudra supprimer la df si la rhs est vide
        #df.append([["A",] , None])        
    if cas == 7:
        pass
    return df

#vérifier si la liste des dfs n'est pas vide
def IsDFNotEmpty(delta):
    if len(delta) == 0:
        return False
    for df in delta:
            if df is None:
                delta.remove(df)
            """if len(df) != 2:
                delta.remove(df)
            if df[1] is None:
                delta.remove(df)"""#ne devrait pas se présenter
    if len(delta) == 0:
        return False
    return True

#transformer les DF pour qu'il n'y ai que 1 attribut à la main droite tel que: X->AB deviennt X->A et X->B.
def OneToRHS(delta):
    deltaOne = []
    if IsDFNotEmpty(delta):
        for df in delta:
            #print(len(df[1]))
            if len(df[1]) == 1:
                   deltaOne.append([df[0], df[1][0]])
            else:
                   for attribut in df[1]:
                       deltaOne.append([df[0], attribut])
    #print(deltaOne)
    return deltaOne

#1 - supprimer les DFs de delta qui sont triviale c-à-d que dans X->Y, Y est inclus dans X
def RemoveTrivialDF(delta):
    for df in delta:
        if df[1] in df[0]:#df[1] est un attribut seul MAIS df[0] est une liste d'attribut
            print("On supprime la dépendance fonctionnelle : "+str(df))
            delta.remove(df)                    
    return delta

#2 - On veut savoir si il existe un "Common LHS" et lequel
#common lhs c-à-d un attribut présent toutes les lhs de toutes les df de delta
def CommonLHSAtt(delta):
    """Recherche la présence des attributs de la première DF dans toutes les autres
et return l'attributs commun"""
    if delta[0][0] is not None:
        for att in delta[0][0]:
            find = True
            for df in delta[1:]:
                if att not in df[0]:
                    find = False
                    break
            if find:
                return att
    return ""

#Supprimer un attribut parce que il est commaun à toutes les dfs
def RemoveAtt(delta, att):
    for df in delta:
        if att == df[1]:
            delta.remove(df)
        elif len(df[0]) == 1:
            #print("La suppression d'un attribut met à null sa main gauche : "+str(df))
            df[0] = None
            #print("Modification effectuée : "+str(df))
        else:
            df[0].remove(att)
    return delta

#Dans ce cas on regroupe toutes les lignes en fonction de la valeur de l'attribut de la main droite A. Ensuite, on fait un appel récursif à OptSRepair pour chaque sous-ensemble avec les DFs sans l'attribut A et on sélectionne le sous ensemle avec le poid maximal
#consensus c-à-d que lhs est vide et donc les valeurs des attributs de Y sont tous les mêmes
def ConsensusAtt(delta):
    for df in delta:
        if df[0] == None or len(df[0]) == 0:
            return df[1]
    return ""

#Dans ce cas on trouve la correspondance de poid maximum du graph pibartite.
#lhs mariage (X1,X2) c-à-d être en présence de la situation suivante : X->Y et Y ->X et que X ou Y soit présent dans toutes les autres dfs
def MarriageAtt(delta):
    """Recherche la présence de marriage dans les DFs. Renvoie une liste des attributs ou ""."""
    for df in delta:
        val = df[1]
        lhs = df[0]
        for att in lhs:
            marriage=False
            for df2 in delta:
                if len(df2[0])==1 and df2[0][0]==val and df2[1]==att:
                    marriage = True
                    break
        if marriage:
            return [lhs, val]
    return ""
        
def OSRSucceeds(delta):
    """determine if the resolution is polynomial or not"""
    while IsDFNotEmpty(delta):
    #if IsDFNotEmpty(delta):
        attributCommun = CommonLHSAtt(delta)
        print("attributCommun : "+attributCommun)
        if attributCommun != "":
            delta = RemoveAtt(delta, attributCommun)
            print("L'attribut commun <<"+attributCommun+">> a été trouvé et supprimé dans delta")
        else:
            attributConsensus = ConsensusAtt(delta)
            print("attributConsensus : "+attributConsensus)
            if attributConsensus != "":
                delta = RemoveAtt(delta, attributConsensus)
                print("L'attribut <<"+attributConsensus+">> a été trouvé dans un consensus et supprimé dans delta")
            else:
                attributMariage = MarriageAtt(delta)
                print("attributMariage = "+attributMariage)
                if attributMariage != "":
                    delta = RemoveAtt(delta, attributMariage[0])
                    delta = RemoveAtt(delta, attributMariage[1])
                else:
                    return False
        print(delta)
    return True

def createData(cas):
    """Return a list of tuples"""
    #N.B. les tuples sont les listes qui ne peuvent pas être modifiées
    data = []
    if cas == 0:
        for i in range(0,10):
            data.append(("id", "bjr" , "numero",str(i), "weight"))
    if cas == 1:
        data.append((1, "HQ", 322, 3, "Paris", 3))
        data.append((2, "HQ", 322, 30, "Madrid", 1))
        data.append((3, "HQ", 122, 1, "Madrid", 1))
        data.append((4, "Lab1", 835, 3, "Londres", 4))
    #print(data)
    return data

def createMetaData(cas):
    """Return a list with the name of each attribute in the same order that they are present in the physical table"""
    meta = []
    if cas == 0:
        meta.extend(("id", "str" , "num","val", "weight"))
    if cas == 1:#id - facility - room - floor - city - weight
        meta.extend(("I", "A", "R", "F", "C", "W"))
    if cas == 2:
        meta.extend(("I", "A", "B", "W"))
    if cas == 3:
        meta.extend(("I", "S", "F", "L", "A", "O", "P", "B", "W"))
    if cas == 4:
        meta.extend(("I", "A", "B", "W"))
    if cas == 5:
        meta.extend(("I", "A", "B", "C", "D", "W"))
    if cas == 6:
        meta.extend(("I", "A", "B", "W"))
    if cas == 7:
        meta.extend(("I", "W"))        
    #print(meta)
    return meta

#2 - CommonLHSRep :Dans ce cas on regroupe toutes les lignes en fonction de la valeur de l'attribut commun A.
#Ensuite, on fait un appel récursif à OptSRepair pour chaque sous-ensemble avec les DFs sans l'attribut A et on fait l'union des opt sous S repair.
#common lhs c-à-d un attribut présent toutes les lhs de toutes les df.
def CommonLHSRep(delta, data, meta, attribut):
    """Return ∪(a)∈πAT [∗]OptSRepair(σA=aT, Δ − A)"""
    listeSegm = {}
    index = meta.index(attribut)
    """Je fais le listing de mes valeurs différentes pour cet attribut
       Je regarde si la valeur existe en cherchant son index. Si pas, je l'ajoute"""
    for ligne in data:
        if not ligne[index] in listeSegm.keys():
            listeSegm[ligne[index]]=[]
        listeSegm[ligne[index]].append(ligne)
    
    result=[]
    """Pour chacunes de ces listes de lignes avec la même valeur,"""
    for segment in listeSegm.values():      
        """J'envoie cette liste temporaire dans OptSrepair """
        sousListe = OptSRepair(delta, segment, meta)
        """if sousListe == False ???"""
        """Je fais l'union des listes retournées"""
        result.extend(sousListe)
    return result
    
#3 - ConsensusRep :Dans ce cas on regroupe toutes les lignes en fonction de la valeur de l'attribut de la main droite A.
#Ensuite, on fait un appel récursif à OptSRepair pour chaque sous-ensemble avec les DFs sans l'attribut A
#et on sélectionne le sous ensemle avec le poid maximal.
#consensus c-à-d que lhs est vide et donc les valeurs des attributs de Y sont tous les mêmes
def ConsensusRep(delta, data, meta, attribut):
    index = meta.index(attribut)
    listeSegm = {}
    """Je fais le listing de mes valeurs différentes pour cet attribut"""
    for ligne in data:
        if not ligne[index] in listeSegm.keys():
            listeSegm[ligne[index]]=[]
        listeSegm[ligne[index]].append(ligne)
        
    result=[]
    poidsMax=0
    """Je lance le traitement de chachun de ces sous tableaux et je garde le retour de celui qui possède une somme de poids le plus élevé"""
    for segment in listeSegm.values():
        sousListe = OptSRepair(delta, segment, meta)
        """traitemant si sousListe == False ??? """
        poids=0
        for ligne in sousListe:
            poids += ligne[len(ligne)-1]
        if poids > poidsMax:
            result=sousListe
            poidsMax = poids    
    return result

#4 - MarriageRep:Dans ce cas on trouve la correspondance de poid maximum du graph pibartite.
#lhs mariage (X1,X2) c-à-d être en présence de la situation suivante : X->Y et Y ->X et que X ou Y soit présent dans toutes les autres dfs
def MarriageRep(delta, data, meta, attributs):
    """1: select an lhs marriage (X1,X2) of Δ
2: for all (a1, a2) ∈ πX1X2T [∗] do
3: Sa1,a2 := OptSRepair(σX1=a1,X2=a2T, Δ − X1X2)
4: w(a1, a2) := wT (Sa1,a2 )
5: Vi := πXiT [∗] for i = 1, 2
6: E := {(a1, a2) | (a1, a2) ∈ πX1X2T [∗]}
7: G := weighted bipartite graph (V1,V2, E,w)
8: Emax := a maximum matching of G
9: return ∪(a1,a2 )∈EmaxSa1,a2"""
    return data
    
#résulution avec les données
def OptSRepair(delta, data, meta):
    #TODO : retirer les DFs triviales : RemoveTrivialDF
    print(delta)
    print(data)
    print(meta)
    if not IsDFNotEmpty(delta):
        print("Le delta est vide")
        return data
    attributCommun = CommonLHSAtt(delta)
    print("attributCommun : "+attributCommun)
    if attributCommun != "":
        delta = RemoveAtt(delta, attributCommun)
        print("L'attribut commun <<"+attributCommun+">> a été trouvé et supprimé dans delta")
        return CommonLHSRep(delta, data, meta, attributCommun)
    attributConsensus = ConsensusAtt(delta)
    print("attributConsensus : "+attributConsensus)
    if attributConsensus != "":
        delta = RemoveAtt(delta, attributConsensus)
        print("L'attribut <<"+attributConsensus+">> a été trouvé dans un consensus et supprimé dans delta")
        return ConsensusRep(delta, data, meta, attributConsensus)
    attributMariage = MarriageAtt(delta)
    print("attributMariage : "+attributMariage)
    if attributMariage != "":
        delta = RemoveAtt(delta, attributMariage[0])
        delta = RemoveAtt(delta, attributMariage[1])
        print("Les attributs <<"+attributMariage+">> ont été trouvé dans un mariage et supprimé dans delta")
        return MarriageRep(delta, data, meta, attributMariage)
    print(delta)
    return False
    
#définition de la méthode main
def main():    
    print("begin")
    cas = 1 #permet de sélectionner un scénario de test
    delta = []
    delta = createDF(cas)
    deltaBis = list(delta)
    print(delta)
    #print(delta[1])
    #print(delta[1][0])    
    delta = OneToRHS(delta) #transformer les DF pour qu'il n'y ai que 1 attribut à la main droite
    delta = RemoveTrivialDF(delta) 
   
    reponse = OSRSucceeds(delta)

    print("La simplification des dépendances donne le résultat suivant : "+ str(reponse))
    if not reponse:
        print("Pas de simplification possible")
        return
    
    data = []
    data = createData(cas)
    #delta = list(deltaBis)
    delta = createDF(cas)
    delta = OneToRHS(delta)
    delta = RemoveTrivialDF(delta) 
    meta = createMetaData(cas)
    print(data)
    #print(data[0])
    #print(data[-1])   
    
    #TODO : retirer les doublons
    result = OptSRepair(delta, data, meta)
    print("Le résultat est : ")
    print(result)
    print("end")

#méthode lancée lors de l'éxécution du cript
main()
