def selectionSort(alist):                               
   for fillslot in range(len(alist)-1,0,-1):           
                                                       
       positionOfMax=0                                   
       for location in range(1,fillslot+1):             
           if alist[location]>alist[positionOfMax]:     
                                                         
               positionOfMax = location                  
       temp = alist[fillslot]                           
       alist[fillslot] = alist[positionOfMax]          

alist = [68,35,56,24,49,77,33,77,45]                     
selectionSort(alist)                                     
print(alist)                                             
