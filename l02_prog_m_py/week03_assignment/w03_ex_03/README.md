
# Week 03, Exercise 03

---

## 3 Kvittouträknaren

---

### Version 1

Gör ett program som upprepade gånger ber användaren skriva in ett tal.\
När man skriver in strängen "quit" eller "avsluta" ska programmet ska 
det räkna ut summan av talen.\
Exempel:

    Välkommen till Kvittokompis! Avsluta genom att skriva: quit 
    Skriv in ett belopp: 25
    Skriv in ett belopp: 50
    Skriv in ett belopp: quit 
    Det blir 75 kr totalt. Välkommen åter!

Tips! För att lösa uppgiften behöver du:\
flera variabler, input, while-loop

---

### Version 2

Programmet ska fråga hur många man är, och tala om hur mycket varje 
person i sällskapet ska betala.

    Hur många är ni? 3
    Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!

---

### Version 3

Programmet ska fråga hur många procent dricks man vill lägga på.\
Om användaren inte skriver något (tom sträng) ska programmet använda 
10% som standardinställning. 

---

### Version 4

Nice to have:\
Prova att använda try+except eller isdigit för att hantera de fall 
när användaren skriver ett felaktigt värde.\

    https://www.w3schools.com/python/python_try_except.asp

    https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-represents-a-number-float-or-int

("Nice to have" handlar om funktionalitet som inte är nödvändig, 
men som är bra att ha.\
Gå gärna vidare till nästa uppgift och återvänd till den här 
om du vill lära dig mer.)

---

### Testa programmet med följande inputs:

**Version 1:**\
100\
10, 20, 15\


**Version 2:**\
100, 1 person\
100, 2 personer\
10, 10, 40 personer\
30, 20, 30, 1 person\


Lägg till egna testfall för dricksen.

---

Student == gnoff

---

Copyright 2025-2026 gnoff

Licensed under the Apache License, Version 2.0 (the "License");\
you may not use this file except in compliance with the License.\
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software\
distributed under the License is distributed on an "AS IS" BASIS,\
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or\
implied.\
See the License for the specific language governing permissions and\
limitations under the License.

---
