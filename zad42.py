import tkinter as tk

def click():
    print('Stisnut je botun!')




root=tk.Tk()
root.title('Botunic')
root.geometry('600x400')

button=tk.Button(root,text='Botun')
button.pack() #postavlja na prvu dostupnu poziciju

button_click=tk.Button(root, text='Klikni me!', command=click).pack(padx=10)




root.mainloop()