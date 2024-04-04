### Exerciciu I

Pratika operasaun no manipulasaun string iha Python, inklui aumenta tan iha string.

1. **Exercísiu 1**: Aumenta "bomba" iha string "Bomba! Bomba! Bomba!".

```python
string = "Bomba! "
aumenta_tan = "Bomba! " * 2
mensagem = string + aumenta_tan
print(mensagem)
```

2. **Exercísiu 2**: Substitui parte husi string.

```python
mensagem = "Karik sei iha tan aumenta tan."
nova_mensagem = mensagem.replace("aumenta tan", "ho susar")
print(nova_mensagem)
```

3. **Exercísiu 3**: Kria string ho konkatenasaun husi variável sira.

```python
nome = "Maria"
idade = 25
profisaun = "doktor"

perfil = "Nia naran mak " + nome + ", idade " + str(idade) + ", profisaun " + profisaun + "."
print(perfil)
```

4. **Exercísiu 4**: Determina medida husi string no hatudu primeiru lima letra.

```python
texto = "Oloron ipsum dolor sit amet."
medida = len(texto)
primeiru_lim = texto[:5]
print("Medida:", medida)
print("Primeiru lima letra:", primeiru_lim)
```
