
# Week 04, Exercise 01

---

## 1 Läsa och förstå kod - diskutera i grupp

Skriv ner vad du tror kommer skrivas ut. \
Skriv sedan in koden i din IDE, exakt som den står, 
och kör den.\
Fick du samma resultat som du trodde? \
Om inte, varför?

---

### 1a

    def foo(t):
        print("test")
    
    foo("hej")

---

### 1b

    def fun1(x, y):
        return x * y
    
    print(3, 5)

---

### 1c

    def fun1(x, y):
        return x * y
    
    print(fun1(3, 5))

---

### 1d

    def fun2(i):
        return 5 * i
    
    x = 2
    y = 3
    a = fun2(fun2(x) + fun2(y))
    print(a)

---

### 1e

    a = 5
    def fun3(a):
        a += 1
    
    a += 2
    print(a)

---

### 1f

    def foo(i):
        return 2*i*i
    
    def goo(x, y):
        return x(y)
    
    a = goo(foo, 3);
    print(a)

---

### 1g

Funktionen "isinstance" kan kontrollera en variabels datatyp. \
Vad gör funktionen is_number? \
Går det att förbättra koden?

    def is_number(x):
        if isinstance(x, int):
            return True
        elif isinstance(x, float):
            return True
        return False
    
    print(is_number(5.5))
    print(is_number(42))

---

### 1h

    def average_words(strings):
        found = []
        for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
        return found
    
    average_words(["sup", "how's", "it", "going", "reflecting", "on", 
    "programs", "and", "coding"])

---

### 1i - En uppgift i tre delar:

1. Lista ut vad som är funktionens syfte, baserad på namn och sammanhang. 
2. Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna. 
3. Rätta felen, så funktionen gör det den ska.


    def find_min(numbers):
        counter = 0
        for item in numbers:
            if item < counter:
                counter = item
        print(f"The smallest item is: {counter}")
        return counter
    
    find_min([10, 3, -4, -11])
    find_min([])
    find_min([100])

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
