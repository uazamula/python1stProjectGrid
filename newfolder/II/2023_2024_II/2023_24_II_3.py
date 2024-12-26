d1, m1 = map(int,input().split())
d2, m2 = map(int,input().split())
if ((d1+13)-30==d2 and ((m2-m1==1)or(m1-m2==11)))or (d1+13==d2 and m1==m2):
    print ("Same birthday!")
else:
    print ("Not the same")