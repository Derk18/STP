#listbox

from tkinter import *

def submit ():
   food=[]
   for index in listbox.curselection():
      food.insert(index,listbox.get(index))
   
   print("An order for : ")
   #print(listbox.get(listbox.curselection()))
   for index in food:
      print(index)


def add():
   listbox.insert(listbox.size(),entry.get())

def delete():
   for index in reversed(listbox.curselection()):
      listbox.delete(index)
   
   #listbox.delete(listbox.curselection())
   listbox.config(height= listbox.size())

window= Tk()
window.title("ALEzia")

listbox = Listbox(window,font=('impact',35),
                  bg= 'black',fg= "yellow",
                  width=12,selectmode= MULTIPLE)
listbox.pack()
listbox.insert(1,"goat")
listbox.insert(2,"beef")
listbox.insert(3,"chicken")
listbox.config(height= listbox.size())

entry=Entry(window)
entry.pack()


submit_button =Button(window,bg="green",
                      activebackground= "green",
                      text= "enter",
                      command= submit)
submit_button.pack()

add_button = Button(window,text= "add",
                    command=add,
                    bg="green",
                    activebackground="green")
add_button.pack()
delete_button = Button(window,text= "delete",
                    command=delete,
                    bg="red",
                    activebackground="red")
delete_button.pack()




window.mainloop()