# Break

`break` instrusaun iha Python uza atu para loop, ho hodi sai hosi loop ne'e.

### Ezempluza `break` instrusaun iha `while` loop:

1. **Exercísiu 1**: Print númeru sira husi 1 to'o 10, maibé labele print númeru 5 no labele halo loop bainhira hasai númeru 5.

```python
num = 1
while num <= 10:
    if num == 5:
        break
    print(num)
    num += 1
```

2. **Exercísiu 2**: Halo loop ho `while` atu kalkula soma númeru sira husi 1 to'o númeru ne'ebé ita fornese, maibé hasai loop bainhira númeru ne'ebé fornese mak 0.

```python
total = 0
while True:
    num = int(input("Fornese númeru (ka '0' hodi para): "))
    if num == 0:
        break
    total += num

print("Total:", total)
```

3. **Exercísiu 3**: Halo loop ho `while` atu halo kalkulasaun ba fatorial, maibé hasai loop bainhira ita kalkula fatorial ba númeru 5.

```python
n = 1
fatorial = 1
while True:
    fatorial *= n
    if n == 5:
        break
    n += 1

print("Fatorial de 5 é:", fatorial)
```

### Ezemplu sira ho `break` instrusaun iha `for` loop iha Python sei hanesan:

1. **Exercísiu 1**: Print númeru sira husi 1 to'o 10, maibé labele print númeru 5 no labele halo loop bainhira hasai númeru 5.

```python
for num in range(1, 11):
    if num == 5:
        break
    print(num)
```

2. **Exercísiu 2**: Halo loop ho `for` atu kalkula soma númeru sira husi 1 to'o númeru ne'ebé ita fornese, maibé hasai loop bainhira númeru ne'ebé fornese mak 0.

```python
total = 0
for _ in range(1000):  # Limita ba 1000 iterasaun
    num = int(input("Fornese númeru (ka '0' hodi para): "))
    if num == 0:
        break
    total += num

print("Total:", total)
```

3. **Exercísiu 3**: Print primeiru 5 númeru primu, maibé labele print númeru 2 no labele halo loop bainhira hasai print primeiru 5 númeru primu.

```python
count = 0
for num in range(2, 100):  # Limita ba 100 iterasaun
    is_prime = True
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        if num == 2:
            continue
        print(num)
        count += 1
        if count == 5:
            break
```
