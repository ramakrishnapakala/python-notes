a = 10;
print(type(a))
b = 10;
print(type(b))
print(id(a),id(b))#104
b = 20; # 100
print(id(a))
print("new of address of b:",id(b))
# mutable
l1 = [10,20]#99
l2 = l1; # 999
print("the l1 is:",l1,id(l1))
print("the l2 is:",l2,id(l2))
l1[0] = "python";
l2[-1] = "one piece"
print(l1[-1])
print("after changing l1")
print("the l1 is:",l1,id(l1))
print("the l2 is:",l2,id(l2))
#complex
c = 10+5.2j;
print(c.real)
print(c.imag)
#float
f1 = 40.5;
f2 = 1e2;
print(type(f1),type(f2))
print(10 > 5)
# constants fix value means non-changeable
PI = 3.14;








