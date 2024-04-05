### Exerciciu I

Ita sei halo kalkuladora simples ne'ebé uza `for` loop atu halo kalkulasaun ba númeru sira ne'ebé ita fornese.

Kódigu ba exercísiu:

```python
print("Kalkuladora Simples")
print("Operasaun disponível: +, -, *, /")

operasaun = input("Fornese operasaun: ")
quantidade_numeru = int(input("Fornese kwantidade numeru: "))

resultado = 0

for i in range(quantidade_numeru):
    numero = float(input(f"Fornese númeru {i+1}: "))
    if i == 0:
        resultado = numero
    else:
        if operasaun == '+':
            resultado += numero
        elif operasaun == '-':
            resultado -= numero
        elif operasaun == '*':
            resultado *= numero
        elif operasaun == '/':
            if numero != 0:
                resultado /= numero
            else:
                print("Erro: la bele halo dividasaun husi zero!")
                break
        else:
            print("Operasaun invalidu! Favor fornese operasaun válidu.")
            break

print("Rezultadu:", resultado)
```

Neste kódigu:

- Ita uza `for` loop atu itera iha kada numeru ne'ebé ita fornese.
- Kada numeru ne'ebé ita fornese sei halo operasaun matemátika ho rezultadu ne'ebé iha tiha.
- Ita kontrola se operasaun mak validu, no se numeru mak 0 iha dividasaun, ita printa mensajen erro no interrompe loop.

### Exerciciu II

Kódigu ba exercísiu ho estrutura diferente:

```python
print("Kalkuladora Simples")
print("Operasaun disponível: +, -, *, /")

operasaun = input("Fornese operasaun: ")
quantidade_numeru = int(input("Fornese kwantidade numeru: "))

numeros = []

for i in range(quantidade_numeru):
    numero = float(input(f"Fornese númeru {i+1}: "))
    numeros.append(numero)

resultado = numeros[0]

for numero in numeros[1:]:
    if operasaun == '+':
        resultado += numero
    elif operasaun == '-':
        resultado -= numero
    elif operasaun == '*':
        resultado *= numero
    elif operasaun == '/':
        if numero != 0:
            resultado /= numero
        else:
            print("Erro: la bele halo dividasaun husi zero!")
            break
    else:
        print("Operasaun invalidu! Favor fornese operasaun válidu.")
        break

print("Rezultadu:", resultado)
```

Neste kódigu:

- Ita uza `for` loop atu itera iha kada numeru ne'ebé ita fornese, maibé ha'u uza lista `numeros` atu kaptura numeru sira.
- Depois ita halo operasaun matemátika iha lista `numeros`.
- Kondisaun sira ba operasaun matemátika mak hanesan antes, kontrola se operasaun mak validu no se numeru mak 0 iha dividasaun.
