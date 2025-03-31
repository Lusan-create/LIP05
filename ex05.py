# Escreva um programa para aprovar  o empréstimo bancário para compra de uma casa. O programa
# deve perguntar o valor da casa, o salário, e a quantidade de anos a pagar. O valor da prestação 
# mensal não pode ser maior que 30% do salario. Calcule o valor da prestação como sendo o valor 
# da casa dividido pelo numero de meses a pagar. Não permita o empréstimo se a condição citada 
# não for atendida. 
# Não permita a entrada de valores que não sejam números.

# Modificar todos os exercicios condicionais para permitirem sua
# execução até uma entrada do usuário desejando sair dele. Também estabeleça um número
# máximo de 3 tentativas de input para quaisquer dados de entrada solicitado errados e  
# informe que o programa será finalizado ao usuáio pela inobservância dos requisitos de 
# entrada.

comando = ""
error = 0
loop = 0
while comando != "desligar" and error < 3:
    
    try:
        valorSalario    = float(input("Escreva o valor do salario: "))
        valorCasa       = float(input("Escreva o valor da casa: "))
        tempoEmprestimo = float(input("Escreva a quantidade de anos a pagar: "))
        
    except ValueError:
        error = error + 1
        print("As informações estão escritas de forma errada você possui ", 3 - error," erros restantes")
        loop = 1
    
    
    
    # Calculo da prestação
    if loop == 0:
        # Tranformação dos anos para mês
        tempoEmprestimo = tempoEmprestimo * 12
    
        #valor final da prestção
        prestação = valorCasa / tempoEmprestimo
    
    
        # Aprovação do emprestimo
    
        if prestação <= (valorSalario * 0.3):
            print(f"Prestação aprovada. Valor: R${prestação:0.2f}")
        
        else: print(f"Valor da prestação (R${prestação:0.2f}) acima de 30% do salário")
        
    if loop == 0:
        comando = input("Escreva 'desligar' para desligar o programa ou qualquer outra coisa para continuar")
