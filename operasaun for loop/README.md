# Operasaun Loop

Iha Python bele uza `for` loop atu iterasaun iha koleksaun husi elemento sira, hanesan list, tuple, string, dictionary, ka set. `for` loop uza estrutura ne'ebé fasil atu komprende no uza iha situasaun sira ne'ebé ita presiza halo repetisaun.

Sintaxe ba `for` loop iha Python:

```python
for item in koleksaun:
    # Halo operasaun ho item ida-idak iha koleksaun
```

Ezemplu simples kona-ba `for` loop:

```python
nomes = ["Ajito", "Nelson", "Lucio"]

for nome in nomes:
    print(nome)
```

Iha ezemplu ne'e, kada elemento iha lista `nomes` sei print iha konsola.

Ita sei kria ejemplu sira ne'ebé uza `for` loop:

1. **Print kada letra iha string**:

```python
texto = "Python"

for letra in texto:
    print(letra)
```

2. **Print kada númeru iha lista**:

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
```

3. **Kalkula total númeru iha lista**:

```python
numeros = [1, 2, 3, 4, 5]
total = 0

for numero in numeros:
    total += numero

print("Total:", total)
```
