#Write a function to return the sum of digits of a number.
def sum_of_digits(n):
    if n==0:
        print("Sum of digits is 0")
        return
    sum=0
    while n>0:
        d=n%10
        sum+=d
        n=n//10
    print("Sum of digits is ",sum)
sum_of_digits(13)