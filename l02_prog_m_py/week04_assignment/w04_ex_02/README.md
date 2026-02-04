
# Lesson 02, Week 04, Exercise 02  

---

## 2 Öva på funktioner och moduler  

---

See [main.py](./src_tapht25d/main.py) in folder "src_tapht25d" 
for TAP HT 25D week 4, exercise 1, assignment.  

Reference to file [main.py](./og_2024/main.py) 
in "og_2024" folder for OG 2024 (TAP HT 24D) work.  

Other files are for when working "in between the two courses" on my 
own to get back into it and learn things.  

---

### Assignment Information  

Samla ihop dina funktioner så att de ligger i en eller flera 
moduler.  
Importera och anropa dem från main.py, så att main-filen bara 
innehåller funktionsanrop.  

---

#### 1  

Skriv en funktion som tar en sträng som parameter.  
När den anropas ska den skriva ut strängen och 
"är en fena på programmering".  

Exempel:  

    my_function("David") → "David är en riktig hacker"

---

#### 2  

##### 2a  

Skriv en funktion med namnet `eko`.  
När den anropas med en sträng ska den upprepa strängen, 
och skriva ut resultatet.  

Exempel:  

    eko("hej") → skriver ut "hejhej" 

##### 2b  

Lägg till en parameter `count`, som avgör hur många 
ekon som ska skapas.  

Exempel:  

    eko("hej", 3) → skriver ut "hejhejhej" 

---

#### 3  

Följande kod ska sluta loopa efter 5 varv.  
Flytta den in i en funktion och justera den enligt 
kommentaren.  

    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        # avsluta loopen med en if-sats här
    print(y)

---

#### 4  

Skriv en funktion med namnet `last`.  
Den ska ta en lista som parameter och returnera 
det sista elementet i listan.  

    last([1, 2, 3]) → 3

---

#### 5  

Skriv en funktion med namnet `cut_edges`.  
Den ska ta en lista som parameter.  
När den anropas ska den returnera en ny lista, 
där den har tagit bort första och sista elementet.  

    cut_edges([1, 2, 3, 4]) → [2, 3]

---

#### 6  

Lös felen i koden.  

    def increase(x):
        return x
        x += 1
    print(increase(1))

---

#### 7  

Bygg en funktion med namnet `average`.  
Den ska ta parametrar: x och y.  
Båda ska vara tal.  
Funktionen ska returnera medelvärdet.  
Till exempel så räknar man ut medelvärdet av 4 och 8 genom med 
formeln:  
(4 + 8) / 2  
vilket blir 6.  

Tips: det kan vara enklare att använda fler variabler.  

---

#### 8  

Gör en funktion som kan skriva ut innehållet i en lista 
lite snyggare.  
Först ska funktionen tala om ifall listan är tom, 
eller hur många element den har.  
Sedan ska funktionen skriva ut elementen i en 
punktlista.  

Exempel:  

    pretty_print(["a", "b", 3.14]) 

Listan har 3 element:  

1. a  
2. b  
3. 3.14  

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
