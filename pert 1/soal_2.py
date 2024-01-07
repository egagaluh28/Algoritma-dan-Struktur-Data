#Muhammmad Galuh Gumelar
#J0403221017

dict = {'Name': 'Sara', 'Age': 7}
#type data kolektif dictionary "dict" serta keys "Name" dan "Age" dan juga  memiliki nilai value "Sara" dan "Age"
dict2 = {'Sex': 'female', 'Birth': 1998}
#type data kolektif dictionary "dict" serta keys "Sex" dan "Birth" dan juga memiliki nilai value "female" dan "1998"
dict3 = {"dict1": dict, "dict2":dict2}
#Type data kolektif yang memanggil "dict" dan "dict2"
print(dict3) #cetak dict3

dict.update(dict2)#
#menambahkan sebuah item "dict2" kedalam "dict"
print("Value : %s" % dict)
#cetak nilai value dari "dict" setelah di update