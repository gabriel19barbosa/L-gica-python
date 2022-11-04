# Logica-python
#Lista 1 questão 1

*Coleta os valores das variáveis.

    sexo = input("Digite seu sexo:M ou F: ")
    h = float(input("Digite sua altura em M (Ex:1.80m): "))

*Métodos utilizados para calcular o peso ideal.

    if sexo == "M":
        peso = (72.7 * h) - 58
    if sexo == "F":
        peso = (62.1 * h) - 44.7

*Retorna para o usuário qual seria seu peso ideal.

    print(f"\n Seu peso ideal é {peso:.2f}Kg")

#Lista 1 questão 2

*Coleta o valor da variável

    peso = int(input("Digite o peso de peixe em Kg: "))

*Métodos utilizados para comparar com a legislação e calcular a multa se necessário.

    if peso <= 50:
        print(f"Você está dentro do limite")
    if peso > 50:
        print(f"Você está acima do limite e recebeu uma multa de R$4,00 por kg excedente")
    multa = (peso - 50)*4

*retorna para o usuário o valor de sua multa.

    print(f"O valor da multa a ser paga é de R$:{multa:.2f}")

#Lista 1 questão 3

*Coleta os valores das variáveis

    pghora = float(input("Digite o valor da sua hora: "))
    hrmes = float(input("Digite a quantidade de horas trabalhadas no mês: "))

*Método para calcular o salario bruto.

    salariob = pghora*hrmes

*Métodos para calcular os impostos

    ir = salariob * 0.11
    inss = salariob * 0.08
    sind = salariob * 0.05
    descontos = ir + inss + sind

*Método para calcular o salario líquido 
    salariol = salariob - descontos

*Retorna ao usuário os valores já calculados
    print(f"Salário bruto R$: {salariob:.2f}")
    print(f"Desconto Imposto de renda R$: {ir:.2f}")
    print(f"Desconto Inss R$: {inss:.2f}")
    print(f"Desconto de sindicato R$: {sind:.2f}")
    print(f"O total descontado foi R$: {descontos:.2f}")
    rint(f"O salário líquido foi de R$: {salariol:.2f}")

#Lista 2 questão 1

*Coleta os valores das variáveis 

    saque = int(input("Digite o valor a sacar R$: "))

*Métodos para calcular a quantidade de notas que o valor digitado usaria.

    cem = int(saque/100)
    saque = saque - (cem*100)
    cinq = int(saque/50)
    saque = saque - (cinq*50)
    dez = int(saque/10)
    saque = saque - (dez*10)
    cinco = int(saque/5)
    saque = saque - (cinco*5)
    um = (saque)

*Retorna ao usuário a quantidade de notas necessárias e quais seriam as notas necessárias para o valor.

    print(f"Notas R$100.00 = {cem}")
    print(f"Notas R$ 50.00 = {cinq}")
    print(f"Notas R$ 10.00 = {dez}")
    print(f"Notas R$ 5.00 = {cinco}")
    print(f"Notas R$ 1.00 = {um}")

#Lista 2 questão 2

*Coleta o valor da variável

    numero = int(input("Digite um numero inteiro: "))

*Método para descobrir se é ímpar ou par

    divisao = numero %2
    if  divisao == 0 :
        print(f"O numero é par")
    else:
        print(f"O numero é ímpar")

#Lista 2 questão 3

*Coleta o valor da variável

    numero = float(input("Digite um numero: "))

*Método para descobrir se é inteiro ou decimal

if(numero // 1 == numero): 
    print('\nNúmero inteiro !')
else:
    print('\nNúmero Decimal !')

#Lista 2 questão 4

*Declaração da lista

    teste = []

*Condição de fim do while

    end = True

*Estrutura de formulário para preenchimento da lista

    while end:
        nome = input("Digite seu nome ")
      altura = input("Qual é a sua altura")
      idade = input("Qual é a sua altura")

      teste.append(nome)
      teste.append(altura)
      teste.append(idade)
      continuar = input("Você deseja continuar?\nDigite 's' para sim e 'n' para parar: ")
      if continuar == 'n':
        end = False

*Retorna ao usuário os valores contidos na lista

    print(teste)


#Lista 3 questão 1

*Função que calcula a área do trapézio

    def área(basemaior, basemenor, altura):
        a = (basemaior * basemenor) *altura /2
        print(f"A área do trapézio é: {a}cm²")

*Chamada de função com parâmetros definidos
    área(basemaior, basemenor, altura)

#Lista 3 questão 2 

*Função que calcula o preço do produto com impostos.

    def soma_imposto (taxa_imposto, custo):
    preçoT = taxa_imposto + custo
    print(f"O preço total do produto com impostos é R$: {preçoT}")

*Variável que define o valor de 10% de impostos a ser cobrado
    taxa_imposto= 0.10 * custo

*Chamada de função com os parâmetros definidos
    soma_imposto(custo, taxa_imposto)

#Lista 3 questão 3 

*Função que converte do formato de 24 horas para o formato de 12 horas
    def conversao(horaconvertida):
    global c
    if horaconvertida >= 12:
        c = horaconvertida
        c -= 12
    elif horaconvertida<12:
        c = horaconvertida
    return c

*Função de saída que diz se a hora é "AM" ou "PM"
    
    def saida(horaconvertida):
    if horaconvertida < 12:
        print(f"{c}:{minuto}{a}")
    else:
        print(f"{c}:{minuto}{p}")

*Estrutura de repetição que diz se o valor de hora é valido e pergunta se quer continuar a conversão
    
    end = True

    while end:
        hora = int(input("Digite a hora: "))
        minuto = int(input("Digite os minutos: "))

        if hora >= 0 and hora <= 24:
            conversao(hora)
            saida(hora)
        else:
            print("Por favor digite uma hora válida")
            break

        continuar = input("você deseja continuar ?Digite S para sim ou N para não.").upper()
        if continuar == "N":
            end = False
