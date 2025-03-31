# English

# I believe the Expression IMC = weight + (height²) is wrong, but it is how my professor sent me.

# 2) Write a python progra, to calculate IMC value (ideial weight) from some specific datas like wheight and height.
# dont allow inputs that arent numbers. The program must bring the results of the IMC, not the account result

#IMC = weight(KG) / (height²(m))

#low Wheight < 18,5
# 18,5 >= normal weight < 25
# 25 >= pre obese < 30
# 30 >= obese grade 1 < 35
# 35 >= obese grade 2 < 40
# Very obesse >= 40

# Allow the execution of the program until the user wish to exit the program. Also establish a maximum of 3 attempts
# to input the right information type and inform the user the program is shutting down for too many errors.

#Brasilian Portuguese

#Acredito que a conta IMC = Peso[kg] ÷ (Altura²[m]) está errada, mas foi como meu professor enviou.

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

while comando != "desçogar" and error < 3: #Loop to keep the program running / Loop para manter o programa funcionando
    
    #Variables
    i   = 0
    imc = 0
    
    # data type check / checagem de tipo de dado
    try:
        altura = float(input("Escreva uma altura: "))
        peso   = float(input("Escreva um peso: "))
        
    except ValueError:
        if error < 3:
            error = error + 1
            print(f"Você cometeu um erro na entrada dos dados {error}/3 \n")
            imc = 999


# Lets find the IMC / Vamos achar o IMC
    if imc != 999:
        imc = peso / (altura * altura)

        if error >= 3:
            print("Você excedeu os erros permitidos pelo sistema \n")

        elif imc < 18.5:
            print("Baixo peso")
            i = 1
    
        elif imc >= 18.5 and imc < 25:
            print("Peso normal")
            i =1
    
        elif imc >= 25 and imc < 30:
            print("Pré obesidade")
            i = 1
    
        elif imc >= 30 and imc < 35:
            print("Obesidade grau 1")
            i = 1
    
        elif imc >= 35 and imc < 40:
            print("Obesidade grau 2")
            i = 1
    
        elif imc >= 40:
            print("Obesidade mórbida")
            i = 1
    


    #if 
    if i == 1:
        comando = input("Escreva 'desligar' para desligar ou qualquer outra coisa para continuar: ")



