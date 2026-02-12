
# # Lesson 02, Week 05, Exercise 02  

---

## 2 Öva på TDD

Samla ihop dina funktioner så att de ligger i en eller flera 
moduler.\
Importera och anropa dem från main.py, så att main-filen bara 
innehåller funktionsanrop.

---

### 2.1

a.
Hitta på lämplig testdata till följande funktion, som omvandlar 
grader Celsius till grader Fahrenheit.

    def c_to_f(degree):
        if degree < -273.15:
            return None
        return degree * 9 / 5 + 32

b.
Vilka ekvivalensklasser har parametern degree?

c.
Skriv ett testfall.

---

### 2.2

a.
Betrakta funktionen count_words(sentence), som tar en sträng och 
returnerar antalet ord.\
Ett ord är en serie tecken som separeras av mellanslag.\
Formulera de krav och acceptanskriterier (AK) som ska gälla för 
funktionen.

b.
Skriv testfall som testar alla AK.

c.
Implementera funktionen, så att alla testfall blir gröna.

---

### 2.3

a.
Betrakta funktionen find_median(numbers), som tar en lista med tal 
och returnerar medianen.\
Median är det mittersta talet, t.ex. är medianen 2 för 
listan [1, 2, 1000].\
Om listan har jämnt antal element ska funktionen returnera 
medelvärdet av de två mittersta talen.\
Formulera de krav och acceptanskriterier (AK) som ska gälla för 
funktionen.

b.
Skriv testfall som testar alla AK.

c.
Implementera funktionen, så att alla testfall blir gröna.

---

### 2.4

Betrakta funktionen is_sorted_ascending(numbers).\
Den ska returnera True om listan numbers är sorterad i stigande 
ordning, False annars.

a.
Vilka ekvivalensklasser har numbers?

b.
Formulera krav och acceptanskriterier för funktionen.

c.
Skriv testfall för funktionen.

---

Student == gnoff

---

Copyright 2026 gnoff

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
