def insertionSort(list):
   for index in range(1,len(list)):

     currentvalue = list[index]
     position = index

     while position>0 and list[position-1]>currentvalue:
         list[position]=list[position-1]
         position = position-1

     list[position]=currentvalue

list = [14,46,43,27,57,41,45,21,70]
insertionSort(list)
print(list)