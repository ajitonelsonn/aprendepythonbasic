print("Kalkuladora Simples")
print("Operasaun disponível: +, -, *, /")

operasaun = input("Fornese operasaun: ")
resultado = 0

while True:
    num = input("Fornese númeru (ka 's' hodi para): ")
    if num == 's':
        break
    num = float(num)

    if operasaun == '+':
        resultado += num
    elif operasaun == '-':
        resultado -= num
    elif operasaun == '*':
        resultado *= num
    elif operasaun == '/':
        if num != 0:
            resultado /= num
        else:
            print("Erro: la bele halo dividasaun husi zero!")
            break
    else:
        print("Operasaun invalidu! Favor fornese operasaun válidu.")

print("Rezultadu:", resultado)
print(f"Rezultadu:, {num} no-/ {resultado}")