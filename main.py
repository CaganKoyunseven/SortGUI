from tkinter import *
from elements import *
window = Tk()
WIDHT = 500
HEIGHT = 500
canvas = Canvas(window,width=WIDHT,height=HEIGHT,bg="white")
canvas.pack()


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1

asfmiafs

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]



def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Main driver code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    i=0
    vector=10
    endvector=20;
    while i < n:
        element1 = element(canvas, HEIGHT,vector ,endvector, arr[i]*10, "Red")
        vector=endvector
        endvector=endvector+10
        i=i+1
    quickSort(arr, 0, n - 1)
    for val in arr:
        print(val, end=" ")



window.mainloop()