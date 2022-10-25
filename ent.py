


class Ent:
    name=""
    owner=None
    inventory=[]   
    pos=[10,10]; 
    def __init__(self,name):
        self.name=name
        self.inventory=[]
        self.pos=[1,1]
        owner=None

    def printout(self):
        print("---")
        print ("ENT:"+self.name+" ["+str(self.pos[0])+","+str(self.pos[1])+"]")
        
        if (self.owner):
            print ("owner :"+self.owner.name)
            
        print ("inventory "+str(len(self.inventory)) +": ")
        
        if len(self.inventory)>0:
            for x in self.inventory:
                # x.printout()
                print(x.name)

        print ("ENT-END:"+self.name)

    def toJSON(self,ident):
        self.retstr=ident+"{\n"
        self.retstr+=ident+'"name": "'+self.name+'",\n';
        self.retstr+=ident+'"position": "'+str(self.pos[0])+', '+str(self.pos[1])+' ",\n';
        if (len(self.inventory)>0):
            self.retstr+=ident+'"inventory":[\n';            
            for self.t in self.inventory:
                self.retstr+=ident+'  {\n'
                self.retstr+=self.t.toJSON(ident+"    ")
                self.retstr+=ident+'  },\n'
            self.retstr+=ident+']\n'
        self.retstr+=ident+"},\n"
        return self.retstr;
    

    


    def pickup(self,obj):
     #   if (self.owner!=None):
     #      self.owner.inventory.remove(self)
        self.inventory.append(obj)
        obj.owner=self

    def drop(self,obj):
        self.inventory.remove(obj)
        obj.owner=None

    def give(self,obj,whom):
        self.inventory.remove(obj)
        obj.owner=whom
        whom.pickup(obj)

    def find_in_inventory(self,name):
        tret=None;
        if len(self.inventory)>0:
            for x in self.inventory:
                if (x.name==name):
                    tret=x;
        return tret;
    
    def proc_iter(self):
        pass
    

    


