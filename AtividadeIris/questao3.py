#Qual a distribuição das espécies no banco de dados?

import pandas as pd
import scipy.stats as stats


IRIS = pd.read_csv("Iris.csv")


setosa = IRIS.loc[IRIS['Species'] == 'Iris-setosa']
versicolor = IRIS.loc[IRIS['Species'] == 'Iris-versicolor']
virginica =IRIS.loc[IRIS['Species'] == 'Iris-virginica']

def testeDeNormalidade(data,specie_name):

    LIMIT = 0.05
    colunas = ["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]
    print(f"{specie_name}:\n")
    
    for c in colunas:
        P_Valor = stats.shapiro(data[c]).pvalue

        if P_Valor > LIMIT:
            print(f"{c}")
            print("Distribuição normal")
            print(f"P_Valor: {P_Valor:.4f}\n")
        else:
            print(f"{c}") 
            print("Distribuição não normal")
            print(f"P_Valor: {P_Valor:.4f}\n")

print("\nTESTE DE SHAPIRO WILK\n")

testeDeNormalidade(setosa,"Iris-Setosa")
print("-"*25)
testeDeNormalidade(versicolor,"Iris-Versicolor")
print("-"*25)
testeDeNormalidade(virginica,"Iris-Virginica")



