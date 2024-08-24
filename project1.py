import random 

n = random.randint(1,100)
a=-1
guesses=1

while(a!=n):
    a=int(input("Guess the number: "))
    if(a<n):
        print("guess a higher number: ")
        guesses+=1

    elif(a>n):
        print("guess a lower number please")
        guesses+=1

print(f"correct guess of {n} after {guesses} attempts!")            