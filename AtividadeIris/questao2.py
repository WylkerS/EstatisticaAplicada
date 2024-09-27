#Há uma correlação significativa entre o comprimento da sépala e o comprimento da pétala?

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as stats


IRIS = pd.read_csv("Iris.csv")


sepal = IRIS["SepalLengthCm"]
petal = IRIS["PetalLengthCm"]

#O gráfico de dispersão revela uma correlação forte e positiva entre os dois dados, evidenciando uma relação aparente entre eles.
sns.regplot(data=IRIS, x=sepal, y=petal, line_kws={"color":"black"})

plt.title('Comprimento da Sépala e da Pétala')
plt.xlabel('Sépala')
plt.ylabel('Pétala')
plt.show()


#Fiz o teste de Shapiro para ver a normalidade
print("\nTESTE DE SHAPIRO\n")

P_ValorSepal = stats.shapiro(sepal).pvalue
print(f"Comprimento da Sépala: {P_ValorSepal}")

P_ValorPetal = stats.shapiro(petal).pvalue
print(f"Comprimento da Pétala: {P_ValorPetal}")

# Como os valores são menores que o LIMIT, utilizo o SPEARMAN
LIMIT = 0.05
coeficienteDeRelação = 0
p_ValorCorrelação = 0 

if (P_ValorPetal > LIMIT ) and ( P_ValorSepal > LIMIT):

    coeficienteDeRelação, p_ValorCorrelação = stats.pearsonr(sepal, petal)
    print(f"Correlação de Pearson: {coeficienteDeRelação}, p-valor: {p_ValorCorrelação}")

else:
    
    coeficienteDeRelação, p_ValorCorrelação = stats.spearmanr(sepal, petal)
    print("\nCORRELAÇÃO DE SPEARMAN\n")
    print(f"Comprimento de petala e sepala: {coeficienteDeRelação}")
    print(f"P_Valor: {p_ValorCorrelação}")

#Conclui-se que há uma forte correlação positiva entre o comprimento da sépala e o da pétala.
    

