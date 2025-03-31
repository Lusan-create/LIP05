
# Faça um algoritmo que leia 4 números inteiros e através de uma 
# rotina de repetição e decisão se consiga mostrar na tela os números organizados de forma 
# crescente. Por enquanto não usar listas, conjuntos ou vetores, usar decisões e 
# repetições somente pra resolver essa questão.


# Entrada dos numeros
n1 = input("Escreva o primeiro número: ")
n2 = input("Escreva o segundo número: ")
n3 = input("Escreva o terceiro número: ")
n4 = input("Escreva o quarto número: ")

# Processamento

# Maior

if n1 >= n2 and n1 >= n3 and n1 >= n4:
    maior = n1
    
elif  n2 >= n1 and n2 >= n3 and n2 >= n4:
    maior = n2
    
elif n3 >= n2 and n3 >= n1 and n3 >= n4:
    maior = n3
    
elif n4 >= n2 and n4 >= n3 and n4 >= n1:
    maior = n4


# Menor

if n1 <= n2 and n1 <= n3 and n1 <= n4:
    menor = n1
    
elif n2 <= n1 and n2 <= n3 and n2 <= n4:
    menor = n2
    
elif n3 <= n2 and n3 <= n1 and n3 <= n4:
    menor = n3
    
elif n4 <= n2 and n4 <= n3 and n4 <= n1:
    menor = n4
    

# nums do Meio

# N4
if maior == n1 and menor == n4:
    if n3 > n2:
        print( menor,n2,n3,maior)
        
    else: print (menor ,n3,n2, maior)
    
elif maior == n2 and menor == n4:
    if n3 > n1:
        print (menor,n1,n3,maior)
    
    else: print (menor, n3, n1, maior)
    
elif maior == n3 and menor == n4:
    if n1 > n2 :
        print(menor, n2, n1, maior)
    else: print(menor, n1, n2, maior)
    
    # inverte
elif maior == n4 and menor == n1:
    if n3 > n2:
        print( menor,n2,n3,maior)
        
    else: print (menor ,n3,n2, maior)
    
elif maior == n4 and menor == n2:
    if n3 > n1:
        print (menor,n1,n3,maior)
    
    else: print (menor, n3, n1, maior)
    
elif maior == n4 and menor == n3:
    if n1 > n2 :
        print(menor, n2, n1, maior)
    else: print(menor, n1, n2, maior)

# N3

elif maior == n1 and menor == n3:
    if n2 > n4:
        print (menor, n4, n2, maior)
    else: print (menor, n2, n4, maior)
    
elif maior == n2 and menor == n3:
    if n1 > n4:
        print(menor, n4, n1, maior)
    else: print(menor, n1, n4, maior)

# Inverte

elif maior == n3 and menor == n1:
    if n2 > n4:
        print (menor, n4, n2, maior)
    else:print(menor, n2, n4, maior )
    
elif maior == n3 and menor == n2:
    if n1 > n4:
        print (menor, n4, n1, maior)
    else:print(menor, n1, n4, maior)

# n2

elif maior == n1 and menor == n2:
    if n3 > n4:
        print(menor, n4, n3, maior)
    else: print(menor, n3, n4, maior)

#inverte

elif maior == n2 and menor == n1:
    if n3 > n4:
        print (menor, n4, n3, maior)
    else:print(menor, n3, n4, maior)
    
