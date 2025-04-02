
# Faça um algoritmo que leia 4 números inteiros e através de uma 
# rotina de repetição e decisão se consiga mostrar na tela os números organizados de forma 
# crescente. Por enquanto não usar listas, conjuntos ou vetores, usar decisões e 
# repetições somente pra resolver essa questão.


# Entrada dos numeros
n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))
n3 = int(input("Escreva o terceiro número: "))
n4 = int(input("Escreva o quarto número: "))

comando = str(input("[\"C\"] para crescente e [\"D\"] para decrescente: "))

# Processamento

if comando == "c" or comando == "C":

    while n1 > n2 or n2 > n3 or n3 > n4:
    
        if n1 > n2:
            n1 , n2 = n2, n1
        
        elif n2 > n3:
            n2 , n3 = n3, n2
    
        elif n3 > n4:
            n3, n4 = n4, n3

elif comando == "d" or comando == "D":
    
    while n1 < n2 or n2 < n3 or n3 < n4:
        
        if n1 < n2:
            n1 , n2 = n2, n1
        
        elif n2 < n3:
            n2 , n3 = n3, n2
    
        elif n3 < n4:
            n3, n4 = n4, n3
        

print (n1,n2,n3,n4)    
