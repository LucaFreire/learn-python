from matplotlib import pyplot as plt
import numpy as np

dados_x = [59219, 55466, 47544, 36443, 35917]

eixo_y = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

#eixo_y = [np.arange(len(dados_x))]


plt.xlabel("Linguagens de Programação") # Legenda Eixo X
plt.ylabel("Popularidade") # Legenda Eixo Y 

plt.bar(eixo_y,dados_x)

plt.show()

