### Exercicius

#### Alguns exercísiu sira hodi pratika uza `continue` no `pass` instrusaun iha Python:

1. **Exercísiu 1**: Print númeru sira husi 1 to'o 10, maibé labele print númeru 5.

```python
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

2. **Exercísiu 2**: Print númeru kbiit husi 1 to'o 20, maibé labele print númeru 10.

```python
for i in range(1, 21):
    if i == 10:
        pass
    else:
        print(i)
```

3. **Exercísiu 3**: Print númeru sira husi 1 to'o 30, maibé labele print númeru ne'ebé kbiit ho 3.

```python
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)
```

4. **Exercísiu 4**: Print primeiru 5 númeru primu, maibé labele print númeru 2.

```python
count = 0
for num in range(2, 100):
    is_prime = True
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        if count < 5:
            print(num)
            count += 1
        else:
            break
```

#### Alguns exercísiu sira hodi pratika uzu `continue` no `pass` instrusaun iha `while` loop iha Python:

1. **Exercísiu 1**: Print númeru sira husi 1 to'o 10, maibé labele print númeru 5.

```python
num = 1
while num <= 10:
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1
```

2. **Exercísiu 2**: Print númeru kbiit husi 1 to'o 20, maibé labele print númeru 10.

```python
num = 1
while num <= 20:
    if num == 10:
        num += 1
        pass
    else:
        print(num)
    num += 1
```

3. **Exercísiu 3**: Print númeru sira husi 1 to'o 30, maibé labele print númeru ne'ebé kbiit ho 3.

```python
num = 1
while num <= 30:
    if num % 3 == 0:
        num += 1
        continue
    print(num)
    num += 1
```

4. **Exercísiu 4**: Print primeiru 5 númeru primu, maibé labele print númeru 2.

```python
count = 0
num = 2
while count < 5:
    is_prime = True
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        if num != 2:
            print(num)
            count += 1
    num += 1
```
