from tkinter import * 
root=Tk()
root.title('KUSHAGRA-GUI')
root.geometry('500x300')
l=Label(text='HELLO I AM A LABEL ',bg='aqua',fg='green',font='cursive 19 bold ')
l.pack(fill=X)
another_label=Label(text="this is times of india newspaper and \nthe thief that stole the money has been caught",bg='blue',fg='white',font='comicsansms 9 bold',padx=12,pady=12,borderwidth=4,relief=SUNKEN)
another_label.pack(side=LEFT,fill=Y)
root.mainloop()