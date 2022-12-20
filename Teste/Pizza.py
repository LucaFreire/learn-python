from matplotlib import pyplot as plt
# Language Popularity

dados = [59219, 55466, 47544, 36443, 35917]
nomes = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]

#       Valores   Legenda  Separa a Fatia  Coloca os Valores
plt.pie(dados,labels=nomes,explode=explode,autopct="%1.1f%%")

plt.show()


