
# Lesson 02, Week 04, Exercise 05  

---

## 5 Turtle graphics  

---

Have not had the time to do this for this week, no code for 
for TAP HT 25D week 4, exercise 4, assignment.  

Also did not do this exercise for OG 2024 (TAP HT 24D) work.  

Other files are for when working "in between the two courses" on my 
own to get back into it and learn things.  
See [ex05_turtle_graphics.py](./ex05_turtle_graphics.py) in this 
folder for work done.  

---

### Assignment Information  

Python har ett paket med inbyggda, enkla funktioner för 
grafik: turtle.  
Tänk dig att du har en robotarm som håller en penna mot 
ett papper.  
Man kan ge olika instruktioner till roboten, 
för att styra den.  

Några exempel:  
* forward - gå rakt framåt i standardriktningen 
(peka ursprungligen åt höger)  
* backward - gå bakåt  
* left, right - sväng vänster eller höger ett antal grader, 
360 grader för ett helt varv  
* dot - sätt ut en prick med en viss storlek  
* speed - normal=6, fast=10, maximal=0  

Läs mer här: Turtle graphics — Python 3.13.1 documentation  

    https://docs.python.org/3/library/turtle.html

Kodexempel:  

    import turtle as t 
    
    # Upprepa 3 gånger 
    for x in range(3): 
        t.forward(100) 
        t.left(120)
    
    # Lyft pennan för att flytta utan att rita 
    t.penup() 
    t.forward(200) 
    t.pendown() 
    t.dot(10, "red") 
    t.color("blue" 
    t.forward(50)
    
    # Låt fönstret stanna kvar tills användaren stänger det 
    t.mainloop() 

---

### 5.1  

Skriv en funktion som ritar en kvadrat.  
Längden på sidan ska vara en parameter till funktionen.  

---

### 2

Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, 
utan att rita.  
Tanken är att du ska kunna kombinera den med kvadratfunktionen, 
för att rita flera kvadrater.  

Exempel:  

    for x in range(5): 
        t.square() 
        t.move_next() 

---

### 5.3  

Bygg om koden så att den ingår i en funktion, 
som ritar en komplett cirkel.  
Använd parametrar i stället för värdena 7, 40 och 30.  

Tips 1: vad händer om man varierar värdet på range?  
Tips 2: 360 grader motsvarar ett helt varv.  

    for x in range(7): 
        t.forward(40) 
        t.right(30) 

---

### 5.4  

Skriv funktioner som ritar de enskilda bokstäverna i 
ordet "PYTHON" med turtle-modulen.  
Kombinera dem och försök få bokstäverna att ritas med 
samma storlek, på en rak linje.  

---

Bonusuppgift, lär dig rekursiva funktioner med turtle graphics:  
Python Turtle Meets Fractal Art: A Recursive Journey  

    https://www.turingtaco.com/python-turtle-meets-fractal-art-a-recursive-journey/

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
