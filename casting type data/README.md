# Casting Tipe Dadus

Casting iha Python mak konversaun husi tipu dadus ida ba tipu dadus seluk. Iha situasaun sira ne'ebé ita presiza konverte tipu dadus atu halo operasaun sira ho efikásia, kasting bele útil.

Ita bele uza funsaun sira hanesan `int()`, `float()`, `str()`, etc., atu kaste tipu dadus.

Ezemplu sira:

1. **Kaste husi int iha float**:

   ```python
   x = 5.5
   y = int(x)  # y sei sai 5
   ```

2. **Kaste husi float iha int**:

   ```python
   x = 10
   y = float(x)  # y sei sai 10.0
   ```

3. **Kaste husi int ka float iha string**:

   ```python
   x = "10"
   y = int(x)     # y sei sai 10
   z = float(x)   # z sei sai 10.0
   ```

4. **Kaste husi string iha int ka float**:

   ```python
   x = "10"
   y = int(x)     # y sei sai 10
   z = float(x)   # z sei sai 10.0
   ```

5. **Kaste husi int iha string**:

   ```python
   x = 10
   y = str(x)   # y sei sai "10"
   ```

6. **Kaste husi float iha string**:

   ```python
   x = 3.14
   y = str(x)   # y sei sai "3.14"
   ```
