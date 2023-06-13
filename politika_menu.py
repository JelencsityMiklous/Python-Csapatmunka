from tkinter import*
menu=Tk()
logo=Canvas(menu,width=600,height=100, bg='grey')
kep=PhotoImage(file='a_jologo-removebg-preview.png')
item=logo.create_image(80,80,image=kep)
logo.grid()
menu.mainloop()
