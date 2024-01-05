L=int(input())
N=int(input())

for i in range(0,N):
    W,H=map(int, input().split())
   
    if (W<L or H<L) and (1<=W<10000 and 1<=H<10000):
        print("UPLOAD ANOTHER")
    elif W==H :
        print("ACCEPTED")
    else :
        print("CROP IT")