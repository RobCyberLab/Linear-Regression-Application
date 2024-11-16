import numpy as np
import matplotlib.pyplot as plt

# Imagine cu o pantă ascendentă - generare aleatorie de puncte
np.random.seed(0)  # pentru reproducibilitate
x_asc = np.random.uniform(1, 40, 30)
y_asc = 2 * x_asc + np.random.uniform(-5, 40, 30)

# Imagine cu o pantă descendentă - generare aleatorie de puncte
x_desc = np.random.uniform(1, 40, 30)
y_desc = 80 - 2 * x_desc + np.random.uniform(-5, 40, 30)


# Funcția pentru regresia liniară
def linear_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Calculul coeficientului b
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    b = numerator / denominator

    # Calculul coeficientului a
    a = y_mean - b * x_mean

    # Calculul valorii estimate de y
    y_pred = a + b * x

    # Calculul erorii totale
    error = np.sum((y - y_pred) ** 2)

    return a, b, y_pred, error


# Aplicarea regresiei liniare pe imaginile cu pantă ascendentă și descendentă
a_asc, b_asc, y_pred_asc, error_asc = linear_regression(x_asc, y_asc)
a_desc, b_desc, y_pred_desc, error_desc = linear_regression(x_desc, y_desc)

# Afisarea rezultatelor
print("Panta ascendentă - Coeficientul a:", a_asc, "Coeficientul b:", b_asc, "Eroarea totală:", error_asc)
print("Panta descendentă - Coeficientul a:", a_desc, "Coeficientul b:", b_desc, "Eroarea totală:", error_desc)

# Afisarea perechilor de puncte pentru imaginea cu pantă ascendentă
print("Perechile de puncte pentru imaginea cu pantă ascendentă:")
for i in range(len(x_asc)):
    print(f"Punctul {i + 1}: ({x_asc[i]}, {y_asc[i]})")

# Afisarea perechilor de puncte pentru imaginea cu pantă descendentă
print("\nPerechile de puncte pentru imaginea cu pantă descendentă:")
for i in range(len(x_desc)):
    print(f"Punctul {i + 1}: ({x_desc[i]}, {y_desc[i]})")

# Trasarea graficului pentru imaginea cu pantă ascendentă
plt.subplot(2, 1, 1)
plt.scatter(x_asc, y_asc, color='blue', label='Date de intrare')
plt.plot(x_asc, y_pred_asc, color='red', label='Linie de regresie')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresie liniară - Pantă ascendentă')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)

# Trasarea graficului pentru imaginea cu pantă descendentă
plt.subplot(2, 1, 2)
plt.scatter(x_desc, y_desc, color='green', label='Date de intrare')
plt.plot(x_desc, y_pred_desc, color='orange', label='Linie de regresie')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresie liniară - Pantă descendentă')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)

plt.tight_layout()
plt.show()
