# Write a function that prints the digits of a number.
def digit(n):
    while n>0:
        d=n%10
        print(d)
        n=n//10
digit(143)