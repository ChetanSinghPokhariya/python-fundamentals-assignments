secret=69
while True:
    n=int(input("Guess the number: "))
    if n==secret:
        print("Correct you Win!")
        break
    elif n>secret:
        print("High! try again")
    elif n<secret:
        print("Low! try again")
        
