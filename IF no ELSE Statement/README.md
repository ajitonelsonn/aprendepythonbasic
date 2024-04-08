# IF no ELSE Statement

`if` no `else` statement iha Python uza atu kontrola fluxu husi programa. `if` statement halo avaliasaun ba kondisaun no deside se operasaun ne'ebé iha iha bloku `if` ka `else` mak sei exeikuta.

Ezemplu sintaxe ba `if` no `else` statement:

```python
if kondisaun:
    # halo operasaun se kondisaun verdadeiru
else:
    # halo operasaun se kondisaun falsu
```

Ezemplu ho `if` no `else` statement:

```python
naran = "Jedy"
idade = 21

if idade >= 18:
    print(""+ naran +" Ita iha idade legal atu partisipa iha votasaun.")
else:
    print(""+ naran +" Ita seidauk iha idade legal atu partisipa iha votasaun.")
```

Iha ezemplu ne'e, programa sei hatene se idade mak iha idade legal atu vota ka lae. Se idade mak 18 ka liu, programa sei hatene "Ita iha idade legal atu partisipa iha votasaun.", kontrariu, programa sei hatene "Ita seidauk iha idade legal atu partisipa iha votasaun.".

`else` statement sempre dependent ba `if` statement ne'ebé precede, no sei exeikuta ita ba kondisaun falsu.

Ita bele utiliza `if` no `else` statement hodi kontrola fluxu husi programa no deside kona-ba operasaun ne'ebé tenki exeikuta bazeia ba kondisaun.
