# English

# 2) Write a python progra, to calculate IMC value (ideial weight) from some specific datas like wheight and height.
# dont allow inputs that arent numbers. The program must bring the results of the IMC, not the account result

#IMC = weight(KG) + (height²(m))

#low Wheight < 18,5
# 18,5 >= normal weight < 25
# 25 >= pre obese < 30
# 30 >= obese grade 1 < 35
# 35 >= obese grade 2 < 40
# Very obesse >= 40

# Allow the execution of the program until the user wish to exit the program. Also establish a maximum of 3 attempts
# to input the right information type and inform the user the program is shutting down for too many errors.

#Brasilian Portuguese

# 2)Escreva um programa em python para calcular os valores de imc a partir de entradas de 
# dados específicos como peso e altura da pessoa. Não permita a entrada de valores que não 
# possam ser números. O sistema deve trazer o resultado escrito do IMC e não o cálculo.

# IMC = Peso[kg] ÷ (Altura²[m]) 
# baixo peso < 18,5
# 18,5 >= peso normal < 25
# 25 >= pre obesidade < 30
# 30 >= obesidade grau 1 < 35
# 35 >= obesidade grau 2 < 40 
# obesidade mórbida >= 40

# Modificar todos os exercicios condicionais para permitirem sua
# execução até uma entrada do usuário desejando sair dele. Também estabeleça um número
# máximo de 3 tentativas de input para quaisquer dados de entrada solicitado errados e  
# informe que o programa será finalizado ao usuáio pela inobservância dos requisitos de 
# entrada.

comando = ""
error   = 0

while comando != "Shutdown": #Loop to keep the program running / Loop para manter o programa funcionando
    
    # data type check / checagem de tipo de dado
    try:
        altura = int(input("Escreva uma altura: "))
        peso   = int(input("Escreva um peso: "))
        
    except ValueError:
        if error < 3:
            print(f"Você cometeu um erro na entrada {error}/3 \n")
            error = error + 1
        if error >= 3:
            print("VocÇe excedeu os erros permitidos pelo sistema \n")
            break

