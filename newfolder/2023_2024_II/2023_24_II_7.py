n = int(input())
arr=[]
for i in range(n):
    id, gender, grade, age, score = input().split()
    arr.append([int(id), 0 if gender=='female' else 1, int(grade), int(age), int(score)])
m= int(input())
olimps=[]
for i in range(m):
    olimps.append(input())
arr.sort(key=lambda x: -x[4])
participants = {}
if 'IOI' in olimps:
    i=0
    aIOI=[]
    while True:
        aIOI.append(arr[i][0])
        i+=1
        if i==n or i==4:
            break
    participants['IOI']=aIOI

if 'CEOI' in olimps:
    i=0
    aCEOI=[]
    while True:
        aCEOI.append(arr[i][0])
        i+=1
        if i==n or i==4:
            break
    participants['CEOI']=aCEOI

if 'EGOI' in olimps:
    i=0
    aEGOI=[]
    k=0
    while True:
        if arr[i][1]==0:
            aEGOI.append(arr[i][0])
            k+=1
        i+=1
        if i==n or k==4:
            break
    participants['EGOI']=aEGOI

if 'EJOI' in olimps:
    i=0
    k=0

    aEJOI=[]
    while True:
        if arr[i][3]<=15:
            aEJOI.append(arr[i][0])
            k+=1
        i+=1
        if i==n or k==4:
            break
    participants['EJOI']=aEJOI

if 'BaltOI' in olimps:
    i=0
    aBaltOI=[]
    while True:
        aBaltOI.append(arr[i][0])
        i+=1
        if i==n or i==6:
            break
    participants['BaltOI']=aBaltOI

if 'BalkOI' in olimps:
    i=0
    k=0
    aBalkOI=[]
    while True:
        if arr[i][2]!=11:
            aBalkOI.append(arr[i][0])
            k+=1
        i+=1
        if i==n or k==4:
            break
    participants['BalkOI']=aBalkOI

if 'JBOI' in olimps:
    i=0
    k=0
    aJBOI=[]
    while True:
        if arr[i][2]!=10 and arr[i][2]!=11:
            aJBOI.append(arr[i][0])
            k+=1
        i+=1
        if i==n or k==4:
            break
    participants['JBOI']=aJBOI

for i in range(len(olimps)):
    participants[olimps[i]].sort()
    print(olimps[i])
    for j in range(len(participants[olimps[i]])):
        print(participants[olimps[i]][j])
    print()
# print (n, arr, m, olimps )
# print(participants)