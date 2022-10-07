pghora = float(input("Digite o valor da sua hora: "))
hrmes = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salariob = pghora*hrmes
ir = salariob * 0.11
inss = salariob * 0.08
sind = salariob * 0.05
descontos = ir + inss + sind
salariol = salariob - descontos
print(f"Salário bruto R$: {salariob:.2f}")
print(f"Desconto Imposto de renda R$: {ir:.2f}")
print(f"Desconto Inss R$: {inss:.2f}")
print(f"Desconto de sindicato R$: {sind:.2f}")
print(f"O total descontado foi R$: {descontos:.2f}")
print(f"O salário líquido foi de R$: {salariol:.2f}")