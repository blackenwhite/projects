#class pet implementation
from random import randrange

class Pet(object):
    boredom_decrement=4
    hunger_decrement=6
    boredom_threshold=5
    hunger_threshold=10
    sounds=['Mrrp']
    def __init__(self,name="Kitty"):
        self.name=name
        self.hunger=randrange(self.hunger_threshold)
        self.boredom=randrange(self.boredom_threshold)
        self.sounds=self.sounds[:] #copy the class attribute so that  we can make changes
                                   #to it, we wont afffect the other pets in the class
    def clock_tick(self):
            self.boredom+=1
            self.hunger+=1
            
    def mood(self):
            if self.hunger<=self.hunger_threshold and self.boredom<=self.boredom_threshold:
                return "happy"
            elif self.hunger > self.hunger_threshold:
                return "hungry"
            else:
                return "bored"
    def __str__(self):
            state="   I'm "+self.name + ". "
            state+="I feel " +self.mood()+". "
            #state+="Hunger {} Boredom {} Words {} ".format(self.hunger,self.boredom,self.sounds)
            return state
        
    def hi(self):
            print(self.sounds[randrange(len(self.sounds))])
            self.reduce_boredom()
        
    def teach(self,word):
            self.sounds.append(word)
            self.reduce_boredom()
        
    def feed(self):
            self.reduce_hunger()
        
    def reduce_hunger(self):
            self.hunger=max(0,self.hunger-self.hunger_decrement)
        
    def reduce_boredom(self):
            self.boredom=max(0,self.boredom-self.boredom_decrement)


#making a pet and playing with it

p1=Pet("Fido")
print(p1)
for i in range(10):
    p1.clock_tick()
    print(p1)
p1.feed()
p1.hi()
p1.teach("Boo")
for i in range(10):
    p1.hi()
print(p1)

#making a program for non-programmer

import sys
#sys.setExecutionLimit(60000)

def whichone(petlist,name):
    for pet in petlist:
        if pet.name==name:
            return pet
    return None

def play():
    animals=[]
    
    option=""
    base_prompt="""
      Quit
      Adopt <petname_with_no_spaces_please>
      Greet <petname>
      Teach <petname> <word>
      Feed <petname>
      
      Choice :"""
    feedback=""
    while True:
        action=input(feedback +"\n"+ base_prompt)
        feedback=""
        words= action.split()
        if len(words) >0:
            command=words[0]
        else:
            command=None
        if command=="Quit":
            print("Exiting..")
            return 
        elif command=="Adopt" and len(words)>1:
            if whichone(animals,words[1]):
                feedback+="You already have a pet with that name\n"
                
            else:
                
                animals.append(Pet(words[1]))
        elif command=="Greet" and len(words) >1:
            pet=whichone(animals,words[1])
            if not pet:
                feedback+="I didnot recognize that pet name.Please try again\n"
                print()
                
            else:
                pet.hi()
        elif command=="Teach" and len(words) >2:
            pet=whichone(animals,words[1])
            if not pet:
                feedback+="I didnot recognize that pet name.Please try again\n"
            else:
                pet.teach(words[2])
                
        elif command=="Feed" and len(words) >1:
            pet=whichone(animals,words[1])
            if not pet:
                feedback+="I didnot recognize that pet name.Please try again\n"
            else:
                pet.feed()
        else:
            feedback+="I didnot recognize that pet name.Please try again\n"
        
        
        for pet in animals:
            pet.clock_tick()
            feedback+="\n" + pet.__str__()
play()