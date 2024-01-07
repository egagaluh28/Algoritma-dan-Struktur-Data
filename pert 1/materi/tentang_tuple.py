x =("kucing","kambing","kuda")
x2 = tuple(("kerbau","kelinci","kecoak"))
print(type(x),x)
print(x[0])
#x[0] = "kelelawar" ERROR
#x.append("kelelawar")  ERROR
#ordered,unchangeable, allow duplicate
y = list(x)
print(type(y),y)
y[0]="kelelawar"
print(type(y),y)
x = tuple(y)
print(type(x),x)