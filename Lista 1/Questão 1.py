sexo = input("Digite seu sexo:M ou F: ")
h = float(input("Digite sua altura em M (Ex:1.80m): "))
if sexo == "M":
    peso = (72.7 * h) - 58
if sexo == "F":
    peso = (62.1 * h) - 44.7
print(f"\n Seu peso ideal é {peso:.2f}Kg")
