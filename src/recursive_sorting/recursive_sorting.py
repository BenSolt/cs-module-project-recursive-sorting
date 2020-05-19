# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    for i in range(len(merged_arr)):

        #if length of array A and B is greater than 0
        if len(arrA) > 0 and len(arrB) > 0:
            # array A at index 0 is less than array B at index 0
            if arrA[0] < arrB[0]:
                merged_arr[i] = arrA[0]
                arrA.remove(arrA[0])
            else:
                merged_arr[i] = arrB[0]
                arrB.remove(arrB[0])
        else:
            if len(arrA) == 0:
                


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here


    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
