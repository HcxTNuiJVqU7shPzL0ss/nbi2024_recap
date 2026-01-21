
# Lesson 02, Week 02, Exercise 01

---

## 1 Diskutera i grupp

---

### File Explanations

See [main.py](main.py) in this folder for TAP HT 25D week 2, 
exercise 1, assignment.  

Reference to [discuss_1.py](./og_2024/discuss_1.py) in "og_2024" folder for 
OG 2024 (TAP HT 24D) work.  

Other files are for when working "in between the two courses" on my 
own to get back into it and learn things.  

---

### Assignment Information

Ni kan göra den här uppgiften antingen direkt, 
eller senare i veckan.  
Om ni gör den senare, passa på att kombinera 
med code review.  

1. Vad är syftet med koden?
2. Testkör koden med några olika värden.
3. Finns det några direkta fel i koden?  
 (fel som gör att programmet kraschar)
4. Finns det logiska fel?  
 (programmet gör något annat än det är tänkt)
5. Diskutera möjliga lösningar på felen ni hittat.
6. Diskutera möjliga förbättringar på koden.

---

#### Code example

    is_member = False
    level1 = 100
    level2 = 300
    discount = 0
    
    price = input("Välkommen, köp något dyrt: ")
    price = float(price)
    if price > level1:
        print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
        discount = discount + 10
    if price >= level2:
        print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
        discount = discount + 25
    
    final_price = price * (100 - discount) / 100
    print("Efter rabatter blir priset.... " + final_price)
    
<BR>

![Code example](ex2_1_code_example.png 
"Code example")

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
