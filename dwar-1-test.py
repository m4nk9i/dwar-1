import ent
import processor


print ("===============================")


world=ent.Ent("world");

a=ent.Ent("stefan");
b=ent.Ent("młot");
c=ent.Ent("potato1");
d=ent.Ent("potato2");
e=ent.Ent("potato3");
grunt=ent.Ent("ground");

world.pickup(a);
world.pickup(b);
world.pickup(c);
world.pickup(d);
world.pickup(e);
world.pickup(grunt);
world.pickup(ent.Ent("carrot"));

dist=processor.Processor("fries machine");
dist.req_material.append("potattto");
dist.res_material.append("fries");
dist.res_material.append("obierki");
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

