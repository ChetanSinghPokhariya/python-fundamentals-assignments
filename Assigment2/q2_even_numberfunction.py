# Write a function that takes two integers a and b and prints all even 
# numbers between them (inclusive).
def even_numbers():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(f"Even numbers between {a} and {b} are: ")
    for i in range(a,b+1):
        if i%2==0:
            print(i)
even_numbers()
# Note: Input is taken inside function (can be improved later)