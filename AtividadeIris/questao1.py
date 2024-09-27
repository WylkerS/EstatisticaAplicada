#Qual espécie de íris (Setosa, Versicolor, Virginica) tem a maior média de comprimento de pétala?

import pandas as pd


IRIS = pd.read_csv("Iris.csv")


def nomeEspecies():
    return pd.unique(IRIS["Species"])

def filtrarDados(name):
    return pd.DataFrame(IRIS.loc[IRIS["Species"]==name])

def mediaComprimento():
    nomeDasEspecies = nomeEspecies()
    for c in nomeDasEspecies:  
        comprimentoMedioPetala = filtrarDados(c)["PetalLengthCm"].mean()
        print(f"\nComprimento médio da pétala {c}: {comprimentoMedioPetala:.2f}") 
        

mediaComprimento()



    