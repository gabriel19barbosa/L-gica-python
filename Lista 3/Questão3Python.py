hora = int(input("Digite a hora: "))
minuto = int(input("Digite os minutos: "))
a = "AM"
p = "PM"
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

conversao(hora)
saida(hora)
