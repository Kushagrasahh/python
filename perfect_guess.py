#PROJECT-2
import random
n = random.randint(1, 100)
print(n)
numberSn = None
guess=0
while (numberSn != n):
    numberSn = int(input("Enter A Number: "))
    guess+=1
    if (numberSn == n):
        print("Awesome! Right Answer")
    else:
        if (numberSn > n):
            print("Oops! Enter a Smaller Number: ")
        else:
            print("Oops! Enter a Greater Number: ")
with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(guess<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guess))

  