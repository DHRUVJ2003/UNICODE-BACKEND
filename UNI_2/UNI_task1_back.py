def adj(a,b):
    soln={}
    for i in range(a,b):
        q=int(i)
        r2=0
        r1=0       
        if (q==0):
            soln.update({i:'False'})
        while(q!=0):
            r1=int(q%2)
            q=int(q/2)
            if ((r1+r2)==2):
                soln.update({i:'True'})
                break
            if (q!=0):
                r2=r1
        if (r1!=r2):
            soln.update({i:'False'})
    return(dict(soln.items()))