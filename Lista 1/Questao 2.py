peso = int(input("Digite o peso de peixe em Kg: "))
if peso <= 50:
    print(f"Você está dentro do limite")
if peso > 50:
    print(f"Você está acima do limite e recebeu uma multa de R$4,00 por kg excedente")
multa = (peso - 50)*4
print(f"O valor da multa a ser paga é de R$:{multa:.2f}")
