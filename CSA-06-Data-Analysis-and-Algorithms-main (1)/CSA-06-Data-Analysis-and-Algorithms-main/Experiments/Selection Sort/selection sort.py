def selection_sort(array,size):
    for i in range(size):
        imin = i
        for j in range(i+1,size):
            if arr[j] < arr[imin]:
                imin=j
        temp=array[j];
        array[i]=array[imin];
        array[imin]=temp;
arr =[12,19,55,2,16]
n=len(arr)
print("Array before sorting:")
print(arr)
selection_sort(arr,n);
print("Array after sorting:")
print(arr)
        
