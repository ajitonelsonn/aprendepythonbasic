# Foti Input Data husi Users

Iha Python, ita bele utiliza funsaun `input()` atu foti input husi usuáriu. Funsain `input()` sei lee linan husi terminal, no ita bele rai input barak ba ita nia programa liuhusi ne'e.

Ezemplu sinples:

```python
# Foti input husi usuáriu
name = input("Hatama ita nia naran: ")

# Hatudu mensajen ho naran ne'ebé usuáriu hatama
print("Ola,", name, "! Benvindu ba Python programming.")
```

Iha ezemplu ne'e, ita utiliza `input()` atu lee naran husi usuáriu. Linha ne'ebé iha mensajen "Foti ita nia naran: " sei hatudu ba usuáriu hodi kaer naran sira iha terminal. Depois, valor ne'ebé introduzidu sei atribui ba variável `name`, no ami sei hatudu mensajen bainhira ita foti naran husi usuáriu ho mensajen "Ola, [naran]! Benvindu ba Python programming.", iha ne'ebé `[naran]` sei sai naran ne'ebé introduzidu husi usuáriu.

Atu foti input husi usuáriu iha forma numeriku, ami bele uza input nian ho funsaun `int()` ka `float()` atu kast-a valor sira ba numeriku. Ei ezemplu:

```python
# Foti input husi usuáriu ho valor numeriku
age = int(input("Hatama ita nia idade: "))

# Hatudu mensajen ho idade ne'ebé usuáriu hatama
print("Ita nia idade mak", age)
```

Iha kódigu ne'e, ita foti idade husi usuáriu, no ami kast-a valor ne'ebé introduzidu ba tipu dadus integer (idad numeriku). Depois, idade ne'ebé foti sei hatudu iha terminal.
