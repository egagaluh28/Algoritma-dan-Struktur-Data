class node:
    def __init__(self,x=None):
        self.data_val = x
        self.next_val = None
        
class linkendlist:
    def __init__(self):
        self.head =None
        
    def print_all():
        pos = L.head;
        while pos !=None:
            print (pos.data_val)
            pos = pos.next_val
                
x = node (3)
y = node (1)
z = node (7)
L = linkendlist()
L.head = x
L.head.next_val = y
#print(L.head.data_val)
#print(L.head.next_val)
#print(L.head.next_val.data_val)
#print(z)
z =  node(7)
y.next_val=z
#L.head.next_val.next_val = z

#pos = L.head; print(pos.data_val)
#pos = L.next_val ; print(pos.data_val)
pos = L.head;
while pos !=None:
    print (pos.data_val)
    pos = pos.next_val