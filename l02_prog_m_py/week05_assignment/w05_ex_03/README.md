
# Week 05, Exercise 03

---

## Söka efter användare

Tänk dig en funktion som kan användas för att visa sökresultat 
medan användaren skriver i ett sökfält.  
Funktionen ska ta två parametrar: input är det användaren skriver, 
master_list är en lista med alternativ som kan hittas.  

`def autocomplete_list(input, master_list):`  

Börja med att formulera de krav och acceptanskriterier (AK) som ska 
gälla för funktionen.   
Välj sedan ut ett AK och skriv ett testfall. (red)  
Skriv sedan kod som uppfyller testfallet. (green)  
Städa i koden, så du känner dig nöjd med din kod hittills.  
Fortsätt sedan med nästa AK.  

---

### Comments

The only way I see something similar to this happening 
is by using `input`.  
However, this does not take the user input until user 
presses enter/return.  
Due to this, I do not see how an actual "autocomplete" while 
user is typing shall be possible.  

So "while user is typing" I do not see how to implement in 
Python without further explanation, more to check once user 
has entered text and pressed enter, to check against a list.

---

#### Requirements and Acceptance Criteria


>  
> req_001  
> User input shall be a string of at least one character.
> 
>> ac_001  
>> If other than a string of minimum one character is input, 
>> no match shall be done. Empty list returned.
>> 1. `int`
>> 2. `float`
>> 3. `str < len 1`
>> 4. `tuple`
>> 5. `list`
>  

>  
> req_002  
> Input shall match fully, not partially, against items in 
> master_list.
> 
>> ac_002  
>> If user input string is x characters, all x characters 
>> shall attempt to match against items in master_list.
>> 1. `a` can match to `bad`, but not to `bod`
>> 2. `ar` can batch to `bard`, but not to `bad` or `sore`
>> 3. `mari` can batch against `maria`, but not to `ari`
>  

>  
> req_003  
> An input shall be possible to match against all items in 
> master_list.
> 
>> ac_003  
>> If user input string is x, all items matching x  
>> in master_list shall be returned.
>> 1. If input matches nothing in master_list, return empty list
>> 2. If input matches one up to all in master_list, return list
>> with all that matched
>  

>  
> req_004  
> If master_list is empty, nothing shall match.
> 
>> ac_004  
>> For the case of empty master_list, nothing shall match, no matter 
>> what the input was. An empty list shall be returned.
>  

>  
> req_005  
> Both input and match shall be insensitive to case.
> 
>> ac_005  
>> Case shall not matter when comparing.
>  

>  
> req_006  
> The master_list shall always be a list.
> 
>> ac_006  
>> If master_list is not a list, return `None`.
>> 1. `int`
>> 2. `float`
>> 3. `str`
>> 4. `tuple`
>  

>  
> req_007  
> The master_list shall contain only elements of type `str`.
> 
>> ac_007  
>> If master_list contains any element not of type `str`, 
>> return `None`.
>  

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
