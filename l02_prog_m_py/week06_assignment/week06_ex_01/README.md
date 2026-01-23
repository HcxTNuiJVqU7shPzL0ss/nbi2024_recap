
# Week 06, Exercise 01  

---

## 1 Läsa och förstå kod - diskutera i grupp  

Skriv ner vad du tror kommer skrivas ut.  
Skriv sedan in koden i din IDE, exakt som den står, 
och kör den.  
Fick du samma resultat som du trodde?  
Om inte, varför?  

---

### 1.1 Vad gör följande kod?  

    class SafeStorage: 
        __data = None 
        def get(self): 
            return self.__data 
        def put(self, data): 
            self.__data = data
    
    safe = SafeStorage() 
    safe.put("Anakonda") 
    x = safe.get() 
    safe.put("Boaorm") 
    y = safe.get() 
    print(x, y)

---

### 1.2a Vad gör följande kod? Fixa eventuella fel.  

    class Animal: 
        def make_noise(self): 
            print("Detta djur har vi inget ljud för.")
    
    class Dog(Animal): 
        def make_noise(self): 
        print("Voff!")
    
    class Cat(Animal): 
        def make_noise(shelf): 
            super().make_noise() 
        print("Mjau!")
    
    def sound_off(animal): 
        animal.make_noise()
    
    c = Cat() 
    d = Dog() 
    h = Rooster() 
    sound_off([c, d, h]) 

---

### 1.2b Lägg till en klass för ett annat djur, till exempel en guldfisk.  

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
