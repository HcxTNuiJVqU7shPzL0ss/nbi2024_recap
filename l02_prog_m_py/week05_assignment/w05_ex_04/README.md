
# Week 05, Exercise 04

---

## Multiplikationstabellen

Vi behöver en funktion som kan ge oss multiplikationstabellen.  
Parametern "n" talar om vilket tals tabell vi ska skapa.  
Parametern "limit" talar om var vi ska sluta.  
Om vi till exempel frågar efter 3:ans tabell, med limit==4, 
ska programmet räkna ut:  

* 3*1 = 3
* 3*2 = 6
* 3*3 = 9
* 3*4 = 12


    multiplication_table(3, 4) → [3, 6, 9, 12]  
    
    def muliplication_table(n, limit):  
        return None  

Formulera krav och acceptanskriterier.  
Kör sedan red-green-refactor för varje acceptanskriterium.  

---

### Requirements and Acceptance Criteria

>  
> req_001  
> Non integers shall not be accepted, but also not generate 
> TraceBack.   
>  
>> ac_001  
>> If other than an integer is input as either n or limit, 
>> nothing shall be done. Empty list returned.
>> 1. `float`
>> 2. `str`
>> 3. `tuple`
>> 4. `list`
>>  
>  

>  
> req_002  
> Input for n and limit shall be a positive integer.
>  
>> ac_002  
>> Both n and limit shall be positive integers.
>> 1. Positive integer accepted
>> 2. If 0 is used, return empty list
>>  
>  

>  
> req_003  
> For practical purposes, range for n and limit shall be from 
> 1 to 10.
>  
>> ac_003  
>> For the exercise, limit the positive integers from 1 to 10.
>> 1. 1 to 10 accepted and give result
>> 2. Any value larger than 10 return an empty list
>>  
>  

>  
> req_004  
> A list shall be returned, as [n*1, n*2, ..., n*x], 
> where x == limit.
>  
>> ac_004  
>> Any valid input for n and limit shall contain correct number 
>> of integers in the resulting list.
>>  
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
