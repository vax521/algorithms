

def bubble_sort(arr):
    for i in range(len(arr)): # 控制排序趟数
        for j in range(0,len(arr)-i-1): # 控制每趟的比较次数
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

if __name__ == '__main__':
    array1 = [1,23,54,56,66,45]
    # print(compare_sort(array1))
    print(bubble_sort(array1))
