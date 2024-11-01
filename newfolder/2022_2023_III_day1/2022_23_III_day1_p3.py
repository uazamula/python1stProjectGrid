n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
vasyl=[]
petro=[]
for i in range(0,n-1):
    number = sum(arr[i])-sum(arr[i+1])
    if i%2==0:
        vasyl.append(number)
    else:
        petro.append(number)
if n%2==0:
    petro.append(arr[n-1][0])
else:
    vasyl.append(arr[n-1][0])
vasyl.sort()
petro.sort()
for i in range(len(vasyl)):
    print(vasyl[i],end=' ')
print()
for i in range(len(petro)):
    print(petro[i],end=' ')