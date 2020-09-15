import random
import sqlite3
from tkinter import *

# __________________________________________________________________________________________________________________________________________________________

#Defining variables
All_options = []                    # it will store 10 random values
Arr_to_show = []
Answer_list = []                    # it will store 4 answer values out of 10 of random 
Total_score = 0
Selected_answers = []               # it will store value given by checkbutton
Option_names = []                   # it will store attempt
play=True
image_counter = 10                  # for timer in image module
option_counter=20                   # for timer in option module

# ___________________________________________________________________________________________________________________________________________________________

# random function to genarate 10 random number and store in variable list
def random_generate():
    i = 0
    while i < 10:
        random_number = random.randrange(1, 41)       # generating random number (max value 40)
        if random_number in All_options:              # this will remove duplicate number
            pass
        else:
            All_options.append(random_number)
            i=i+1

    i = 0
    
    while i < 10:
        random_number = random.randrange(0,10)        # generating random number (0 to 9)
        if random_number in Arr_to_show:              
            pass
        else:
            Arr_to_show.append(random_number)
            i=i+1
    
#____________________________________________________________________________________________________________________________________________________________

# access sqlite database to take input from database
def database():
    local = sqlite3.connect('DATABASE.db')
    for i in range(0,10):
        temp = local.execute('select * from s2 where id=?',(All_options[i],))
        for j in temp:
           Option_names.append(j[1])

#____________________________________________________________________________________________________________________________________________________________

# Function to show image on screen with timer 
def show_image():
    root=Tk()
    root.title("Project")
    root.geometry('1520x800+0+0')
    label = Label(root, fg="black", font="Verdana 35 bold")
    label.place(x=1200, y=100)

# ---------------------------------------------
    # below function is for  Timer of 10 second
    def count(): 
        global image_counter 
        # To manage the intial delay. 
        if image_counter==-1:
            image_counter=10           
            root.destroy()
        else: 
            display=str(image_counter) 
        label['text']=display
        label.after(1000, count)  
        image_counter -= 1
    count()

# ------------------------------------------------
    # below function is to exit from current  window and it will also set value of counter for next time so that it starts fron 10
    def eliminate():
        global image_counter
        image_counter=10
        root.destroy()

    c = Canvas(width = 1000, height = 630, bg='grey')
    c.place(x=100,y=30)
    image_1 = PhotoImage(file = str(Answer_list[0])+'.gif')        
    image_2 = PhotoImage(file = str(Answer_list[1])+'.gif')        
    image_3 = PhotoImage(file = str(Answer_list[2])+'.gif')        
    image_4 = PhotoImage(file = str(Answer_list[3])+'.gif')        
    c.create_image(10+65, 0+50, image = image_1, anchor = NW)
    c.create_image(440+75,0+50, image = image_2, anchor = NW)
    c.create_image(10+65,350, image = image_3, anchor = NW)
    c.create_image(440+75,350, image = image_4, anchor = NW)
    
    Button(root,text="OK", command=eliminate, padx=20, pady=3,font='Caladea 15 bold').place(x=1200,y=200 )

    root.mainloop()

#____________________________________________________________________________________________________________________________________________________________

#showing options
def show_option():
    root=Tk()
    root.title("Project")
    root.geometry('1520x800+0+0')

    label = Label(root, fg="black", font="Verdana 35 bold")
    label.place(x=1200, y=100)    

# ------------------------------------------------
    # this function is for timer of 20 second
    def count(): 
        global option_counter
        # To manage the intial delay. 
        if option_counter==-1:
            option_counter=20           
            root.destroy()
        else:   
            display=str(option_counter) 
        label['text']=display
        label.after(1000, count)  
        option_counter -= 1
    count()
# ---------------------------------------------
    # below function is to exit from current  window and it will also set value of counter for next time so that it starts fron 20
    def eliminate():
        global option_counter
        option_counter=20
        root.destroy()


#----------------------------------------------
    #function to set variable into list chosen by user
    setVar = IntVar()                   #variable for checkbuttons
    def get_value():
        if setVar.get() not in Selected_answers and len(Selected_answers)<4:
            Selected_answers.append(int(setVar.get()))
		
