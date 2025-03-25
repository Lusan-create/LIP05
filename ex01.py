

#English:

#1) Write a python program that read two decimal numbers, read the operation (add, subtract, multiply, divide) 
# and show the results with two decimal places. Dont allow a division by zero.

# Allow the execution of the program until the user wish to exit the program. Also establish a maximum of 3 attempts
# to input the right information type and inform the user the program is shutting down for too many errors.




#1) Escreva um programa em python que leia dois números decimais, leia a operação desejada 
#dentre adição, subtração, multiplicação ou divisão e mostre o seu resultado com duas casas 
#decimais. Não permita a possibilidade do sistema tentar calcular uma divisão por zero ou a
#leitura de caracteres que não possam ser números.

#permita a execução do programa até uma entrada do usuário desejando sair dele. Também estabeleça um número
#máximo de 3 tentativas de input para quaisquer dados de entrada solicitado errados e  
#informe que o programa será finalizado ao usuáio pela inobservância dos requisitos de 
#entrada.



comando = " "
error = 0
operacao = "0"


#Loop to keep the program running until the user input "desligar" (Shutdown) in the right moment
#Loop para manter o programa rodando até o usuário dar o input "desligar"
while comando != "desligar":
    
    #Resets the commands
    #Reseta os comandos 
    i = 0
    comando = "0"
    
    
    #Checks the data type
    #Checagem de tipo
    try:
        n1 = int(input("Escreva o primeiro número: "))
        n2 = int(input("Escreva o segundo número: "))
        print("Operações: Soma (+), Subtração (-), Multiplicação (*) e Divisão (/)")
        operacao = input("Qual a operação: ")
    
    except ValueError:
        print ("Você digitou um número errado")
        error = error + 1
        print (f"Você possui {error}/3 erros.")  
        

    
    #Checks the errors quantity
    #Checa a quantidade de erros
    if error == 3:
        print("Desligando por quantidade de erros excedidos")
        break
    
    
    #Logic to choose
    #Lógica de escolha das contas
    
    if operacao == "0": #Checa se houve value error / Checks for a value error
        breakpoint

    elif operacao == "adição" or operacao == "adicao" or operacao == "+":
        res = n1 + n2
        print(f"RESPOSTA: {res:.2f}")
        i = 1

    elif operacao == "subtracao" or operacao == "subtração" or operacao == "-":
        res = n1 - n2
        print(f"RESPOSTA: {res:.2f}")
        i = 1

    elif operacao == "multiplicacao" or operacao == "multiplicação" or operacao == "x" or operacao == "." or operacao == "*":
        res = n1 * n2
        print(f"RESPOSTA: {res:.2f}")
        i = 1

    elif operacao == "divisao" or operacao == "divisão" or operacao == "/":
        
        if n2 == 0:#Vê se a divisão foi feita por zero / Check if a division by zero ocurred
            print("O número não pode ser dividido por zero") 

        else: res = n1 / n2
        print(f"RESPOSTA: {res:.2f}")
        i = 1
        
    else: #Caso não ouve value error, mas a operação foi escrita de maneira errada. / No value error, but the operation is written wrong
        print ("Você digitou a operação de maneira errada")
        error = error + 1
        print (f"Você possui {error}/3 erros.")
        operacao = '0'
    
    
    if i == 1: # Da a opção de desligar se a operação ocorreu / Gives the option to shutdown ("desligar") if the operation ocurred
        comando = input ("Escreva 'desligar' para desligar ou qualquer outra coisa para continuar")




