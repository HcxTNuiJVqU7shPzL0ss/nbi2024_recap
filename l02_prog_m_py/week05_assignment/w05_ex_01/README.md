
# Week 05, Exercise 01

---

## 1 Läsa och förstå kod - diskutera i grupp

Skriv ner vad du tror kommer skrivas ut. \
Skriv sedan in koden i din IDE, exakt som den står, 
och kör den.\
Fick du samma resultat som du trodde? \
Om inte, varför?

---

### 1.1 Vilka ekvivalensklasser har uttrycken?

    1a. x > 100
    1b. y == 42
    1c. len(text) >= 5
    1d. z == True
    1e. 8 < v < 16
    1f. w == 32 or w == 64 or w == 128
    1g. if x < 5: … elif x < 10: … elif x < 15: … else

---

### 1.2
Det har smugit sig in kommentarer i stället för kod på några ställen.\
Skriv färdigt testfallen test_empty_list och test_number_list. 

    # Returnerar summan av alla tal i listan
    def sum_list(list):
        return None
    
    def test_empty_list():
        expected = # ???
        actual = # ???
        assert actual == expected
    
    def test_number_list():
        assert sum_list([5]) == 5
        assert # ???
        assert # ???
        assert # ???

---

### 1.3a
Diskutera följande kod. Räcker det med ett testfall för att 
testa funktionen? 

    # Returnerar ett heltal med antalet vokaler som finns i 
    # ordet (aeiouyåäö)

    def count_vowels(word):
        return None
    
    def test_no_vowels():
        assert count_vowels("qwrt") == 0
        assert count_vowels("Tt") == 0
        assert count_vowels("123 123") == 0
        assert count_vowels("") == 0

---

### 1.3b

Skriv färdigt funktionen count_vowels med hjälp av TDD-metoden, 
red → green → refactor. 

---

### 1.4

Formulera testfall för en funktion som hittar största talet 
i en lista.

    # Returnerar det största talet i listan
    # Returnerar None om det inte finns något
    def find_max(list):

---

### 1.5

Winner takes it all brukar det ju heta, men nu ska vi försöka 
ge lite heder åt alla andrapristagare.\
Formulera testfall för en funktion som hittar näst största 
talet i en lista!

    # Returnerar det nästa största talet i lista
    # Returnerar None om det inte finns något
    # Om det är delad förstaplats så returneras det talet
    def find_2nd_max(list):

---

Student == gnoff

---

Copyright 2026 gnoff

Licensed under the Apache License, Version 2.0 (the "License");\
you may not use this file except in compliance with the License.\
You may obtain a copy of the License at\

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software\
distributed under the License is distributed on an "AS IS" BASIS,\
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or\
implied.\
See the License for the specific language governing permissions and\
limitations under the License.\

---
