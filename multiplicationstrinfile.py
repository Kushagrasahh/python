n = int(input("enter a no: "))

for k in range(2, n):#loop for iterating from where you want table
    list = [k*i for i in range(1, 11)]#list-comprehension
    string = '' 
    #conversion of list to string
    print(list)
    #list cannot be appended directly to string so iterate it first and concatanate
    # it with space 
    for i in range(len(list)): 
      string += str(list[i]) + ' '
      #simple writing in file
    with open("table.txt", "a") as f:
     f.write(f"Multiplication table of {k} :  ")
     f.write(string)
     f.write("\n")
