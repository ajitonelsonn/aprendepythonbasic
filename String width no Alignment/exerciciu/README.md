### Exerciciu I

Exercísiu sira hodi pratika string width no alignment iha Python:

1. **Exercísiu 1**: Kria tabela ho alignment no width ne'ebé adekuadu ba informasaun ida.

```python
# Dados ba tabela
produtus = [
    ("Lapiseira", 2, 1.50),
    ("Kareta Rais", 1, 20.00),
    ("Kadernu", 3, 3.75)
]

# Hatudu tabela
print("PRODUTU         KANTIDADE  PREÇU UNITÁRIU")
for produto in produtus:
    print("{:<15} {:^10} {:>15.2f}".format(*produto))
```

2. **Exercísiu 2**: Kria mensajen ho alignment ne'ebé klaru.

```python
# Dados ba mensajen
nome = "Ana"
idade = 30

# Hatudu mensajen ho alignment
mensagem = "O nome {} iha idade {}.".format(nome, idade)
print("{:^50}".format(mensagem))
```
