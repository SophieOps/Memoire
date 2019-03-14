# coding: utf-8

    
#création d'une liste de tuples de test
def createData():
    data = []
    for i in range(0,10):
        data.append(("id", "bjr" , "numero",str(i), "weight"))
    #print(data)
    return data
#résulution avec les données
def OptSRepair(delta,T):
    data = []
    data = createData()
    #print(data[0])
    #print(data[8])
    
#création d'une liste de tuples de dépendances fonctionelles de test
def createDF():
    df = []
    cas = 1
    if cas == 0:
        for i in range(0,10):
            df.append((("A", "B") , ("C",)))
    #cas 1 de l'article
    if cas == 1:
        df.append((("F",) , ("C","A")))
        df.append((("F", "R") , ("C",)))
    #cas 2 de l'article
    if cas == 2:
        df.append((("A",) , ("B",)))
        df.append((("B",) , ("A",)))    
        df.append((("B",) , ("C",)))
    #cas 3 de l'article,
    #S = ssn, F = first, L = last, A = address, O = office, P = phone, B = fax
    if cas == 3:
        df.append((("S",) , ("F", "L", "A")))
        df.append((("F", "L") , ("S",)))
        df.append((("S", "O") , ("P", "B")))
    #cas 4 de l'article : Négatif
    if cas == 4:
        df.append((("A",) , ("B",)))
        df.append((("B",) , ("A",)))
    #cas 5 de l'article : Négatif
    if cas == 5:
        df.append((("A",) , ("B",)))
        df.append((("C",) , ("D",)))
    return df

#transformer les DF pour qu'il n'y ai que 1 attribut à la main droite tel que: X->AB deviennt X->A et X->B.
def OneToRHS(delta):
    deltaOne = []
    for df in delta:
        print(len(df[1]))
        if len(df[1]) == 1:
               deltaOne.append(df)
        else:
               for attribut in df[1]:
                   deltaOne.append((df[0],(attribut,)))
    #print(deltaOne)

#supprimer les DFs de delta qui sont triviale c-à-d que dans X->Y, Y est inclus dans X
def RemoveTrivialDF(delta):
    for df in delta:
        include = False
        for dhs in df[1]:
            for lhs in df[0]:
                
            
    #print(deltaOne)
                   
#test si la complexité de la situation des DFs
def OSRSucceeds(delta):
    while delta is nontrivial:
        delta = RemoveTrivialDF(delta)
        if delta has a common lhs A then
            delta := delta − A
        else if delta has a consensus FD ∅ → A then
            delta := delta − A
        else if delta has an lhs marriage (X1,X2) then
            delta := delta − X1X2
        else
            return False
    return True

#définition de la méthode main
def main():
    
    print("begin")
    delta = []
    delta = createDF()
    #print(delta[1])
    #print(delta[1][0])    
    #transformer les DF pour qu'il n'y ai que 1 attribut à la main droite
    deltaOne = OneToRHS(delta)
    
    OSRSucceeds(deltaOne)
    
    #retirer les doublons
    #OptSRepair(Δ,T)
    
    #1 - retirer les DFs  X->A triviales, c'est-à-dire quand A est inclus dans X
    #2 - CommonLHSRep :Dans ce cas on regroupe toutes les lignes en fonction de la valeur de l'attribut commun A. Ensuite, on fait un appel récursif à OptSRepair pour chaque sous-ensemble avec les DFs sans l'attribut A et on fait l'union des opt sous S repair.
    #common lhs c-à-d un attribut présent toutes les lhs de toutes les df.
    #3 - ConsensusRep :Dans ce cas on regroupe toutes les lignes en fonction de la valeur de l'attribut de la main droite A. Ensuite, on fait un appel récursif à OptSRepair pour chaque sous-ensemble avec les DFs sans l'attribut A et on sélectionne le sous ensemle avec le poid maximal.
    #consensus c-à-d que lhs est vide et donc les valeurs des attributs de Y sont tous les mêmes
    #4 -  :Dans ce cas on trouve la correspondance de poid maximum du graph pibartite.
    #lhs mariage (X1,X2) c-à-d

    
    print("end")

#méthode lancée lors de l'éxécution du cript
main()
