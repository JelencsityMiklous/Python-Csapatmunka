from tkinter import*
menu=Tk()
logo=Canvas(menu,width=300,height=100, bg='white')
kep=PhotoImage(file='a_jologo-removebg-preview.png')
item=logo.create_image(80,80,image=kep)
menu.mainloop()
