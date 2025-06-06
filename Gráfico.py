import matplotlib.pyplot as plt

temp1 = [18.9 ,19, 19, 18.9, 18.8, 18.7, 18.6, 18.5, 18.6, 18.4, 18.7, 19.6, 20.6, 21.1, 21.3, 21.5, 22.3, 22.4, 23.7, 23.7, 22.7, 21.8, 21.2, 20.2]

temp2 = [20.2, 20.2, 20, 20, 19.8, 19.7, 20, 20, 19.7, 19.8, 21.1, 23, 24.3, 25.8, 27.3, 27.5, 27.2, 22.7, 22.3, 21.5, 21.1, 20.9, 20.7, 20.5]


plt.boxplot([temp1,temp2], labels = ['01/01/2024', '31/12/2024'], patch_artist=True, boxprops=dict(facecolor='purple'))

plt.title("Média de temperatura no primeiro e último dia de 2024")
plt.xlabel("Fonte de pesquisa")
plt.ylabel("Temperaturas")
plt.show()

Umidade1 = [88, 89, 89, 90, 91, 91, 87, 84, 86, 87, 85, 84, 80, 82, 82, 83, 81, 80, 81, 81, 84, 83, 85, 87]
Umidade2 = [91, 92, 92, 93, 94, 94, 94, 89, 88, 88, 84, 79, 75, 68, 65, 71, 84, 93, 96, 91, 91, 91, 90, 91]

plt.boxplot([Umidade1,Umidade2], labels = ['01/01/2024', '31/12/2024'], patch_artist=True, boxprops=dict(facecolor='purple'))
plt.title("Média de umidade relativa no primeiro e último dia de 2024")
plt.xlabel("Fonte de pesquisa")
plt.ylabel("Temperaturas")
plt.show()