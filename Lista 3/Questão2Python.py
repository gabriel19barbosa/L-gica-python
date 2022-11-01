def soma_imposto (taxa_imposto, custo):
    preçoT = taxa_imposto + custo
    print(f"O preço total do produto com impostos é R$: {preçoT}")

custo = float(input("Digite o custo do produto sem os impostos: "))
"""para um imposto de 10%"""
taxa_imposto= 0.10 * custo
soma_imposto(custo, taxa_imposto)