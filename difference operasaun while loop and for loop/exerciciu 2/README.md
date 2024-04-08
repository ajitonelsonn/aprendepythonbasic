### Exercicius

Alguns exercísiu sira hodi pratika uzu `for` loop no `while` loop iha Python:

1. **Exercísiu 1**: Print númeru sira husi 1 to'o 10 ho `for` loop.

```python
print("Exercísiu 1: Print númeru sira husi 1 to'o 10 ho for loop")
for num in range(1, 11):
    print(num)
```

```python
print("Exercísiu 1: Print númeru sira husi 1 to'o 10 ho while loop")
num = 1
while num <= 10:
    print(num)
    num += 1
```

2. **Exercísiu 2**: Print númeru kbiit husi 1 to'o 20 ho `for` loop.

```python
print("Exercísiu 2: Print númeru kbiit husi 1 to'o 20 ho for loop")
for num in range(1, 21):
    if num % 2 != 0:
        print(num)
```

```python
print("Exercísiu 2: Print númeru kbiit husi 1 to'o 20 ho while loop")
num = 1
while num <= 20:
    if num % 2 != 0:
        print(num)
    num += 1
```

3. **Exercísiu 3**: Print númeru sira husi 10 to'o 1 ho `for` loop.

```python
print("Exercísiu 3: Print númeru sira husi 10 to'o 1 ho for loop")
for num in range(10, 0, -1):
    print(num)
```

```python
print("Exercísiu 3: Print númeru sira husi 10 to'o 1 ho while loop")
num = 10
while num >= 1:
    print(num)
    num -= 1
```

4. **Exercísiu 4**: Print númeru sira husi 1 to'o 100, maibé labele print númeru ne'ebé kbiit ho 7 ho `for` loop.

```python
print("Exercísiu 4: Print númeru sira husi 1 to'o 100, maibé labele print númeru ne'ebé kbiit ho 7 ho for loop")
for num in range(1, 101):
    if num % 7 == 0:
        continue
    print(num)
```

```python
print("Exercísiu 4: Print númeru sira husi 1 to'o 100, maibé labele print númeru ne'ebé kbiit ho 7 ho while loop")
num = 1
while num <= 100:
    if num % 7 != 0:
        print(num)
    num += 1
```
