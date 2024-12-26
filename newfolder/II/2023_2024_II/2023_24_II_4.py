w = list(map(int,input().split()))
t = list(map(int,input().split()))
box1=[0,0,0,0]
box2=[0,0,0,0]

for i in range(4):
    if t[i]==1:
        box1[i]=w[i]
    else:
        box2[i]=w[i]
#print(box1,box2)
res=-1
minw=max(sum(box1),sum(box2))
for i in range(4):
    minw_prompt= max(sum(box1)-box1[i],sum(box2)+box1[i])
    if minw_prompt<minw:
        minw=minw_prompt
        res=i+1
    minw_prompt= max(sum(box2)-box2[i],sum(box1)+box2[i])
    if minw_prompt<minw:
        minw=minw_prompt
        res=i+1

print (res)