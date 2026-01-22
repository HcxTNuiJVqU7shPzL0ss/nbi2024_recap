
# Lesson 02, Week 02, Exercise 05

---

## 5 Miniräknare

---

### File Explanations

See [main.py](main.py) in this folder for TAP HT 25D week 2, 
exercise 1, assignment.  

Reference to [calculator_5.py](./og_2024/calculator_5.py) 
in "og_2024" folder for OG 2024 (TAP HT 24D) work.  

Other files are for when working "in between the two courses" on my 
own to get back into it and learn things.  

---

### Assignment Information

1  
Gör ett program som frågar användaren efter 3 tal.  
Sedan ska det räkna ut vad summan blir, och skriva ut 
på konsolen.  
(summa: tal1 + tal2 + tal3)  

---

2  
Programmet ska tala om vilket som är det största talet, 
utan att använda Python-funktionen `max`.  
Använd i stället `if/elif/else`.  
Fundera på om man kan lösa uppgiften på olika sätt.  

---

3  
Programmet ska tala om ifall två av talen är lika, 
eller alla tre är lika.  

---

4  
Programmet ska tala om vilket som är det mellersta talet.  
Observera att det bara finns ett mellersta tal om alla tre är 
olika, eller alla tre är lika.  
(Om talen skulle vara till exempel 2, 2, 5 så räknas inget av 
dem som mellerst i den här uppgiften.)  

---

För att testa systematiskt kan du göra en tabell.  
Kör sedan programmet.  
Kontrollera att programmet skriver ut samma saker som du har 
skrivit in i tabellen.  
Vi kallar talen t1, t2 och t3.  

Förslag på värden att testa med:  
1 2 3,  
1 3 2,  
3 2 1,  
-1 -3 -1,  
9 9 9,  
32 32 16  

**Tabell för testning:**

| t1 | t2 | t3 | Summa | Störst | Två lika? | Tre lika? | Mellerst? |
|:--:|:--:|:--:|:-----:|:------:|:---------:|:---------:|:---------:|
| 1  | 2  | 3  |   6   |   3    |    nej    |    nej    |     2     |
| 1  | 3  | 2  |   6   |   3    |    nej    |    nej    |     2     |
| 3  | 2  | 1  |   6   |   3    |    nej    |    nej    |     2     |
| -1 | -3 | -1 |  -5   |   -1   |    ja     |    nej    |    nej    |
| 9  | 9  | 9  |  27   |   9    |    nej    |    ja     |     9     |
| 32 | 32 | 16 |  80   |   32   |    ja     |    nej    |    nej    |

---

Student == **_gnoff_**  

---

Copyright 2025-2026 gnoff

Licensed under the Apache License, Version 2.0 (the "License");  
you may not use this file except in compliance with the License.  
You may obtain a copy of the License at  

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software  
distributed under the License is distributed on an "AS IS" BASIS,  
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or 
implied.  
See the License for the specific language governing permissions and  
limitations under the License.

---
