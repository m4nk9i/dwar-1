from enum import Enum

class EntType(Enum):
    ET_UNKNOWN=0;
    ET_PERSON=1;
    ET_OBJECT=2;
    ET_PRODUCE=3;
    ET_PROCESSOR=4;

class ObjectType(Enum):
    OT_UNKNOWN=0;
    OT_PRODUCE_BANANA=101;
    OT_PRODUCE_POTATO=102;
    OT_PRODUCE_CARROT=103;
    OT_PRODUCE_FRIES=201;
    OT_WASTE_PEELING=901;


class Ent:
    etype=EntType.ET_UNKNOWN;
    name=""
    owner=None
    inventory=[]   
    pos=[10,10]; 

    def __init__ (self,type,name):
        self.etype=type
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
        self.retstr=""        
        #self.retstr=ident+"{\n"
        self.retstr+=ident+'"type": "'+str(self.etype.name)+'",\n';
        self.retstr+=ident+'"name": "'+self.name+'",\n';
        self.retstr+=ident+'"position": "'+str(self.pos[0])+', '+str(self.pos[1])+' "';
        if (len(self.inventory)>0):
            self.retstr+=',\n'+ident+'"inventory":[\n';            
            for self.t in self.inventory:
                self.retstr+=ident+'{\n'
                self.retstr+=self.t.toJSON(ident+"    ")
                if self.t==self.inventory[-1]:
                    self.retstr+='\n'+ident+'}\n'    
                else:
                    self.retstr+='\n'+ident+'},\n'
            self.retstr+=ident+']\n'
 #       else:
 #           self.retstr+="\n";
 #       self.retstr+=ident+"},\n"
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

    def find_in_inventory_by_name(self,name):
        tret=None;
        if len(self.inventory)>0:
            for x in self.inventory:
                if (x.name==name):
                    tret=x;
        return tret;

    def find_in_inventory_by_etype(self,oetype):
        tret=None;
        if len(self.inventory)>0:
            for x in self.inventory:
                if (x.etype==oetype):
                    tret=x;
        return tret;        
    
    def find_in_inventory_by_otype(self,ootype):
        tret=None;
        if len(self.inventory)>0:
            for x in self.inventory:
                if (x.otype==ootype):
                    tret=x;
        return tret;  

    def proc_iter(self):
        pass
    

    


