T = input()
for _j in xrange(T):
    N = input()
    a = sorted(raw_input()); poss = True
    _i = N
    for i in xrange(1,N):
        b = sorted(raw_input()); tmp = True
        for j in xrange(N): tmp *= (a[j] <= b[j])
        if tmp : a = b
        else : poss = False; _i = i+1; break
    while _i < N : raw_input();  _i += 1
    if poss : print "YES"
    else : print "NO"
    
