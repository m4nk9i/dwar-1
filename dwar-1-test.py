import ent
import processor


print ("===============================")


world=ent.Ent(ent.EntType.ET_UNKNOWN,"world");

a=ent.Ent(ent.EntType.ET_UNKNOWN,"stefan");
b=ent.Ent(ent.EntType.ET_UNKNOWN,"młot");
c=ent.Ent(ent.EntType.ET_PRODUCE,"potato1");
d=ent.Ent(ent.EntType.ET_PRODUCE,"potato2");
e=ent.Ent(ent.EntType.ET_PRODUCE,"potato3");
grunt=ent.Ent(ent.EntType.ET_UNKNOWN,"ground");

world.pickup(a);
world.pickup(b);
world.pickup(c);
world.pickup(d);
world.pickup(e);
world.pickup(grunt);
world.pickup(ent.Ent(ent.EntType.ET_PRODUCE,"carrot"));

dist=processor.Processor(ent.EntType.ET_PROCESSOR,"fries machine");
dist.req_material.append(ent.ObjectType.OT_PRODUCE_POTATO);
dist.res_material.append(ent.ObjectType.OT_PRODUCE_FRIES);
dist.res_material.append(ent.ObjectType.OT_WASTE_PEELING);
dist.pickup(d);
dist.pickup(e);
#dist.proc_ok=1;

b.pos=[6,5];
# b.owner=a;

a.pos=[10,8];
a.pickup(b);
a.pickup(c);
a.give(b,grunt)

grunt.pickup(dist)

a.printout();
grunt.printout();


for x in range(12):
    dist.printout();
    dist.proc_iter();

jso="{\n"
jso+=world.toJSON("  ");
#jso+=",\n";
#jso+=grunt.toJSON("  ");
jso+="}\n"

with open('base.json', 'w') as f:
    f.write(jso)

print(jso);

