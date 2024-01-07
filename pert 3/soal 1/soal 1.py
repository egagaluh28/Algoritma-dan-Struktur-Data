class Node:                                             # membuat sebuah class bernama Node
    def __init__(self, dataval=None) :                  # mendeklarasikan sebuah fungsi dari class dengan nilai value dataval none
        self.dataval = dataval                          # fungsi dataval dengan value none
        self.nextval = None                             # fungsi nextval dengan value none
        
class SlinkendList:                                     # membuat sebuah class bernama SlinkendList
    def __init__(self) :                                # mendeklarasikan sebuah fungsi dari class SlinkendList agar bisa diakses 
        self.headval = None                             # fungsi dari headval dengann nilai None
    def listprint(self):                                # fungsi method Listprint untuk mencetak hasil dari Slinkendlist
        printval = self.headval                         # variabel yangdibuat untuk menyimpan head pada linkendlist
        while printval is not None :                    # apabila variabel tidak sama dengan None
            print (printval.dataval, "-->", end="")     # maka mencetak dataval dan menyambungkan
            printval = printval.nextval                 # selama putaran terjadi maka printval akan dirubah menjadi nextval
        print("NULL")                                   # apabila printval.dataval tidak ada maka akan mencetak "NULL"
        
list1 = SlinkendList()                                  # variabel list1 ini akan menjadi class baru dari SlinkendList
list1.headval = Node(1)                                 # list1 headval akan diisikan dengan nilai 1 
e2 = Node(3)                                            # e2 adalah class yang berisi nilai "3"
e3 = Node(4)                                            # e3 adalah class yang berisi nilai "4"
e4 = Node(10)                                           # e4 adalah class yang berisi nilai "10"

list1.headval.nextval = e2                              # mengirimkan nilai e2 ke dalam headval

e2.nextval = e3                                         # mengirimkan nilai e2 ke dalam data node e2
e3.nextval = e4                                         # mengirimkan nilai e3 ke dalam data node e4
list1.listprint()