sum=0
while(True):
    n = input("enter the prices: \n")
    if (n!='q'):
        sum +=  int(n)
        print(f"total so far...   {sum}")
    else:
        print(f"TOTAL AMOUNT = {sum}")
        break   


'''sum = 0
while (True):
	userInput = input("Enter the item price or press q to quit: ")
	if (userInput!='q'):
		sum = sum + int(userInput)
		print(f"Order total so far: {sum}")
	else:
		print(f"Your Bill total is {sum}. Thanks for shopping with us")
		break'''