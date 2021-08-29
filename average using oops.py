class number:
    def __init__(self,average ):
        self.average = average
    def info(self):
        print(f"the average of {self.average} is {sum(self.average)/len(self.average)}")

a=number([78,67,89,90,82])  
a.info()    