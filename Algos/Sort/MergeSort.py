def merge(array, temp_array, low, mid, high):
    pass



def Sort(array, temp_array, low, high):
    if low < high:
        mid = (low + high)//2
        Sort(array, temp_array, low, mid)
        Sort(array, temp_array, mid+1, high)
        merge(array, temp_array, low, mid, high)



