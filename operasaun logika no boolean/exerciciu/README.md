### Exerciciu I

Alguns exercísiu sira hodi pratika operadores logika no boolean iha Python:

1. **Exercísiu 1**: Verifika se númeru iha entre limites ne'ebé determina (5 no 10).

```python
num = int(input("Foti númeru: "))

# Verifika se númeru entre 5 no 10
between_limits = num >= 5 and num <= 10

print("Númeru entre 5 no 10:", between_limits)
```

2. **Exercísiu 2**: Verifika se ema iha tinan legal ba halo atividade jogu kasino (tinan legal mak 18 ka tinan bo'ot liu 18).

```python
idade = int(input("Foti ita nia idade: "))

# Verifika se idade legal atu halo atividade jogu kasino
pode_halodeporte = idade >= 18

print("Ita bele halo atividade desportu:", pode_halodeporte)
```

3. **Exercísiu 3**: Verifika se usuário iha permissaun ba halo edição iha sistema (permissaun bele mak `admin`).

```python
permissaun = input("Foti ita nia permissaun: ")

# Verifika se usuario iha permissaun administrador
tem_permissoes = permissaun == "admin"

print("Ita iha permissaun administrador:", tem_permissoes)
```

4. **Exercísiu 4**: Verifika se cliente bele hola deskontu espesiál iha loja (terdaftar no cliente loyal).

```python
terdaftar = True
cliente_loyal = True

# Verifika se cliente bele hola deskontu espesiál
bele_deskontu = terdaftar and cliente_loyal

print("Cliente bele hola deskontu espesiál:", bele_deskontu)
```
