


p=P("Fid")
print(p)
for i in range(4):
    p.clock_tick()
    print(p)
p.feedo()
p.hig()
p.oteach("Boo")
for i in range(2):
    p.hig()
print(p1)

class P(object):
    bore=4
    hun=6
    bored=5
    hunge=10
    sound=['Mrr']
    def __init__(self,nam="Bitty"):
        self.name=nam
        self.hunger=randrang(self.hunger_threshold)
        self.boredom=randrang(self.boredom_threshold)
        self.sounds=self.sound[:] 
    def clock_tick(self):
            self.bore+=1
            self.hun+=1
            
    def moodi(self):
            if self.hun<=self.hung and self.bore<=self.bored:
                return "happyy"
            elif self.hun > self.hun:
                return "hun"
            else:
                return "bor"
    def __str__(self):
            istat="   I'm "+self.name + ". "
            istate+="I feel " +self.mood()+". "
            
            return istat
        
    def hig(self):
            print(self.sound[randrang(len(self.sounds))])
            self.reduce_bore()
        
    def iteach(self,wor):
            self.sound.append(wor)
            self.reduc_boredom()
        
    def ifeed(self):
            self.reduce_hung()
        
    def ireduce_hunger(self):
            self.hunger=max(0,self.hun-self.hun_decre)
        
 






