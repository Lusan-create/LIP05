# 4) O software deve permitir a leitura de um código cifrado (protocolo) que contenha 10 caracteres,
# de uma estação meteorológica, a principio esse código deve trazer os seguintes dados:
# zona de medição = 02 caracteres ==> 01 sul 02 norte 03 leste 04 oeste
# temperatura     = 04 caracteres ==> 0321 ==> temperatura + 32,1ºC ou 1321 temperatura -32,1ºC
# pluviometria    = 04 caracteres ==> 0400 ==> índice pluviométrico 400mm 
# Exemplo se o código recebido for 0402980010 seu software deve decodificar a seguinte informação:
# Campinas, região: Norte,  Temperatura: 29,8ºC, Índice pluviométrico:10mm 
# Não permita que seja digitado um código de menos de 10 caracteres e que não seja um numero
# decimal

# Modificar todos os exercicios condicionais para permitirem sua
# execução até uma entrada do usuário desejando sair dele. Também estabeleça um número
# máximo de 3 tentativas de input para quaisquer dados de entrada solicitado errados e  
# informe que o programa será finalizado ao usuáio pela inobservância dos requisitos de 
# entrada.

comando    = ""
codificado = []
error      = 0

while comando != "desligar" and error < 3:
    
    i = 0
    
    protocolo = list(input("Escreva o protocolo: "))

    #Checa se todas as posiçãoes da lista são números
    for x in protocolo:
        try:
            int(x) == True
        except ValueError:
            error = error + 1
            print("\nA string deve conter apenas números inteiros")
            print(f"Erros restantes: {error}/3")
            i = 1
            break
        
    #checagem de tamanho da o protocolo
    if len(protocolo) != 10:
        print("O protocolo está errado")
        error = error + 1
        i = 1
    
   
    
    if i != 1:
        print (f"\nPrtocolo: {protocolo};\n")
        #Encontrar a zona de medição:
        if protocolo [0] + protocolo [1]   == "01":
            codificado.append("sul")
        
        elif protocolo [0] + protocolo [1] == "02":
            codificado.append("norte")
        
        elif protocolo [0] + protocolo [1] == "03":
            codificado.append("leste")
    
        elif protocolo [0] + protocolo [1] == "04":
            codificado.append("oeste")
        
        else:
            error = error + 1
            print (f"Protocolo escrito errado {error}/3\n")
            i = 1
        
    
    
    if i != 1:
        #Encontrar Temperatura
        print(codificado)
        if protocolo [2] == "0":
            codificado.append(f"+{protocolo [3]}{protocolo [4]},{protocolo [5]}\n")
            print(codificado)
            
        elif protocolo [2] == "1":
            codificado.append(f"{protocolo [3]}{protocolo [4]},{protocolo [5]}\n")
            print(codificado)
            
        else:
            error = error + 1
            print (f"Protocolo escrito errado {error}/3\n")
            i = 1
        
        
        
        

