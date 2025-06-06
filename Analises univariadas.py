import pandas as pd
import numpy as np
from statistics import mode
#temperaturas do primeiro e último dia do ano

temp1 = pd.Series([18.9 ,19, 19, 18.9, 18.8, 18.7, 18.6, 18.5, 18.6, 18.4, 18.7, 19.6, 20.6, 21.1, 21.3, 21.5, 22.3, 22.4, 23.7, 23.7, 22.7, 21.8, 21.2, 20.2])
temp2 = pd.Series([20.2, 20.2, 20, 20, 19.8, 19.7, 20, 20, 19.7, 19.8, 21.1, 23, 24.3, 25.8, 27.3, 27.5, 27.2, 22.7, 22.3, 21.5, 21.1, 20.9, 20.7, 20.5])
#temperatura de todos os dias do ano

df = pd.read_csv('INMET_SE_SP_A771_SAO PAULO - INTERLAGOS_01-01-2024_A_31-12-2024.csv', sep=';', encoding='latin1', skiprows=8)

temp_total = [
    float(str(x).replace(',', '.'))
    for x in df.iloc[:, 9]
    if pd.notna(x) and str(x).strip() != ''
]
temp_np = np.array(temp_total)


#a) Medidas de Tendência Central: Média, Mediana e Moda.

print(f"A média das temperaturas durante o dia 01/01/2024 foi de: {temp1.mean():.2f}Cº")
print(f"A média das temperaturas durante o dia 31/12/2024 foi de: {temp2.mean():.2f}Cº")
print(f"A média das temperaturas durante o ano de 2024 foi de: {temp_np.mean():.2f}Cº")
print("=======================================================================================")
print(f"A mediana das temperaturas durante o dia 01/01/2024 foi de {temp1.median()}Cº")
print(f"A mediana das temperaturas durante o dia 31/12/2024 foi de {temp2.median():.2f}Cº")
print(f"A mediana das temperaturas durante o ano de 2024 foi de: {np.median(temp_np):.2f}Cº")
print("=======================================================================================")
print(f"A moda das temperaturas durante o dia 01/01/2024 foi de {temp1.mode()[0]}Cº")
print(f"A moda das temperaturas durante o dia 31/12/2024 foi de {temp2.mode()[0]}Cº")
print(f"A moda das temperaturas durante o ano de 2024 foi de: {mode(temp_np):.2f}Cº")
print("=======================================================================================")

#b) Medidas de Dispersão: Máximo, Mínimo, Amplitude, Variância, Desvio Padrão e Coeficiente de Variação.

print(f"A temperatura máxima e mínima durante o dia 01/01/2024 foram de: {temp1.max()}Cº e {temp1.min()}Cº")
print(f"A temperatura máxima e mínima durante o dia 31/12/2024 foram de: {temp2.max()}Cº e {temp2.min()}Cº")
print(f"A temperatura máxima e mínima durante o ano de 2024 foram de: {temp_np.max()}Cº e {temp_np.min()}Cº")
print("=======================================================================================")
print(f"A amplitude das temperaturas do dia 01/01/2024 foi de {temp1.max() - temp1.min():.2f}Cº")
print(f"A amplitude das temperaturas do dia 31/12/2024 foi de {temp2.max() - temp2.min():.2f}Cº")
print(f"A amplitude das temperaturas do ano de 2024 foi de {temp_np.max() - temp_np.min():.2f}Cº")
print("=======================================================================================")
print(f"A variância amostral das temperaturas do dia 01/01/2024 foi de {temp1.var():.2f}Cº")
print(f"A variância amostral das temperaturas do dia 31/12/2024 foi de {temp2.var():.2f}Cº")
print(f"A variância amostral das temperaturas do ano de 2024 foi de {temp_np.var():.2f}Cº")
print("=======================================================================================")
print(f"O desvio padrão das temperaturas do dia 01/01/2024 foi de {temp1.std():.2f}Cº")
print(f"O desvio padrão das temperaturas do dia 31/12/2024 foi de {temp2.std():.2f}Cº")
print(f"O desvio padrão das temperaturas do ano de 2024 foi de {temp_np.std():.2f}Cº")
print("=======================================================================================")
print(f"O coeficiente de variação das temperaturas do dia 01/01/2024 foi de {temp1.std() / temp1.mean() * 100:.2f}Cº")
print(f"O coeficiente de variação das temperaturas do dia 31/12/2024 foi de {temp2.std() / temp2.mean() * 100:.2f}Cº")
print(f"O coeficiente de variação das temperaturas do ano de 2024 foi de {temp_np.std() / temp_np.mean():.2f}Cº")
print("=======================================================================================")

#c) Medidas Separatrizes: Quartis.

print(f"Os quartis das temperaturas do dia 01/01/2024 foram de {temp1.quantile([0.25][0]):.2f}Cº(25%), {temp1.quantile([0.50][0]):.2f}Cº(50%) e {temp1.quantile([0.75][0]):.2f}Cº(75%)")
print(f"Os quartis das temperaturas do dia 31/12/2024 foram de {temp2.quantile([0.25][0]):.2f}Cº(25%), {temp2.quantile([0.50][0]):.2f}Cº(50%) e {temp2.quantile([0.75][0]):.2f}Cº(75%)")
print(f"Os quartis das temperaturas do ano de 2024 foram de {np.percentile(temp_np, [25])[0]:.2f} Cº(25%), {np.percentile(temp_np, [50])[0]:.2f}Cº(50%) e {np.percentile(temp_np, [75])[0]:.2f}Cº(75%)")
