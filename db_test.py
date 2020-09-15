from tkinter import *
import sqlite3
root=Tk()
root.title("project")

fID=IntVar()
Name=StringVar()

def db():
    id=fID.get()
    name=Name.get()
    x=sqlite3.connect('DATABASE.db')
    #x.execute('create table s2(id int, name text)')
    x.execute('insert into s2(id, name) values(?,?)',(id,name))
    #x.execute('DELETE FROM s2 where id=8')
    y=x.execute('select * from s2')
    for i in y:
        print(i)
        x.commit()

root.title("Project")
Label(root,text="id").grid()#row=0, padx=2, pady=2)
Label(root,text='name').grid()#row=1, padx=2, pady=2)
#Label(root, text='User Id')
Entry(root, textvar=fID).grid(row=0, column=1,columnspan=12, sticky=E,padx=2, pady=2)
Entry(root , textvar=Name).grid(row=1, column=1,columnspan=12, sticky=S, padx=2, pady=2)
Button(root,text="OK", command=db).grid(row=2, column=5, sticky=S)
root.mainloop()
