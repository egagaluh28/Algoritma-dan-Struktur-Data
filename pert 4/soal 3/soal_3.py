class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def update(self, position, new_data):
        y = self.head
        counter = 0
        while y is not None:
            if counter == position:
                old_data = y.data
                y.data = new_data
                return old_data
            counter += 1
            y = y.next
            
        return None
    
    def print(self):
        y = self.head
        while y != None:
            print(y.data, "<==>", end=" ")
            y = y.next
        print("", )
        
    def delete(self, data):
        hapus = self.head
        if hapus and hapus.data == data:
            self.head = hapus.next
            hapus = None
            return
        previous_node = None
        while hapus and hapus.data != data:
            previous_node = hapus
            hapus = hapus.next
        if hapus is None:
            return
        previous_node.next = hapus.next
        hapus = None

satu = SLL()
satu.head = Node(10)
dua = Node(20)
tiga = Node(30)
opat = Node(40)
satu.head.next = dua
dua.next = tiga
tiga.next = opat
print("==================================")
print("data sebelum dihapus :")
satu.print()
print("==================================")
print("data sesudah dihapus :")
satu.delete(10)
satu.print()
print("==================================")





