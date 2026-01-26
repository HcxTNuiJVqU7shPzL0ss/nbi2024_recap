
# Lesson 02, Week 06, Exercise 02  

---

## 2 Länder  

---

### 1 a:  

På Island bor det 383726 invånare och i Danmark 5961249.  
Skapa objekt för länderna.  
(Data från januari 2024. Avrunda befolkningen.)  

    class Country: 
        def __init__(self, name, pop): 
            self.__name = name 
            self.__population = pop
    
    se = Country("Sverige", 10.5) 
    no = Country("Norge", 5.5) 

---

### 1 b:  

Lägg till en metod med namnet "print_info".  
Om man anropar den för Sverige-objektet ska den skriva ut:  

     "I Sverige bor det 10.5 miljoner invånare".  
 
Funktionen ska använda sina egenskaper, så att den fungerar 
för de andra länderna också.  

---

### 1 c:  

Lägg till landets area som en egenskap till klassen.  
Använd en parameter till konstruktorn, alltså __init__ metoden.  
Ge arean ett default värde på None så att man inte måste ange 
arean när man skapar ett landsobjekt.  
Exempel på default värde för en vanlig funktion:  

    # y har default värde 10 
    def exempel(x, y=10): 
    print(x + y) 
    
    exempel(2)  # skriver ut 12

---

### 1 d:  

Ändra i metoden "print_info" så att den skriver ut arean också, 
men bara om arean inte är None.  

---

### 1 e:  

Skapa en ny metod med namnet "add_language".  
Den ska lägga till ett av landets officiella språk.  
(Sverige har bara ett, men Finland har två språk 
(svenska och finska) och Schweiz har fyra.)  
För att kunna spara ett varierande antal behöver du använda 
en lista.  

---

### 1 f:  

Ändra i "print_info" så att den skriver ut alla officiella språk, 
på en ny rad.  

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
