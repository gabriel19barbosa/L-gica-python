teste = []
end = True
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
        print(teste)