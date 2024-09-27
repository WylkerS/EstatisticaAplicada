#Quais características (Comprimento de sépala,largura de sépala, comprimento de pétala, largura de pétala) têm a maior variabilidade dentro de cada espécie?
import pandas as pd


IRIS = pd.read_csv("Iris.csv")


setosa = IRIS.loc[IRIS['Species'] == 'Iris-setosa']
def testeDeVariabilidade(data, specie_name):

    colunas = ["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]
    
    print(f"\nTeste de variabilidade com desvio padrão para {specie_name}:\n")
    
    for c in colunas:
        standard_deviation = data[c].std(ddof=0)
        print(f"{c}") 
        print(f"Desvio padrão = {standard_deviation:.4f}\n")
        
testeDeVariabilidade(setosa,"Iris-setosa")