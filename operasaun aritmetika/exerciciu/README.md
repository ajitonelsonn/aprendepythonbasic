### Exerciciu I

Iha ne'e ita sei koko exercísiu sira hodi pratika operasaun aritmétika iha Python.

1. **Exercísiu 1**: Kalkula área husi retangulu ho valores ne'ebé fornese.

   ```python
   comprimentu = float(input("Foti komprimentu retangulu: "))
   largura = float(input("Foti largura retangulu: "))

   area = comprimentu * largura

   print("Área husi retangulu mak:", area)
   ```

2. **Exercísiu 2**: Kalkula perimetro husi triângulu ho valores ne'ebé fornese.

   ```python
   lado1 = float(input("Foti medida ba lado 1: "))
   lado2 = float(input("Foti medida ba lado 2: "))
   lado3 = float(input("Foti medida ba lado 3: "))

   perimetro = lado1 + lado2 + lado3

   print("Perimetro husi triângulu mak:", perimetro)
   ```

3. **Exercísiu 3**: Kalkula volume husi kubu ho valores ne'ebé fornese.
   Volume = side _ side _ side

   ```python
   sisi = float(input("Foti medida ba sisi kubu: "))

   volume = sisi ** 3

   print("Volume husi kubu mak:", volume)
   ```

4. **Exercísiu 4**: Kalkula area husi cirkulu ho valores ne'ebé fornese.

   ```python
   raio = float(input("Foti raio husi cirkulu: "))
   pi = 3.14159

   area = pi * (raio ** 2)

   print("Área husi cirkulu mak:", area)
   ```

### Exerciciu II

5. **Exercísiu 5**: Kalkula temperatura iha Celsius konvertidu ba Fahrenheit.

   ```python
   celsius = float(input("Foti temperatura iha Celsius: "))

   # Kalkula temperatura iha Fahrenheit
   fahrenheit = (celsius * 9/5) + 32

   print("Temperatura iha Fahrenheit mak:", fahrenheit)
   ```

6. **Exercísiu 6**: Kalkula média husi notas ne'ebé fornese.

   ```python
   nota1 = float(input("Foti nota 1: "))
   nota2 = float(input("Foti nota 2: "))
   nota3 = float(input("Foti nota 3: "))

   # Kalkula média
   media = (nota1 + nota2 + nota3) / 3

   print("Média husi notas mak:", media)
   ```

7. **Exercísiu 7**: Kalkula valor total ho deskontu.

   ```python
   preco_produto = float(input("Foti prezus produto: "))
   deskontu = float(input("Foti deskontu (%) ne'ebé aplika: "))

   # Kalkula deskontu iha montante
   deskontu_valor = (preco_produto * deskontu) / 100

   # Kalkula total montante ho deskontu
   total = preco_produto - deskontu_valor

   print("Prezus total ho deskontu mak:", total)
   ```
