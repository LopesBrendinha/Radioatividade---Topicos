import numpy as np
import matplotlib.pyplot as plt


#ano = int(input("Digite o valor de ano: "))



r1 = - (np.log(2) / 10950)
r2= - (np.log(2) / 8)
r3 = - (np.log(2) / 10512)

def p(t, formula):
    return 100 * np.exp(t *formula)  

y_axis = np.array(range(1, 87600))
x_axis = p(y_axis, r1)

y_iodo = np.array(range(1, 87600))
x_iodo = p(y_iodo, r2)

y_estroncio = np.array(range(1, 87600))
x_estroncio = p(y_estroncio, r3)

plt.plot(y_axis, x_axis, label="Cesio", color='blue')
plt.plot(y_iodo, x_iodo, label="Iodo", color='pink')
plt.plot(y_estroncio, x_estroncio, label="Estroncio", color='red')


plt.ylabel("Tempo (t)")
plt.xlabel("População p(t)")
plt.title("Crescimento Populacional - Modelo de Malthus")
plt.legend()
plt.grid(True)


plt.show()
