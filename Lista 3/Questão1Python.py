def área(basemaior, basemenor, altura):
    a = (basemaior * basemenor) *altura /2
    print(f"A área do trapézio é: {a}cm²")

basemenor = float(input("Digite o valor da base menor em centímetros: "))
basemaior = float(input("Digite o valor da base maior em centímetros: "))
altura = float(input("Digite o valor da altura em centímetros: "))
área(basemaior, basemenor, altura)
