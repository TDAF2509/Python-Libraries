def power(x,k):
    print("power being run with",x,k)
    if k==0:
        print("k=0:",x,k)
        return 1
    y = power(x,k//2)
    print("y=",y)
    print("unwound power run with",x,k)
    if k%2==0:
        print("k is even:",x,k)
        return y*y
    else:
        print("else:",x,k)
        return y*y*x

def main():
    print(power(2,12))

main()
