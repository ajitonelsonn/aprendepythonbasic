# elif Statement

`elif` statement iha Python uza atu adiciona kondisaun sira ne'ebé dependente ba `if` statement. Ita bele uza `elif` hodi testa kondisaun adisionál sira depois de `if` statement, no antes de `else` statement.

Sintaxe ba `elif` statement:

```python
if kondisaun1:
    # halo operasaun se kondisaun1 verdadeiru
elif kondisaun2:
    # halo operasaun se kondisaun2 verdadeiru
elif kondisaun3:
    # halo operasaun se kondisaun3 verdadeiru
else:
    # halo operasaun se nenhuma kondisaun verdadeiru
```

Ezemplu ba `elif` statement:

```python
nota = 85

if nota >= 90:
    print("Nota A")
elif nota >= 80:
    print("Nota B")
elif nota >= 70:
    print("Nota C")
elif nota >= 60:
    print("Nota D")
else:
    print("Nota F")
```

Neste ezemplu, programa sei testa nota ba kada intervalu. Se nota mak 85, programa sei hatene kondisaun "nota >= 80" no print "Nota B", la'ós halo avaliasaun ba kondisaun seluk iha `elif` statement.
