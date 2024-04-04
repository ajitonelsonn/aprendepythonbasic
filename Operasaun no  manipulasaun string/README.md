# operasaun logika no boolean

Operasaun no manipulasaun string hanesan asaun sira ne'ebé ita bele halo ho string sira iha Python. Ne'e inklui konkatenasaun, kaptura medida (length), fatia (slice), peskiza, no transformasaun ba maiúsula ka minúscula, entre operasaun sira seluk.

Lista operasaun no manipulasaun string sira:

1. **Konkatenasaun**: Kombina duas ka buka string sira.

   ```python
   string1 = "Ola,"
   string2 = " mundu!"
   mensagem = string1 + string2
   print(mensagem)  # Sai "Ola, mundu!"
   ```

2. **Kaptura Medida (Length)**: Determina medida husi string.

   ```python
   mensagem = "Ola, mundu!"
   comprimentu = len(mensagem)
   print(comprimentu)  # Sai 12
   ```

3. **Fatia (Slice)**: Buka parte spesífiku husi string.

   ```python
   mensagem = "Ola, mundu!"
   fatia = mensagem[4:9]
   print(fatia)  # Sai "mundu"
   ```

4. **Peskiza**: Prokura string ida iha string seluk.

   ```python
   mensagem = "Ola, mundu!"
   resultado = mensagem.find("mundu")
   print(resultado)  # Sai 5
   ```

5. **Maiúsula ka Minúscula**: Transforma string ba maiúsula ka minúscula.

   ```python
   mensagem = "Ola, mundu!"
   maiusula = mensagem.upper()
   minuscula = mensagem.lower()
   print(maiusula)   # Sai "OLA, MUNDU!"
   print(minuscula)  # Sai "ola, mundu!"
   ```

6. **Substituisaun**: Substitui parte spesífiku husi string.

   ```python
   mensagem = "Ola, mundu!"
   nova_mensagem = mensagem.replace("mundu", "amigu")
   print(nova_mensagem)  # Sai "Ola, amigu!"
   ```
