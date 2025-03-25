
import math



# 3) Calcule um polinômio do segundo grau através da fórmula de báskara ax²+ bx + c. Não 
# permita o sistema tentar calcular divisão por zero, raiz negativa ou entrada de valores 
# que não sejam números. Mostrar quantas raízes o sistema deve gerar: nenhuma(se for numero
# complexo com raiz negativa, uma ou duas) e seus valores sempre com duas casas decimais.


# Modificar todos os exercicios condicionais para permitirem sua
# execução até uma entrada do usuário desejando sair dele. Também estabeleça um número
# máximo de 3 tentativas de input para quaisquer dados de entrada solicitado errados e  
# informe que o programa será finalizado ao usuáio pela inobservância dos requisitos de 
# entrada.

comando = ""
error   = 0
loop    = 1

while comando != "desligar":
    
    try:
        a = float(input("Escreva o valor de A: "))
        b = float(input("Escreva o valor de B: "))
        c = float(input("Escreva o valor de C: "))
        
    except ValueError:
        error = error + 1
        print(f"Voce escreveu o tipo de dado errado. {error}/3 erros restantes.")
        loop = 0
        
    if 2 * a == 0:
        print("Não é possivel fazer a conta, pois o divizor é 0")
        loop = 2
    
    if loop != 0 and loop != 2:
        
    
        res1 = (b * b)  - 4 * a * c
        
        if res1 > 0:
        
            res1 = math.sqrt(res1)
        
            res1 = (b + res1) / (2 * a)
            
            
    
            res2 = (b * b) - 4 * a * c
        
            res2 = math.sqrt(res2)
        
            res2 = (b - res2) / (2 * a)
        
        
            if res1 == res2:
                
                print(f"\nRESPOSTA: {res1}")

            else:
                print(f"RESPOSTA 01: {res1:.02f}")
                print(f"RESPOSTA 02: {res2:.02f}")
            
        
        else: print("O delta é negativo e não existe raiz quadrada de números negativos")

            
    if loop != 0:
        comando = input("'desligar' para desligar ou qualquer outra coisa para continaur")
        