#--------------------------------------------
    #function to clear all selection
    def refresh():
        while Selected_answers:
            Selected_answers.pop()
        setVar.set(0)

    checkButton0 = Checkbutton(root,text = Option_names[Arr_to_show[0]],variable = setVar,onvalue = 1, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,command = get_value)
    checkButton0.grid(row=0, sticky=W) 

    checkButton1 = Checkbutton(root,text = Option_names[Arr_to_show[1]],variable = setVar,onvalue = 2, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,command = get_value)
    checkButton1.grid(row=1, sticky=W) 

    checkButton2 = Checkbutton(root,text = Option_names[Arr_to_show[2]],variable = setVar,onvalue = 3, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,command = get_value)
    checkButton2.grid(row=2, sticky=W) 

    checkButton3 = Checkbutton(root,text = Option_names[Arr_to_show[3]],variable = setVar,onvalue = 4, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,command = get_value)
    checkButton3.grid(row=3, sticky=W)

    checkButton4 = Checkbutton(root,text = Option_names[Arr_to_show[4]],variable = setVar,onvalue = 5, offvalue = 0,height = 3,width = 20,
        font='KacstOffice 25 bold',bd=5,command = get_value)
    checkButton4.grid(row=4, sticky=W)  

    checkButton5 = Checkbutton(root,text = Option_names[Arr_to_show[5]],variable = setVar,onvalue = 6, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,command = get_value)
    checkButton5.grid(row=0, column=1, sticky=W)  

    checkButton6 = Checkbutton(root,text = Option_names[Arr_to_show[6]],variable = setVar,onvalue = 7, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,command = get_value)
    checkButton6.grid(row=1, column=1, sticky=W)  
    
    checkButton7 = Checkbutton(root,text = Option_names[Arr_to_show[7]],variable = setVar,onvalue = 8, offvalue = 0,height = 3,width = 20,
        font='KacstOffice 25 bold',bd=5,command = get_value)
    checkButton7.grid(row=2, column=1, sticky=W)

    checkButton8 = Checkbutton(root,text = Option_names[Arr_to_show[8]],variable = setVar,onvalue = 9, offvalue = 0,height = 3,width = 20,
        font='KacstOffice 25 bold',bd=5,command = get_value)
    checkButton8.grid(row=3, column=1, sticky=W)

    checkButton9 = Checkbutton(root,text = Option_names[Arr_to_show[9]],variable = setVar,onvalue =10, offvalue = 0,height = 3,width = 20,
        font='KacstOffice 25 bold',bd=5,command = get_value)
    checkButton9.grid(row=4, column=1, sticky=W)

    Button(root,text = "OK", command=eliminate, padx=20, pady=3,font='Caladea 15 bold').place(x=1200,y=200)
    
    Button(root,text = "Refresh",command = refresh, padx=20, pady=3,font='Caladea 15 bold').place(x=1200, y=300)
    root.mainloop()


# ___________________________________________________________________________________________________________________________________________________________

# function to calculate the result
def check_result():
    for i in Selected_answers:
        global Total_score
        if All_options[Arr_to_show[i-1]] in Answer_list:
            Total_score+=5
        else:
            Total_score-=2
    print(Total_score)

# ___________________________________________________________________________________________________________________________________________________________

# function to clear the interface for next question
def clear_all():
    while Selected_answers:
        Selected_answers.pop()
    while All_options:
        All_options.pop()
        Option_names.pop()
        Arr_to_show.pop()


# ___________________________________________________________________________________________________________________________________________________________

# function to show the result 
def show_result():
    root=Tk()
    root.title("Project")
    root.geometry('1520x800+0+0')

# ----------------------------------------
    #function to replay game
    def replay():
        global Total_score
        global play
        Total_score=0
        play=True
        root.destroy()

    label = Label(root, text="Your Total score is :", fg="black", font="Verdana 45 bold")
    a = str(Total_score)
    b = "/100"
    label2 = Label(root, text=a+b, fg="black", font='Verdana 40 bold', )
    label.pack()
    label2.pack()
    Button(root,text = "exit", fg="black", font="Caladea 30 bold", command=root.destroy).pack()
    Label(root).pack()
    Button(root,text = "replay", fg="black", font="Caladea 30 bold",command=replay).pack()
    root.mainloop()
    
# ___________________________________________________________________________________________________________________________________________________________

# Main function starts here
while play:
    play=False
    for j in range(5):
        random_generate()
        database()
        Answer_list= All_options[0:4]
        show_image()
        show_option()
        check_result()
        clear_all()
    show_result()
