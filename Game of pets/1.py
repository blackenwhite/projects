#class pet implementation
from random import randrange

p1=Pet("Fid")
print(p1)
for i in range(4):
    p1.clock_tick()
    print(p1)
p1.feed()
p1.hi()
p1.teach("Boo")
for i in range(10):
    p1.hi()
print(p1)

class Pet(object):
    boredom_dec=4
    hunger_dec=6
    boredom_thr=5
    hunger_thre=10
    sounds=['Mrr']
    def __init__(self,name="Bitty"):
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



