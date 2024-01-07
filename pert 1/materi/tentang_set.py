#x = {"mawar","melati","flamboyan","anggrek"}
x  = set(("mawar","melati","flamboyan","anggrek"))
print(type(x),x)
x.add("kamboja")
x.add("mawar")
x.add("mawar")
x.add("mawar")
print(type(x),x)
#print(x[0]) ga ada indeks

data = ["membaca","menulis","menggambar","menulis","menulis","menulis","menulis","menggambar"]



distinct = set(data)
print(distinct,len(distinct))

if "tulip" in x:
    x.remove("tulip")
    
print(type(x),x)