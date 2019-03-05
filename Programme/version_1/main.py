class Table:

    def __init__(self, data):
        for ligne in data:
            tuple = Tuple(**data)
            print(tuple.cle)
            cls.TUPLES.append(tuple)
        
class Tuple:
    
    def __init__(self, **data):
        self.cle = data['cle']
        self.cle1 = data['cle1']

    def list(self):
        txt = ""
        txt = "cle" + " : " + self.cle + " -- "
        txt = txt + "cle1" + " : " + self.cle1 + " -- "
        print(txt)
        
    @classmethod
    def create_table(self, data):
        #pour chaque ligne du fichier JSON, créer une instance tuple et la lister
        #for data in json.load(open("datas_file.json")):
            #tuple = Tuple(**data)
            #print(tuple.cle)
            #cls.TUPLES.append(tuple)
        #print(len(cls.TUPLES))
        pass


#création d'un dictionnaire de test
#def createData():

#définition de la méthode main
def main():
    #que va faire le programme ?
    #créer des tuples
    #les analyser
    #data = createData()
    
    data = []
    for i in range(0,100):
        data.append({"clé"+i:"val"+i})
    return data
    print(data)
    print(data[0])
    print(data[99])

    #TUPLES = []
    #Tuple.create_table(data)
    
    #donnees = Tuple(**data)
    #print(données.list)
    #print(donnees.cle)
    #donnees.list()
    
    print("end")

#méthode lancée lors de l'éxécution du cript
main()
