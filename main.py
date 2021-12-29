for n in range(10,200):
    sum=0
    for i in str(n):
        k=int(i)**len(str(n))
        sum+=k
    if int(n)==sum:
        print(n)