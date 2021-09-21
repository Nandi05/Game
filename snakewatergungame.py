import random
def game(a,b):
    if a==b:
        return None
    
    if a=='s':
        if b=='w':
            return False
        elif b=='g':
            return True
    if a=='w':
        if b=='s':
            return True
        elif b=='g':
            return False
    if a=='g':
        if b=='w':
            return True
        elif b=='s':
            return False

print("comp turn: snake(s),water(w) or gun(g): ")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
else:
    comp='g'
you=input("player 2 turn: snake(s) water(w) or gun(g): ")
print("computer chose:",comp)
print("you chose:",you)
j=game(comp,you)
if j==True:
    print("you win!")
elif  j== None:
    print("this is a tie")

else:
    print("you lose!")

