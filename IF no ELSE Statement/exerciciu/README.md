### Exerciciu I

Alguns exercísiu sira hodi pratika `if` no `else` statement iha Python:

1. **Exercísiu 1**:Verifika se númeru ne'ebé fornese mak múltiplu husi 3 no 5 ka labele.

```python
numero = int(input("Fornese númeru: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("Númeru fornese mak múltiplu husi 3 no 5.")
else:
    print("Númeru fornese labele múltiplu husi 3 no 5.")
```

2. **Exercísiu 2**: Determina se númeru ne'ebé fornese mak númeru kbiit (even) ka labele.

```python
numero = int(input("Fornese númeru: "))

if numero % 2 == 0:
    print("Númeru fornese mak númeru kbiit (even).")
else:
    print("Númeru fornese mak númeru ímpar (odd).")
```

3. **Exercísiu 3**: Verifika se númeru ne'ebé fornese mak múltiplu husi 5 ka labele.

```python
numero = int(input("Fornese númeru: "))

if numero % 5 == 0:
    print("Númeru fornese mak múltiplu husi 5.")
else:
    print("Númeru fornese labele múltiplu husi 5.")
```

4. **Exercísiu 4**: Verifika se pessoa ne'ebé fornese mak adultu ka labele.

```python
idade = int(input("Fornese idade: "))

if idade >= 18:
    print("Pessoa ne'ebé fornese mak adultu.")
else:
    print("Pessoa ne'ebé fornese labele adultu.")
```

5. **Exercísiu 6**: Verifika se númeru ne'ebé fornese mak positivu, negativu, ka zero uza operador ternáriu.

```python
numero = float(input("Fornese númeru: "))

resultado = "Númeru fornese mak positivu." if numero > 0 else "Númeru fornese mak negativu." if numero < 0 else "Númeru fornese mak zero."
print(resultado)
```

### Exerciciu II elif

6. **Exercísiu 5**: Verifika se temperatura fornese mak friu, mornu, ka ki'ik liu.

```python
temperatura = float(input("Fornese temperatura: "))

if temperatura < 10:
    print("Frio iha.")
elif temperatura >= 10 and temperatura < 20:
    print("Mornu iha.")
else:
    print("Ki'ik liu iha.")
```

7. **Exercísiu 7**: Verifika se númeru ne'ebé fornese mak númeru pozitivu, negativu, ka zero.

```python
numero = float(input("Fornese númeru: "))

if numero > 0:
    print("Númeru fornese mak númeru pozitivu.")
elif numero < 0:
    print("Númeru fornese mak númeru negativu.")
else:
    print("Númeru fornese mak zero.")
```
