# Funsaun ba adisaun
def adisaun(a, b):
    return a + b

# Funsaun ba subtrasaun
def subtrasaun(a, b):
    return a - b

# Funsaun ba multiplikasaun
def multiplikasaun(a, b):
    return a * b

# Funsaun ba dividasaun
def dividasaun(a, b):
    if b == 0:
        return "Erro: la bele halo dividasaun husi zero!"
    else:
        return a / b

print("Kalkuladora Simples")
print("Operasaun disponível: +, -, *, /")

operasaun = input("Fornese operasaun: ")
num1 = float(input("Fornese númeru 1: "))
num2 = float(input("Fornese númeru 2: "))

if operasaun == '+':
    print("Rezultadu:", adisaun(num1, num2))
elif operasaun == '-':
    print("Rezultadu:", subtrasaun(num1, num2))
elif operasaun == '*':
    print("Rezultadu:", multiplikasaun(num1, num2))
elif operasaun == '/':
    print("Rezultadu:", dividasaun(num1, num2))
else:
    print("Operasaun invalidu! Favor fornese operasaun válidu.")