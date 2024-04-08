# Kontinue and Pass

`continue` no `pass` sira hanesan instrusaun kontrola fluxu iha Python ne'ebé uza iha loops.

1. **`continue`**: Instrusaun `continue` uza atu pasu wainhira ita iha loop, no ita hakarak para iterasaun ne'e no kontinua ba ita nia loop. Kondisaun sira seluk iha loop sei kontinua halo evaluasaun, maibé kódigu iha bloku wainhira `continue` sei kuda.

   Ezemplu:

   ```python
   for i in range(5):
       if i == 2:
           continue
       print(i)
   ```

   Iha ezemplu ne'e, bainhira `i` igual ho 2, instrusaun `continue` sei pasa no loop sei kontinua ba ita nia iterasaun selanjutnya. Númeru 2 la sei print, maibé númeru sira seluk hanesan 0, 1, 3, 4 sei print.

2. **`pass`**: Instrusaun `pass` uza hanesan plasafera temporáriu. Nia la halo nenhum operasaun, no kódigu kontinua atu executa normal. Uza `pass` wainhira ita iha obrigatoriedade atu inklui instrusaun, maibé ita laiha kódigu konkretu hodi inklui.

   Ezemplu:

   ```python
   for i in range(5):
       if i == 2:
           pass
       else:
           print(i)
   ```

   Iha ezemplu ne'e, bainhira `i` igual ho 2, instrusaun `pass` sei la halo nenhum operasaun, maibé ita sei kontinua ba ita nia loop. Entónia, ita sei print númeru sira seluk hanesan 0, 1, 3, 4.
