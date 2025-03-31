# Faça o usuário entrar com dois valores valor mínimo e valor máximo 
# O seu algoritmo deverá decidir se a contagem que será feita é crescente ou decrescente que será mostrada ao usuário,
# se o 1 º numero digitado for maior que o 2 º então a contagem é decrescente e se 
# acontecer o contrário, crescente


# Entrada de dados
min = int(input("Escreva o mínimo: "))
max = int(input("Escreva o número maximo: "))

# Checagem de contagem

if min < max:
    for x in range (min, max + 1, 1):
        print(x)
    
elif min > max:
    for y in range (max, min + 1, 1):
        print (y)

