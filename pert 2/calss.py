class motor :
    def __init__(self,m,p):
        self.merek=m
        self.platno=p
        
    def printinfo(self):
        print("info:",self.merek, self.platno)
        
    def cetak10xinfo(self):
        for i in range(10):
            self.print__info
            
x = motor("yamaha","z1000ab")
y=motor("honda","anjay")
print(type(x))
x.printinfo()
x.cetak10xinfo(3)