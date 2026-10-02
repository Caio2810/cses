import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
    
mov = 0
    
for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
        dif = arr[i - 1] - arr[i]
        mov+=dif
        arr[i] = arr[i - 1]
    
print(mov)