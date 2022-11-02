import ent
import produce
class Processor(ent.Ent):
  etype=ent.EntType.ET_PROCESSOR;
  name=""
  owner=None
  inventory=[]   
  req_material=[]
  res_material=[]
  pos=[10,10]; 
  proc_speed=0.1;
  proc_prog=0.0;
  proc_ok=0;
    
        

  def proc_iter(self):
  #  print ("qqqqq")

    if (self.proc_prog==0.0):
      self.temp_list=[]
      for self.it in self.req_material:
        self.t1=self.find_in_inventory_by_otype(self.it)

        if self.t1!=None:
          self.temp_list.append(self.t1)
          self.inventory.remove(self.t1)
          print("remove to processor :")
          print (self.t1)

      print ("self.temp_list")
      print (self.temp_list)
      print ("----")
      print (len(self.req_material));
      print (len(self.temp_list));
      if (len(self.req_material)==len(self.temp_list)):
        print ("kasujemy")
        self.proc_ok=1;
        self.temp_list.clear()
      else:
        print ("zwracamy")
        if (len(self.temp_list)>0):
          self.inventory.append(self.temp_list)

      
      #todrop=self.find_in_inventory(self.req_material[0])
      #if (todrop!=None):
      #  self.drop(todrop)
        
            
    if (self.proc_ok==1):
      self.proc_prog+=self.proc_speed;
      if (self.proc_prog>1.0):
        self.proc_prog=0.0;
        if len(self.res_material)>0:
          for x in self.res_material:
            t_obj=produce.Produce(x)
            t_obj.otype=x;
            
            print (t_obj.otype)
            self.pickup(t_obj)
          self.proc_ok=0;
            

        
  def printout(self):
    print ("------- proc.printout")
    super().printout();
    print("prog:"+str(self.proc_prog));
    print("req_material "+str(self.req_material))
    print("res_material "+str(self.res_material))




  def toJSON(self,indent):
    self.tstr=super().toJSON(indent);
    self.tstr+=indent+',\n'+indent+'"proc_speed": "'+str(self.proc_speed)+'",\n';
    self.tstr+=indent+'"proc_prog": "'+str(self.proc_prog)+'",\n';
    self.tstr+=indent+'"proc_ok": "'+str(self.proc_ok)+'",\n';
    self.tstr+=indent+'"req_matrial":"fff",\n';
    self.tstr+=indent+'"res_matrial":"res"\n';
    return self.tstr;






    


