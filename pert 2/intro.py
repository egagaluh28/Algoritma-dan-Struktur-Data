class mobil:
    def __init__(self,m,mo,p,w,t=None):
        self.merek = m
        self.model = mo
        self.plat = p
        self.warna = w
        self.tahun = t
        
    def info(self):
        print("info detail :",self.merek, self.model, self.plat, self.warna, self.tahun)
    
m1 = mobil("toyota","avanza","F1","hitam","2023")
print(type(m1),m1.merek) 
m1.info()
m1.warna="merah"
m1.info()