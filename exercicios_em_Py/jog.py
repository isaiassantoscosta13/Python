import matplotlib.pyplot as plt
import numpy as np
import random

# Definir os limites do gráfico
plt.xlim(0, 100)
plt.ylim(0, 100)

# Criar um ponto inicial
x = 1
y = 1

# Definir o tamanho inicial do ponto
size = 10

# Armazenar as coordenadas anteriores em listas
xs = [x]
ys = [y]

# Traçar o primeiro ponto
plt.scatter(x, y, s=size)

# Definir as coordenadas de parada do loop
x_stop = random.uniform(30, 60)
y_stop = random.uniform(5, 80)

# Definir um loop que atualiza a posição do ponto de maneira aleatória
while x < x_stop and y < y_stop:
    # Gerar um número aleatório para a mudança de posição na coordenada x
    delta_x = random.uniform(0, 1)
    # Calcular a mudança de posição na coordenada y de acordo com a função y = 2^x
    delta_y = 2**delta_x - 1
    # Atualizar a posição do ponto
    x += delta_x
    y += delta_y
    # Adicionar as novas coordenadas à lista de coordenadas
    xs.append(x)
    ys.append(y)
    # Atualizar o tamanho do ponto de forma exponencial
    size *= 1.1
    size = np.exp(size/100)
    # Limpar a figura
    plt.clf()
    # Traçar o ponto com o novo tamanho
    plt.scatter(x, y, s=size)
    # Traçar a linha conectando os pontos anteriores
    plt.plot(xs, ys, c='blue')
    plt.pause(0.1)

plt.show()
