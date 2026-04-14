import matplotlib.pyplot
import time
import random

def binary_search(arr ,st,end, target):
    mid = st + (end-st)//2
    if(arr[mid] < target):
        binary_search(arr , mid+1 , end , target)
    elif(arr[mid] > target):
        binary_search(arr , st, mid -1 , target)
    elif(arr[mid] == target):
        return
    return