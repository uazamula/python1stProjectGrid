n,m = map(int,input().split())
sizes = list(input().split())
tshorts=[]

for i in range(n):
    tshorts.append(list(map(int,input().split())))
wanted=[]
k = int(input())
d = {}
for i in range(len(sizes)):
    d[sizes[i]]=i

for i in range(k):
    c,s=input().split()
    wanted.append([int(c),d[s]])
sum_c=[0 for i in range(n)]
for i in range(n):
    sum_c[i]=sum(tshorts[i])
sum_s=[0 for i in range(m)]
for i in range(n):
    for j in range(m):
        sum_s[j]+=tshorts[i][j]

remain=[]
buy=[[0 for i in range(m)] for j in range(n)]
colors= {i for i in range(n)}
r=0
for i in range(k):
    if tshorts[wanted[i][0]-1][wanted[i][1]]>0:
       # print('c:',wanted[i][0]-1,' s:',wanted[i][1],' num:',tshorts[wanted[i][0]-1][wanted[i][1]],'Yes',' i:',i)
        tshorts[wanted[i][0]-1][wanted[i][1]]-=1
        sum_c[wanted[i][0]-1]-=1
        sum_s[wanted[i][1]]-=1
    else:
        t=0
        while True:
            if sum_s[wanted[i][1]+t]>0:
                is_present=False
                for j in colors:
                    if tshorts[j][wanted[i][1]+t]>0:
                        tshorts[j][wanted[i][1]+t]-=1
                        sum_c[j]-=1
                        sum_s[wanted[i][1]+t]-=1
                        is_present=True
                        if sum_c[j]<1:
                            colors.remove(j)
                        break
                if is_present:
                    break
            t+=1
            if wanted[i][1]+t==m:
                buy[wanted[i][0]-1][wanted[i][1]]+=1
                break
            if tshorts[wanted[i][0]-1][wanted[i][1]+t]>0:
                tshorts[wanted[i][0]-1][wanted[i][1]+t]-=1
                break
    # print(tshorts)
    # print(buy)
    # print('------')

for i in range(n):
    for j in range(m):
        print(tshorts[i][j], end=' ')
    print()

for i in range(n):
    for j in range(m):
        print(buy[i][j], end=' ')
    print()