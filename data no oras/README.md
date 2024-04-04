# Data no Oras

Iha Python, ita bele uza library `datetime` atu uza ba data no oras (time). Ne'e inklui kalkulasaun, formatasaun, no manipulasaun ba data no oras.

Exemplos kona-ba `datetime`:

1. **Kria Objektu Data no Oras Agora**:

```python
import datetime

now = datetime.datetime.now()
print("Data no oras agora:", now)
```

2. **Kria Objektu Data Específiku**:

```python
data_especifiku = datetime.datetime(2022, 12, 31)
print("Data específiku:", data_especifiku)
```

3. **Formatasaun Data no Oras**:

```python
agora = datetime.datetime.now()
formatu_data = agora.strftime("%Y-%m-%d")
formatu_oras = agora.strftime("%H:%M:%S")
print("Formatu data:", formatu_data)
print("Formatu oras:", formatu_oras)
```

4. **Kalkulasaun Entre Datas**:

```python
data1 = datetime.datetime(2022, 5, 10)
data2 = datetime.datetime(2023, 5, 10)
diferensa = data2 - data1
print("Diferensa entre datas:", diferensa.days, "dias")
```
