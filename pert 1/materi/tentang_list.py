x = ["jeruk","apel","belimbing"]
print(type(x),x)
y = list(("durian","kedondong","mangga"))
print(type(y),y)
x[1]="manggis"
x.append("jeruk")
x.append("jeruk")
print(x)
print(x.count("jeruk"))