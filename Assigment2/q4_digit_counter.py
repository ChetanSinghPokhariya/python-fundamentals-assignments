#Write a function that counts the number of digits of a number.
def counter(n):
    if n==0:
        print("Number of digits are: 1")
        return
    count=0
    while n>0:
        n=n//10
        count+=1
    print("Number of digits are: ",count)

counter(0)
