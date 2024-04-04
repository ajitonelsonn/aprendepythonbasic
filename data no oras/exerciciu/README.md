### Exerciciu I

Exercísiu sira hodi pratika `datetime` iha Python:

1. **Exercísiu 1**: Hatudu data no oras agora.

```python
import datetime

now = datetime.datetime.now()
print("Data no oras agora:", now)
```

2. **Exercísiu 2**: Kalkula idade husi data ne'ebé fornese.

```python
data_niver = datetime.datetime(2002, 4, 20)
now = datetime.datetime.now()
idade = now.year - data_niver.year - ((now.month, now.day) < (data_niver.month, data_niver.day))
print("Idade:", idade)
```

3. **Exercísiu 3**: Hatudu data ho formatu ne'ebé espesífiku.

```python
now = datetime.datetime.now()
formatu_data = now.strftime("%d/%m/%Y")
formatu_oras = now.strftime("%H:%M:%S")
print("Data:", formatu_data)
print("Oras:", formatu_oras)
```

4. **Exercísiu 4**: Determina semana do ano ba data espesífiku.

```python
data = datetime.datetime(2023, 4, 15)
semana = data.strftime("%U")
print("Semana do ano:", semana)
```
