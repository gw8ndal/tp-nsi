import sys, time
sys.setrecursionlimit(100000)
def pascal(n, p, mem = None):
    if mem == None :
        mem = {}
    if p == 0 or n == p:
        return 1
    else:
        if (n,p) in mem.keys():
            return mem[(n, p)]
        else:
            p1 = pascal(n-1, p-1, mem)
            p2 = pascal(n-1, p, mem)
            mem[(n, p)] = p1 + p2
            return p1 + p2

def pascal_bourrin(n, p):
    if p == 0 or n == p:
        return 1
    else:
        p1 = pascal_bourrin(n-1, p-1)
        p2 = pascal_bourrin(n-1, p)
        return p1 + p2


result = []
for i in 5,10,15,20:
    stimeb = time.process_time_ns()
    pb = pascal_bourrin(i, i//2)
    etimeb = time.process_time_ns()
    stime = time.process_time_ns()
    p = pascal(i, i//2)
    etime = time.process_time_ns()
    time_normal = etime - stime
    time_bourrin = etimeb - stimeb
    result.append((time_normal, time_bourrin, time_bourrin/time_normal))
    print(pb, p, result)
