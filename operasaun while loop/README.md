# Operasaun  while Loop

`while` loop iha Python uza atu halo repetisaun ba bloku kodigu durante kondisaun determinada sei verdadeira. Enkuantu kondisaun iha `while` loop sei verdadeira, bloku kodigu sei kontinua executa.

Sintaxe ba `while` loop iha Python:

```python
while kondisaun:
    # halo operasaun sira
```

Ezemplu simples kona-ba `while` loop:

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

Iha ezemplu ne'e, bloku kodigu iha `while` loop sei print valor ba "Count" to'o valor 4, tanba kondisaun `count < 5` sei verdadeira.

Ita sei kria ejemplu sira ne'ebé uza `while` loop:

1. **Print númeru sira husi 1 to'o 5**:

```python
num = 1
while num <= 5:
    print(num)
    num += 1
```

2. **Print númeru kbiit husi 1 to'o 10**:

```python
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1
```

3. **Halo kalkulasaun ba fatorial númeru iha lista**:

```python
numeros = [5, 3, 7, 2, 4]
index = 0
while index < len(numeros):
    fatorial = 1
    num = numeros[index]
    for i in range(1, num + 1):
        fatorial *= i
    print(f"Fatorial de {num} é {fatorial}")
    index += 1
```
