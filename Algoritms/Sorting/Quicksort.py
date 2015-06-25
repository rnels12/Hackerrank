def partition(ar):
    lar = len(ar)
    if lar <= 1: return ar
    p = ar[0]; 
    lpar=[];rpar=[]
    for i in range(1,lar):
        if ar[i] < p:
            lpar.append(ar[i])
        else:
            rpar.append(ar[i])
    lpar = partition(lpar)
    rpar = partition(rpar)
    ar = lpar + [p] + rpar
    print ' '.join(map(str,ar)) 
    return ar 

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)

    
