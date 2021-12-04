# Simple To-Do List App
# Topics: tkinter, grid geometry manager
# Topics: Listbox Widget, Scrollbar widget, tkinter.messagebox, Try/Except Block, pickle

from tkinter import *
import tkinter.messagebox
import pickle

#create Window
root = tkinter.Tk()
root.title('To-Do_Application By HARI_')

#functionality for add_task
def add_task():
  task = entry_tasks.get()
  if task != "":
    listbox_tasks.insert(tkinter.END,task)
    entry_tasks.delete(0,tkinter.END)
  else:
    tkinter.messagebox.showwarning(title='Warning' ,message='You Must Enter A Task.')

#functionality for delete_task
def delete_task():
  try:
    task_index = listbox_tasks.curselection()[0]
    listbox_tasks.delete(task_index)
  except:
    tkinter.messagebox.showwarning(title='Warning' ,message='You Must Select A Task.')

#functionality for Load_task rb => run_binary it write the tasks as a binary
#pickle => Pickling is used to store python objects. This means things like lists, dictionaries, class objects, and more.\
    
def load_task():
  try:
    tasks = pickle.load(open("tasks.dat","rb"))
    listbox_tasks.delete(0,tkinter.END)
    for task in tasks:
      listbox_tasks.insert(tkinter.END,task)
  except:
    tkinter.messagebox.showwarning(title='Warning' ,message="You Don't Have Any Saved File")
    
#functionality for Save_task wb => write_binary
def save_task():
  tasks = listbox_tasks.get(0,listbox_tasks.size())
  pickle.dump(tasks, open("tasks.dat","wb"))

#create seprate frame for scroll bar
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side = tkinter.RIGHT,fill = tkinter.Y)

# create GUI
listbox_tasks = tkinter.Listbox(frame_tasks,height=10,width=60)
listbox_tasks.pack(side=tkinter.LEFT)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

#create Entry boxes
entry_tasks = tkinter.Entry(root,width = 50)
entry_tasks.pack()

#create Button for Add_tasks
button_add = tkinter.Button(root,text = 'Add Tasks',width=48,bd=3,fg='white',command=add_task,bg='black')
button_add.pack()

#create Button for Delete_tasks
button_delete = tkinter.Button(root,text = 'Delete Tasks',width=48,bd=3,fg='white',command=delete_task,bg='black')
button_delete.pack()

#create Button for Load_tasks
button_load = tkinter.Button(root,text = 'Load Tasks',width=48,bd=3,fg='white',command=load_task,bg='black')
button_load.pack()

#create Button for Save_tasks
button_save = tkinter.Button(root,text = 'Save Tasks',width=48,bd=3,fg='white',command=save_task,bg='black')
button_save.pack()

root.mainloop()
