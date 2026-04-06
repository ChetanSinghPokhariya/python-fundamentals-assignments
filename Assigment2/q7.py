while(True):
    n=input("Enter the number: ")
    if (n=="quit"):
        break
    n=int(n)
    if n>0:
        print("Its a positive number")
    elif n<0:
        print("Its a negative number")  
    else:
        print("Its a zero")  
        