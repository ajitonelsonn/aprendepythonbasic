### Exercicius

Alguns exercísiu sira hodi pratika `while` loop iha Python:

1. **Exercísiu 1**: Print númeru husi 1 to'o 10.

```python
num = 1
while num <= 10:
    print(num)
    num += 1
```

2. **Exercísiu 2**: Print númeru kbiit husi 1 to'o 20.

```python
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1
```

3. **Exercísiu 3**: Print "Hello, World!" hamutuk ho númeru sira husi 1 to'o 5.

```python
num = 1
while num <= 5:
    print(f"{num}. Hello, World!")
    num += 1
```

4. **Exercísiu 4**: Halo kalkulasaun ba fatorial númeru ne'ebé ita fornese.

```python
num = int(input("Fornese númeru: "))
fatorial = 1
i = 1
while i <= num:
    fatorial *= i
    i += 1
print(f"Fatorial de {num} é {fatorial}")
```
