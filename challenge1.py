print("Descubra seu IMC")

peso = float(input("Olá, qual o seu peso atual? "))
altura = float(input("E qual a sua altura? " ))

# potência no python é colocando dois asteriscos 

imc = peso / altura ** 2
print("Seu imc é %.1f"% imc)