print("Kalkuladora Simples")
print("Operasaun disponível: +, -, *, /")

operasaun = input("Fornese operasaun: ")
num1 = float(input("Fornese númeru 1: "))
num2 = float(input("Fornese númeru 2: "))

if operasaun == '+':
    print("Rezultadu:", num1 + num2)
elif operasaun == '-':
    print("Rezultadu:", num1 - num2)
elif operasaun == '*':
    print("Rezultadu:", num1 * num2)
elif operasaun == '/':
    if num2 != 0:
        print("Rezultadu:", num1 / num2)
    else:
        print("Erro: la bele halo dividasaun husi zero!")
else:
    print("Operasaun invalidu! Favor fornese operasaun válidu.")