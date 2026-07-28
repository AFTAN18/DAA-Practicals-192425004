def linear_search(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            print("Element found at the index:",i)
            break;
    else:
        print("Element is not found!")
arr=[5,67,87,54,43]
key=87
linear_search(arr,key)
