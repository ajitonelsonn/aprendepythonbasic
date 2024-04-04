# String

String iha programasaun komputador hanesan sériu husi karakter sira ne'ebé uza hodi reprezenta tekstu. Iha Python, ita bele uza aspas simples (`'`) ka aspas dobru (`"`) hodi kria string.

Ezemplu:

```python
nome = "Ana"
saudasaun = 'Ola, mundu!'

print(nome)
print(saudasaun)
```

Output:

```
Ana
Ola, mundu!
```

String bele konsiste husi letra, númeru, ka karakter sira seluk. Ita bele halo operasaun sira ho string, hanesan konkatenasaun (junta string sira), ka manipulasaun ba parte sira husi string.

Ezemplu sira:

```python
# Konkatenasaun
saudasaun = "Ola," + " " + "mundo!"
print(saudasaun)  # Sai "Ola, mundo!"

# Manipulasaun ba parte sira husi string
mensagem = "Ola, mundo!"
print(mensagem[0])   # Sai "O"
print(mensagem[5:])  # Sai "mundo!"
```

Output:

```
Ola, mundo!
O
mundo!
```

String iha Python bele uza operadores sira hanesan `+` (konkatenasaun), `*` (repetisaun), no operadores atribuisaun sira hodi manipula no kria string sira.
