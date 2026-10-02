n = int(input())
somaN = 0

somaNs = sum(map(int, input().split()))

for i in range(n + 1):
    somaN+=i
    
print(somaN - somaNs)