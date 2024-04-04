### Exerciciu I

Exercísiu sira hodi pratika fórmata string iha Python:

1. **Exercísiu 1**: Fórmata string ho variável sira ne'ebé inklui naran, idade, no profisaun.

```python
nome = "Maria"
idade = 25
profisaun = "doktor"

mensagem = "Nia naran mak {}, idade {}, no profisaun {}.".format(nome, idade, profisaun)
print(mensagem)
```

2. **Exercísiu 2**: Fórmata string ho f-string atu hatudu informasaun kona-ba temperatura no unidade medida.

```python
temperatura = 25.6
unidade = "Celsius"

mensagem = f"Temperatura mak {temperatura} grau {unidade}."
print(mensagem)
```

3. **Exercísiu 3**: Fórmata string atu kalkula total balansu ho variável sira.

```python
saldo_anterior = 1000
kreditu = 500
debitu = 200

balansu_atual = saldo_anterior + kreditu - debitu
mensagem = "Balansu anterior: ${}, Kreditu: ${}, Debitu: ${}, Balansu atual: ${}".format(saldo_anterior, kreditu, debitu, balansu_atual)
print(mensagem)
```

4. **Exercísiu 4**: Fórmata string ho informasaun kona-ba koordenada GPS.

```python
latitude = -8.5489
longitude = 125.5770

mensagem = f"Koordenada GPS: Latitude {latitude}, Longitude {longitude}."
print(mensagem)
```
