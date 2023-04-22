import math

vInicial = 0
grav = 9.81
altura = float(input("Defina a altura do corpo em relação ao solo(em m): "))
raiz = math.sqrt(2 * altura / grav)

tempo = raiz

print("O tempo necessário para que o corpo atinja o solo é de %.2f"% tempo)