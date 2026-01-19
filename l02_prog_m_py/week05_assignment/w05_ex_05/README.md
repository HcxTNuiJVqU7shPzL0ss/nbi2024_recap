
# Week 05, Exercise 05

---

## Balansera listor

Som en del i ett större program har vi en lista som kan innehålla 
flera element.  
Men elementen kan flyttas mellan denna och en annan lista.  
Vi behöver ett sätt att balansera listorna, så att de har lika 
många element - åtminstone så nära som möjligt.  
Ordningen på elementen är inte viktig.  
Formulera krav och acceptanskriterier.  
Kör sedan red-green-refactor för varje acceptanskriterium.  

---

### Requirements and Acceptance Criteria

>  
> req_001  
> Both inputs shall always be a list.
> 
>> ac_001  
>> If any of the two inputs is not a list, return `None`.
>> 1. `int`
>> 2. `float`
>> 3. `str`
>> 4. `tuple`
>  

>  
> req_002  
> An empty input list shall be accepted.
> 
>> ac_002  
>> Both inputs shall be possible to be an empty list.
>> 1. The first input is empty list
>> 2. The second input is empty list
>> 3. Both inputs are empty lists
>  

>  
> req_003  
> The list shall be possible to be of different length compared 
> to one another.
> 
>> ac_003  
>> The two lists shall not be forced to be of the same length.
>> 1. Both list the same length
>> 2. The first list longer than the other
>> 3. The second list longer than the first
>  

>  
> req_004  
> If one list is more than 1 element longer than the other, the 
> lists shall be balanced so that they differ max of 1 in length.
> 
>> ac_004  
>> No matter the length of the two lists, the output shall 
>> be two balanced lists, where the length list vs list differs 
>> by no more than 1.
>  

>  
> req_005  
> List elements should support all types.
> 
>> ac_005  
>> No matter the type of the element in the two lists, 
>> the function shall support it.
>> 1. `int`
>> 2. `float`
>> 3. `str`
>> 4. `tuple`
>> 5. `list`
>  

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
