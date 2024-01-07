class stack :
    def __init__(self, n=5):
        self.size = n
        self.bnyk_itemnya = 0
        self.top = -1
        self.data = []
        print("objek stack dibuat dengan kapasitas sebesar :", n)
        
    def info (self):
        print("info detail stack")
        print("kapasitas", self.size)
        print("jumlah item saat ini", self.bnyk_itemnya)
        if self.top !=-1:
            print("top", self.top, "-", self.data[self.top])
        else:
            print("top : -")
        print("list data", self.data)
        
s = stack (10)
s.info()