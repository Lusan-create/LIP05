
# Faça um algoritmo que leia 4 números inteiros e através de uma 
# rotina de repetição e decisão se consiga mostrar na tela os números organizados de forma 
# crescente. Por enquanto não usar listas, conjuntos ou vetores, usar decisões e 
# repetições somente pra resolver essa questão.

# Repita o exercício, porém agora o usuário pode escolher se
# organizado de forma crescente ou decrescente

# Entrada dos numeros
n1      = input("Escreva o primeiro número: ")
n2      = input("Escreva o segundo número: ")
n3      = input("Escreva o terceiro número: ")
n4      = input("Escreva o quarto número: ")
comando = input("Escreva a ordem ('crescente' ou 'decrescente'):  ")

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
        segundo  = n2
        terceiro = n3
        
    else:
        segundo  = n3
        terceiro = n2
    
elif maior == n2 and menor == n4:
    if n3 > n1:
        segundo  = n1
        terceiro = n3
    
    else:
        segundo  = n3
        terceiro = n1
    
elif maior == n3 and menor == n4:
    if n1 > n2 :
        segundo  = n2
        terceiro = n1
        
    else:
        segundo  = n1
        terceiro = n2
    
    # inverte
elif maior == n4 and menor == n1:
    if n3 > n2:
        segundo  = n2
        terceiro = n3
        
    else: 
        segundo  = n2
        terceiro = n3
    
elif maior == n4 and menor == n2:
    if n3 > n1:
        segundo  = n1
        terceiro = n3
    
    else: 
        segundo  = n3
        terceiro = n1
    
elif maior == n4 and menor == n3:
    if n1 > n2 :
        segundo  = n2
        terceiro = n1
        
    else:         
        segundo  = n1
        terceiro = n2

# N3

elif maior == n1 and menor == n3:
    if n2 > n4:
        segundo  = n4
        terceiro = n2
        
    else:         
        segundo  = n2
        terceiro = n4
    
elif maior == n2 and menor == n3:
    if n1 > n4:
        segundo  = n4
        terceiro = n1
        
    else:         
        segundo  = n1
        terceiro = n4

# Inverte

elif maior == n3 and menor == n1:
    if n2 > n4:
        segundo  = n4
        terceiro = n2
        
    else:        
        segundo  = n2
        terceiro = n4
    
elif maior == n3 and menor == n2:
    if n1 > n4:
        segundo  = n4
        terceiro = n1
        
    else:        
        segundo  = n1
        terceiro = n4

# n2

elif maior == n1 and menor == n2:
    if n3 > n4:
        segundo  = n4
        terceiro = n3
        
    else:         
        segundo  = n3
        terceiro = n4

#inverte

elif maior == n2 and menor == n1:
    if n3 > n4:
        segundo  = n4
        terceiro = n3
        
    else:        
        segundo  = n3
        terceiro = n4
        
        

# Saída

if comando == "descrescente":
    print(maior,terceiro,segundo,menor)   
    
elif comando == "crescente":
    print(menor,segundo,terceiro,maior)
    
else : print("Comando errado.")
