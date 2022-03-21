def selectionSort(array):
    for i in range(len(array)-1):
        print(array)
        minimum_index = i
        min_value = array[i]
        for j in range(i+1,len(array)):
            
            if min_value > array[j]:
                
                min_value = array[j]
                minimum_index = j
                print(min_value)
        if minimum_index != i :
            array[minimum_index], array[i] = array[i], array[minimum_index]
    return array


print(selectionSort([5,9,3,10,45,2,0]))
