# Differensia operasaun while loop annod for loop

`while` loop no `for` loop sira sira hanesan estrutura kontrola fluxu iha Python, maibé uza kondisaun diferente no iha situasaun sira ne'ebé diferente.

Diferença boot ne'ebé importante atu hatene:

1. **`while` loop**:
   - `while` loop uza kondisaun bo'ot atu determina se loop sei kontinua ka lae.
   - Ita uza `while` loop kada ita la hatene ho pontu ki'ik liu kona-ba quantia repetisaun ka ita la hatene kona-ba kondisaun final.
   - Ita uza `while` loop ameasa ne'ebé ita la kontrola mak hanesan loop infinitu se ita la kuida.

Ezemplu ba `while` loop:

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

2. **`for` loop**:
   - `for` loop uza koleksaun husi elemento sira atu determina repetisaun.
   - Ita uza `for` loop kada ita hatene quantia repetisaun no ita presiza ita uza koleksaun husi elemento sira.
   - `for` loop iha mekanismu kontrola ho'os tanba ita hatene klaru quantia repetisaun.

Ezemplu ba `for` loop:

```python
nomes = ["Ana", "Maria", "José"]
for nome in nomes:
    print(nome)
```

Resumu: `while` loop uza kondisaun bo'ot atu determina repetisaun, enkuantu `for` loop uza koleksaun husi elemento sira. Depende ba situasaun no kuantidade repetisaun, ita bele uza `while` loop ka `for` loop iha Python.
