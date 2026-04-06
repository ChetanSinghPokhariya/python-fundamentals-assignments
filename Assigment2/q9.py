def is_Prime(n):
    if n<=1:
        print("It is not a Prime number")
        return
    for i in range(2,n):
        if n%i==0:
            print("It is not a prime number")
            return
    print("Its a Prime number")
is_Prime(7)
is_Prime(0)
is_Prime(1)
is_Prime(11)