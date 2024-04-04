# String width no Alignment

Iha Python, ita bele kontrola width no alignment (alinhamentu) husi string bazeia ba karakter sira ne'ebé ita inklui iha string. Ne'e importante bainhira ita kria output sira ne'ebé formatadu iha maneira ne'ebé di'ak, hanesan tabela ka relatóriu.

Ita bele kontrola width no alignment liu husi fórmata string ho `str.format()` ka f-string. Ita uza notasaun especial ne'ebé inklui dala balun ho {} iha string formatadu atu indika width no alignment.

Exemplos:

1. **Alignment (Alinhamentu)**:

   Ita bele kontrola alinhamentu husi string iha kada fórmata liu husi sinais `-` (left-align), `^` (center-align), ka `>` (right-align).

   ```python
   nome = "Jedy"
   idade = 21

   # Alinhamentu left, center, no right
   print("{:<10}".format(nome))   # Sai "Ana       "
   print("{:^10}".format(idade))  # Sai "   30    "
   print("{:>10}".format(idade))  # Sai "        30"
   ```

2. **Width (Largura)**:

   Ita bele kontrola width husi string ho indikasaun husi dala iha {}.

   ```python
   nome = "Jedy"
   idade = 21

   # Largura 10
   print("{:<10}".format(nome))   # Sai "Ana       "
   print("{:^10}".format(idade))  # Sai "    30    "
   ```
