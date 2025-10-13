import matplotlib.pyplot as plt
import numpy as np

n = int(input("Quantos pontos você quer plotar? "))

xpoints = []
ypoints = []

for i in range(n):
    x = float(input(f"Digite o valor de x[{i+1}]: "))
    xpoints.append(x)
    print()

for i in range(n):
    y = float(input(f"Digite o valor de y[{i+1}]: "))
    ypoints.append(y)
    print()

xpoints = np.array(xpoints)
ypoints = np.array(ypoints)

plt.plot(xpoints, ypoints)

plt.savefig("grafico.png")
plt.show()
