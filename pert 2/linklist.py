class node:
    def _init_(self,x=None):
        self.data_val = x
        self.next_val = None

class linkedlist:
    def _init_(self):
        self.head =None

    def print_all(self):
        pos =   self.head; 
        print("Head--->",sep="",end="")
        while pos != None:
            print(pos.data_val,"--->",sep="",end="")
            pos = pos.next_val
        print("|") 

    def len(self):
        pos = self.head
        panjang = 0
        while pos != None:
            panjang +=1
            pos = pos.next_val
        return panjang    


x = node(3)#; print(x,x.data_val,x.next_val)
y = node(1)#; print(y,y.data_val,y.next_val)
L = linkedlist()#; print(L)

L.head = x
L.head.next_val = y
#print(L.head.data_val)
#print(L.head.next_val)
#print(L.head.next_val.data_val)

z = node(7)#; print(z)
y.next_val = z
w = node(100)
z.next_val = w
#L.head.next_val.next_val = z

L.print_all()
print(L.len())