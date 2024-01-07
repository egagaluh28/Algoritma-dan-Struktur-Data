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
            print(y.data, "===>", end=" ")
            y = y.next
        print("||")

satu = SLL()
satu.head = Node(10)
dua = Node(20)
tiga = Node(30)
opat = Node(40)
satu.head.next = dua
dua.next = tiga
tiga.next = opat
print("SLL awal:")
satu.print()
position = 3
new_data = 80
old_data = satu.update(position, new_data)
print(f"Nilai node pada posisi {position} sebelum diupdate adalah {old_data}")
print( "SLL setelah diupdate:")
satu.print()
print(f"Nilai node pada posisi {position} setelah diupdate adalah {new_data}")