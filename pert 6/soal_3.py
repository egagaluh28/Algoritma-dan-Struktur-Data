class queue :
    def __init__(self, n):
        self.kapasitas = n
        self.depan = None
        self.belakang = None
        self.isi = 0
        self.data = [None]*n
        
    def enqueue(self, x) :
        print(" ENQUEUE :", x)
        if self.isi < self.kapasitas:
            if self.isi == 0:
                self.depan = self.belakang = 0
            else :
                self.belakang = self.belakang + 1
                if self.belakang == self.kapasitas:
                    self.belakang = 0
            self.data[self.belakang]= x
            self.isi = self.isi + 1
        else :
            print("gagal enqueue")
            
    def dequeue(self):
        if self.isi > 0 :
            hasil = self.data[self.depan]
            self.depan = self.depan + 1
            if self.depan == self.kapasitas:
                self.depan = 0
            self.isi = self.isi - 1
        else :
            print("GAGAL DEQUEUE")
            hasil = None
        return hasil
    
    def vis (self):
        print ("")
        
        for i in range (self.kapasitas, 0, -1) :
            print("   [%2s]   "%(i), end="")
        print("")
        
        for i in range(self.kapasitas):
            print("=========== ", end="")
        print("")
        
        kosong = self.kapasitas - self.isi
        for i in range (kosong):
            print(" %-8s >>"%(""), end="")
            
        posisi = self.belakang
        for i in range (self.isi):
            print(" %-8s >>"%(self.data[posisi]), end="")
            posisi = (posisi - 1)
            if posisi < 0 :
                posisi = self.kapasitas-1
        print(" [DEPAN] ")
        for i in range (self.kapasitas):
            print("=========== ", end="")
        print("")
        
q1 = queue (5)
q1.vis()

q1.enqueue("Bintang")
q1.enqueue("Bulan")
q1.enqueue("Matahari")
q1.vis()

q1.dequeue()
q1.vis()
        