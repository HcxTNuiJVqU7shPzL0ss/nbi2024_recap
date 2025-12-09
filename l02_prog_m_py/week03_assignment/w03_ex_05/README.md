
# Week 03, Exercise 05

---

## 5 Gissa talet

---

Gör ett spel som slumpar ett hemligt tal mellan 1 och 100.\
Sedan ska man försöka gissa det.\
Om man gissar för lågt eller för högt ska spelet tala om det.\
Efter att man har gissat rätt ska spelet skriva ut antalet 
gissningar.

---

    # Slumpa ett hemligt tal 
    secret = random.randint(1, 100)

---

    Exempel:
    Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du 
    gissa vilket det är?
    Gissa: 40 
    Nej, det är för lågt! 
    Gissa: 55 
    Nej, det är för högt! 
    Gissa: 51 
    Det är rätt!! Du gjorde det på 3 gissningar.

---

Version 2:\
Skriv ut om man är nära ifall man gissar högst 5 ifrån det rätta svaret.

    "Nu börjar det brännas!"

---

Student == gnoff

---

Copyright 2025 gnoff

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
