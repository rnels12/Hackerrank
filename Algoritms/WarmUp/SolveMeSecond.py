def solveMeSecond(a,b):
       return a+b
   
#main   
n = int(raw_input())  
for i in range(0,n):
    a, b = raw_input().split()
    res = solveMeSecond(int(a),int(b))
    print res
