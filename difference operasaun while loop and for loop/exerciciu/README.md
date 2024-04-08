### Exercicius

#### Kalkuladora simples uza `while` loop:

```python
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
```

Iha kódigu ne'e, ita uza `while True` atu halo loop infinitu. Ita uza `break` statement atu para loop bainhira ita kaptura input "s". Kada input numeriku ita uza ba halo operasaun matemátika ba resultado. Se input operasaun invalidu ka halo dividasaun husi zero, ita printa mensajen erro no para loop.

#### For Loop

Ita bele uza `for` loop mós hodi implementa kalkuladora simples. Kodeigu iha `for` loop sei iha estrutura loloos hanesan iha `while` loop, maibé ita sei uza `for` loop atu itera iha koleksaun husi input sira ne'ebé fornese husi úzuaris.

Kódigu ho `for` loop ba kalkuladora simples:

```python
print("Kalkuladora Simples")
print("Operasaun disponível: +, -, *, /")

operasaun = input("Fornese operasaun: ")
resultado = 0

numeros = []
while True:
    num = input("Fornese númeru (ka 's' hodi para): ")
    if num == 's':
        break
    num = float(num)
    numeros.append(num)

for num in numeros:
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
```

Diferénsia entre `for` loop no `while` loop:

1. **`while` loop**:

   - Uza kondisaun hodi determina se loop tenki kontinua ka lae.
   - Uza bainhira ita la hatene pontu finál.
   - Uza kondisaun bo'ot.

2. **`for` loop**:
   - Uza koleksaun husi elemento sira hodi determina repetisaun.
   - Uza bainhira ita hatene klaru kuantidade repetisaun.
   - Uza koleksaun ho'os tanba ita hatene kuantidade repetisaun.

Resumu: `while` loop uza kondisaun hodi determina repetisaun, enkuantu `for` loop uza koleksaun husi elemento sira. Depende ba situasaun no kuantidade repetisaun, ita bele uza `while` loop ka `for` loop iha Python.

### Seluk tan

While Loop Oinsa iha For Loop

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

Iha parte ida ne'e, ita bele uza `for` loop mós hodi halao tarefa ne'ebé iha `while` loop. Maibé, importante atu hatene katak `for` loop iha nia maneira atu uza no kondisaun sira hodi determina kuantidade repetisaun mak la klaru iha situasaun ida ne'e.

Kódigu ho `for` loop ba parte ne'ebé hanesan iha `while` loop:

```python
for count in range(5):
    print("Count:", count)
```

Ne'e hanesan kódigu iha `for` loop. Ida ne'e halo ita repete operasaun ho kuantidade ne'ebé determinadu hosi `range(5)`. Ida ne'e mos printa "Count" hamutuk ho númeru husi 0 to'o 4, inkluzivu.

Maibé, iha situasaun ida-ne'e, uza `while` loop mós apropriadu tanba ita hatene kuantidade repetisaun mak la klaru, tanba ne'e `while` loop bele kontinua halo repetisaun bainhira kondisaun hanesan verdadeiru.

Iha parte ne'ebé ita iha kódigu `while` ne'e, ita bele muda atu uza `for` loop hanesan hanesan iha kódigu ida ne'ebé hanesan ne'e:

```python
for count in range(5):
    print("Count:", count)
```

Iha kódigu `for` loop, ita uza `range(5)` atu kria koleksaun husi númeru husi 0 to'o 4. Depois, ita uza `for` loop atu iterasaun iha kada númeru ne'e iha koleksaun, no halo print.

Ne'e modo simples liu hodi halo konta husi 0 to'o 4. Se iha buat sira ne'ebé hatene klaru kuantidade repetisaun, `for` loop bele sai alternativa ne'ebé di'ak.
