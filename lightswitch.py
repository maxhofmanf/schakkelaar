from cProfile import label
import tkinter as tk
window = tk.Tk()

# schijf hier tussen je code
window["bg"] = "black"
onoff = True
def Click():
    global onoff,buttonStat
    if onoff == True:
        print("lightswitch = on")
        onoff =False
        myWindow = window.config(bg ="yellow")
        button.config(text = "lightswitch: on")

    elif onoff == False:
        print("lightswitch = off")
        onoff = True
        myWindow = window.config(bg = "black")
        button.config(text= "lightswitch: off")

   

button = tk.Button(text='light switch: off' ,bg="white", fg="black", padx = 50 , pady = 50, command= Click)
button.pack(pady = 240, padx = 426)


# schijf hier tussen je code

window.mainloop()