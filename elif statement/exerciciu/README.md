### Exerciciu I

Alguns exercísiu sira hodi pratika `elif` statement iha Python:

1. **Exercísiu 1**: Determina kategoria ne'ebé númeru ne'ebé fornese mak iha.

```python
numero = float(input("Fornese númeru: "))

if numero > 0:
    print("Númeru fornese mak positivu.")
elif numero < 0:
    print("Númeru fornese mak negativu.")
else:
    print("Númeru fornese mak zero.")
```

2. **Exercísiu 2**: Determina se temperatura fornese mak friu, mornu, ka ki'ik liu.

```python
temperatura = float(input("Fornese temperatura: "))

if temperatura < 10:
    print("Frio iha.")
elif temperatura < 20:
    print("Mornu iha.")
else:
    print("Ki'ik liu iha.")
```

3. **Exercísiu 3**: Determina se pessoa ne'ebé fornese mak adultu, adolescente, ka labarik.

```python
idade = int(input("Fornese idade: "))

if idade >= 18:
    print("Pessoa ne'ebé fornese mak adultu.")
elif idade >= 13:
    print("Pessoa ne'ebé fornese mak adolescente.")
else:
    print("Pessoa ne'ebé fornese mak labarik.")
```

4. **Exercísiu 4**: Determina dia da semana ba númeru ne'ebé fornese.

```python
dia = int(input("Fornese númeru ba dia (1-7): "))

if dia == 1:
    print("Domingu")
elif dia == 2:
    print("Tersa")
elif dia == 3:
    print("Kuarta")
elif dia == 4:
    print("Kinta")
elif dia == 5:
    print("Sesta")
elif dia == 6:
    print("Sabadu")
elif dia == 7:
    print("Domingu")
else:
    print("Númeru labele iha intervalu husi 1-7.")
```
