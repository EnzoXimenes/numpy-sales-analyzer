import numpy as np

vendas = np.array([
    [120, 135, 110, 150, 145, 160, 155],
    [90,  100, 85,  110, 105, 120, 115],
    [200, 180, 210, 190, 220, 230, 215],
    [70,  80,  75, 90,  85, 95, 100],
    [150, 145, 160, 155, 170, 165, 180]
])

desvio_padrao = np.std(vendas, axis = 1)
media_coluna = np.mean(vendas, axis = 0)
indice_menor_desvio = np.argmin(desvio_padrao)
media_linha = np.mean(vendas, axis = 1)
percentil = np.percentile(vendas, 90)
maior_indice = np.argmax(media_linha)
menor_indice = np.argmin(media_linha)
melhor_dia = np.argmax(media_coluna)
media_melhor_dia = media_coluna[melhor_dia]
pior_dia = np.argmin(media_coluna)
media_pior_dia = media_coluna[pior_dia]
media = np.mean(vendas)
quantidade_abaixo = np.sum(vendas < media)

print(f"A loja {maior_indice + 1} foi a que vendeu mais!")
print(f"A loja  {menor_indice + 1} foi a que vendeu menos!")
print(f"A média de cada loja é {media_linha}!")
print(f"A média de cada dia é {media_coluna}!")
print(f"A loja mais consistente é {indice_menor_desvio + 1}")
print(f"O dia {melhor_dia + 1} no melhor dia vendeu {media_melhor_dia}")
print(f"O dia {pior_dia + 1} no pior dia vendeu {media_pior_dia}")
print(f"O percentil 90 das vendas é {percentil}")

if quantidade_abaixo > 0:
    print(f"Existem {quantidade_abaixo} abaixo da média")
else:
    print("Não existem vendas abaixo da média ")
