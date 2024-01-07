#Muhammmad Galuh Gumelar
#J0403221017

stok = {'mangga':100, 'jeruk':200, 'apel':600}
#3 pasang keys dan value dari type data koleksi dictionary
for akey in stok.keys(): #pengulangan akey di dalam stok keys
    print("key",akey,"berniali", stok[akey])
    #cetak item yang ada di dalam key dengan nilai value
    
for k in stok.keys():#pengulangan k di dalam stok keys
    print("k",akey,"berniali", stok[k])
    #cetak hasil k sesuai dengan nilai value yang ada di dalam stok
    
ks= list(stok.keys()) #variable ks akan mengubah bentuk stok keys ke dalam bentuk list
print(ks)#mencetak ks