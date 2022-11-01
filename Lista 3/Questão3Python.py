def conversao(horaconvertida):
    global c
    if horaconvertida >= 12:
        c = horaconvertida
        c -= 12
    elif horaconvertida<12:
        c = horaconvertida
    return c

def saida(horaconvertida):
    if horaconvertida < 12:
        print(f"{c}:{minuto}{a}")
    else:
        print(f"{c}:{minuto}{p}")

a = "AM"
p = "PM"
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
