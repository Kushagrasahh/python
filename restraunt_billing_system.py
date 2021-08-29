# PROJECT-3
print("\n****WELCOME TO CHAT-BAZAR****\n")
print("PLEASE SELECT YOUR ORDER: ")
print("PANEER: 250/PLATE")
print("CHICKEN: 500/PLATE")
print("PANEER-TIKKA: 300/PLATE")
print("BHOJAN-THAL: 200/PLATE")
print("MANCHURIAN: 150/PLATE")
print("CHOWMEIN: 50/PLATE")
print("After Ordering The Food Please Enter (EXIT) And Quantity (0) To Confirm Your Order!\n")
dict = {'PANEER': 250, 'CHICKEN': 500, 'PANEER-TIKKA': 300,
        'BHOJAN-THAL': 200, 'MANCHURIAN': 150, 'CHOWMEIN': 50}
list = list(dict.keys())
sum = 0
cNt = 0
while True:
    odr = input("Enter Your Order Please: \n")
    quantityS = int(input("Enter Qnantity: "))
    cNt += 1
    if odr == 'EXIT':
        break
    elif odr in list:
        k = dict[odr]*quantityS
        sum += k
        print(f'The Total Of {odr} With Quantity {quantityS} is: {str(k)}')
    else:
        print("OOPS! Please Enter The Items Given In The Menu: ")
        print("This Item Entered Above Will Not Count In Your Bill!THANKS ")

print("Thanks For Ordering The Food!")
print("Your Bill Total is ", sum)
if cNt > 5:
      sum = (1/5)*sum  # 20%profit
      print('CONGRULATIONS!  YOU ORDERED MORE THAN 5 ITEMS SO YOUR DISCOUNTED BILL AMOUNT IS:', sum)
