# Este script faz a classificação se um site é autêntico ou falso, usando o 
# algoritmo KNN e a biblioteca SciKit Learn
# Rodrigo Costa
# 2018-nov-09
# Fonte https://archive.ics.uci.edu/ml/datasets/Website+Phishing
# =============================================================================

# Instalar última versão do SciKit Learn usando pip
# pip3 install -U scikit-learn

# Importando biblioteca SciKit Learn
from sklearn.neighbors import KNeighborsClassifier

# Importando biblioteca math
import math

# Listas para conter os atributos de cada registro
entradas, saidas = [], []

# Abrir e ler o arquivo de texto com os dados
with open("website_data.txt", "r") as arquivo:
	for linha in arquivo.readlines():
    # Organizar os atributos em uma linha
		atributo = linha.replace("\n","").split(",")

    # Adicionar os atributos mais relevantes(por enquanto) a lista
		entradas.append([int(atributo[0]), 
                     int(atributo[1]), 
                     int(atributo[2]), 
                     int(atributo[3]), 
                     int(atributo[4]), 
                     int(atributo[5]), 
                     int(atributo[6]), 
                     int(atributo[7]), 
                     int(atributo[8])]
                  )

    # O último atributo é a classificação
    # -1 = Falso
    # 0 = Suspeito
    # 1 = Autêntico
		saidas.append(int(atributo[9]))

# Quantidade de registros para treinamento
treinamento = 0.6
limite = int(treinamento * len(entradas))

# Tamanho do K definido como raiz do total de entradas
#neigh = KNeighborsClassifier(n_neighbors=math.sqrt(len(entradas)))
neigh = KNeighborsClassifier(n_neighbors=15)

# 
neigh.fit(entradas[:limite], saidas[:limite])

# 
labels = neigh.predict(entradas[limite:])

# Contagem de acertos
acertos, indice_label = 0, 0
for i in range(limite, len(entradas)):
	if labels[indice_label] == saidas[i]:
		acertos += 1
	indice_label += 1
    
# Impressão de resultados
print("Total de treinamento: %d" % limite)
print("Total de testes: %d" % (len(entradas) - limite))
print("Total de acertos: %d" % acertos)
print("Porcento de acertos: %.2f" % (100 * acertos / (len(entradas) - limite)))
#print("Limite: " + str(limite))

print("\n\n")
teste = 15

print("Atributos do elemento %d" % (limite + teste))
print(entradas[limite + teste])

print("Classe do elemento")
print(saidas[limite + teste])
print("Classe encontrada")
print(labels[teste])
