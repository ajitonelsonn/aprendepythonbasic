# Operadores atribuição

Operadores atribuição (assignment operators) iha Python uza atu atribui valor ba variável. Sira inklui operadores báziku hanesan `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=` no operadores bitwise ho atribuição hanesan `&=`, `|=`, `^=`, `<<=`, `>>=`.

Lista operadores atribuição sira:

1. `=`: Atribui valor ba variável.
2. `+=`: Adiciona valor ba variável.
3. `-=`: Subtrai valor husi variável.
4. `*=`: Multiplica variável ho valor.
5. `/=`: Divide variável ho valor.
6. `//=`: Divide variável ho valor no atribui resultado (division inteira).
7. `%=`: Calcula modulus husi variável ho valor.
8. `&=`: AND bit-a-bit entre variável no valor atribuídu.
9. `|=`: OR bit-a-bit entre variável no valor atribuídu.
10. `^=`: XOR bit-a-bit entre variável no valor atribuídu.
11. `<<=`: Shift left variável ho númeru posisaun atribuídu.
12. `>>=`: Shift right variável ho númeru posisaun atribuídu.

Eis ezemplu sira:

```python
# Operador "="
x = 5   # x sai 5

# Operador "+="
x += 3  # x sai 8 (5 + 3)

# Operador "-="
x -= 2  # x sai 6 (8 - 2)

# Operador "*="
x *= 4  # x sai 24 (6 * 4)

# Operador "/="
x /= 3  # x sai 8.0 (24 / 3)

# Operador "//="
x //= 2 # x sai 4.0 (8.0 // 2)

# Operador "%="
x %= 3  # x sai 1.0 (4.0 % 3)

# Operador "&="
x &= 3  # x sai 0 (100 & 011 = 000)

# Operador "|="
x |= 6  # x sai 7 (000 | 110 = 111)

# Operador "^="
x ^= 5  # x sai 2 (111 ^ 101 = 010)

# Operador "<<="
x <<= 2 # x sai 8 (0010 << 2 = 1000)

# Operador ">>="
x >>= 1 # x sai 4 (1000 >> 1 = 0100)
```
