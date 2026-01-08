
# Week 04, Exercise 04

---

## Pokerhand

När man spelar poker har man en hand med 5 kort, som man hoppas ska 
bli bättre än motståndarnas.\
Du ska bygga en funktion som kan utvärdera en pokerhand och tala om 
hur bra den är.

Exempel på körning:

    poker_hand(cards)
    "Du fick ett par med valören: 5"

---

### 1

Bygg en funktion som slumpar ett spelkort.\
Den ska returnera en lista med två element:\
färg och valör.

Färg kan vara: ruter, hjärter, spader eller klöver.\
Valör kan vara tvåa till ess, för enkelhets skull använder vi 
talen 2 till 14.

Exempel på ett kort:

    ["hjärter", 12]

---

### 2

Bygg en funktion som jämför två spelkort och kan tala om 
ifall de har samma valör.

---

### 3

Bygg första versionen av poker_hand(cards).\
Med hjälp av de andra funktionerna ska den ta reda på om 
man har ett par, dvs det finns två kort med samma valör.

---

Fortsätt att lägga till fler kontroller till funktionen.\
Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:

    pretty_print_card(["hjärter", 5]) → "hjärter fem" 

---

Lista med pokerhänder.

* Ett par (två lika kort)
* Två par
* Tretal (tre lika)
  * _gnoff: Triss_
* Straight (5 kort i följd, t.ex. 7-8-9-10-11)
  * _gnoff: stege_
* Flush / färg (alla kort har samma färg)
* Hus (par och tretal med olika valörer)
  * _gnoff: kåk_
* Fyrtal
* Straight flush (5 kort i följd, med samma färg)
* Femtal
  * _gnoff: Existerar inte i vanlig poker_

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
