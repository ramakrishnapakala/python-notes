'''p = True;
q  = True;
r = 1;
s = 1.0;
s2 = 1.0;
print(p is not q,id(p),id(q));#f
print(q is not r,id(q),id(r))#t
print(r is not s)#t
print(s is not s2) #f
l1 = [10,"py"]
l2 = [10,"py"]
print(id(l1),id(l2),l1 is l2)
l3 = l1;
print(id(l1),id(l3),l1 is l3)
l3[-1] = "one";#mutable
print("l1",l1,"l3:",l3)
a = 10;
b =a;
a = 100; #immutable
print(a,b)
'''
s = "python";
print("py" in s);
print("y" in s);
print("js" in s);#f
print("P" in s);#f
''' == will complete content
in will check  given value or
object '''
print("py" == "python");
print("yp" in "python");
print("p" not in s)#f
print("yp" not in "python");# f



