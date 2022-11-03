from ent import Ent,EntType,ObjectType;

class Produce(Ent):
    etype=EntType.ET_PRODUCE;
    otype=ObjectType.OT_UNKNOWN;
    name=""
    owner=None
    inventory=[]   
    pos=[10,10];     

    def __init__ (self,potype,name=""):
        self.otype=potype
        self.name=name
        self.inventory=[]
        self.pos=[1,1]
        owner=None

    def toJSON(self,indent):        
        self.tstr=super().toJSON(indent);
        self.tstr+=",\n"+indent+'"p_type":"'+str(self.otype.name)+'"\n';
        return self.tstr;