#1) Escreva um programa em python que leia dois números decimais, leia a operação desejada 
#dentre adição, subtração, multiplicação ou divisão e mostre o seu resultado com duas casas 
#decimais. Não permita a possibilidade do sistema tentar calcular uma divisão por zero ou a
#leitura de caracteres que não possam ser números.

comando = " "
error = 0
operacao = "0"



while comando != "desligar":
    
    i = 0
    comando = "0"
    
    #Checagem de tipo
    try:
        n1 = int(input("Escreva o primeiro número: "))
        n2 = int(input("Escreva o segundo número: "))
        operacao = input("Qual a operação: ")
    
    except ValueError:
        print ("Você digitou um número errado")
        error = error + 1
        print (f"Você possui {error}/3 erros.")  
        
    #Fim da checagem de tipo
    
    
    #Checa a quantidade de erros
    if error == 3:
        print("Desligando por quantidade de erros excedidos")
        break
    
    
    #Lógica de escolha das contas
    
    if operacao == "0": #Checa se a operação foi escolhida ou houve um value error antes
        breakpoint

    elif operacao == "adição" or operacao == "adicao" or operacao == "+": #Checa algumas maneiras de sinalizar a adição
        res = n1 + n2
        print(f"RESPOSTA: {res:.2f}")
        i = 1

    elif operacao == "subtracao" or operacao == "subtração" or operacao == "-":#Checa algumas maneiras de sinalizar a subtração
        res = n1 - n2
        print(f"RESPOSTA: {res:.2f}")
        i = 1

    elif operacao == "multiplicacao" or operacao == "multiplicação" or operacao == "x" or operacao == "." or operacao == "*": #Checa algumas maneiras de sinalizar a multiplicaçao
        res = n1 * n2
        print(f"RESPOSTA: {res:.2f}")
        i = 1

    elif operacao == "divisao" or operacao == "divisão" or operacao == "/": #Checa algumas maneiras de sinalizar a divisão
        
        if n2 == 0:#Vê se a divisão foi feita por zero
            print("O número não pode ser dividido por zero") 

        else: res = n1 / n2
        print(f"RESPOSTA: {res:.2f}")
        i = 1
        
    else: #Caso não ouve value error, mas a operação foi escrita de maneira errada.
        print ("Você digitou a operação de maneira errada")
        error = error + 1
        print (f"Você possui {error}/3 erros.")
        operacao = '0'
    
    if i == 1:
        comando = input ("Escreva 'desligar' para desligar ou qualquer outra coisa para continuar")
