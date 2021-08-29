#project-1
import random

a=random.randint(1,3)

def win(comp,human):
    if comp=='s' and human=='w':
        print("Oops-comp wins")
    elif comp=='s' and human=='g':
        print("Yeah-you win")
    elif comp=='s' and human=='s':
         print("Tie")  

    if comp=='w 'and human=='s':
        print("Yeah-you win")
    elif comp=='w' and human=='g':
        print("Oops-comp win")
    elif comp=='w' and human=='w':
         print("Tie") 

    if comp=='g' and human=='s':
        print("Oops-comp win")
    elif comp=='g' and human=='w':
        print("Yeah-you win")
    elif comp=='g' and human=='g':
         print("Tie")            
    
print("Computer has chosen its choice kindly enter yours----")
if a==1:
        comp='s'
elif a==2:
        comp ='w'
elif a==3:
        comp='g'


human=input("Enter your choice\n")

k=win(comp,human)

comp_choice=comp
print("Computer chose - " + comp_choice)