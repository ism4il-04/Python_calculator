import tkinter as tk

#l'expression
e=""
# Create main window
root = tk.Tk()
root.title("Python Calculator")

# les fonctions
def click(button):
    global e
    e += str(button)
    display.set(e)

def clear():
    global e
    e = ""
    display.set("")

def calc():
    global e
    e = str(eval(e))

    display.set(e)

def on_keypress(event):
    char = event.char
    if char in '0123456789+-*/.=()':
        click(char)
    elif event.keysym == 'Return':
        calc()
    elif event.keysym == 'BackSpace':
        supprimer()

def supprimer():
    global e
    e = e[0:len(e)-1]
    display.set(e)

# Create display
display = tk.StringVar()
entry = tk.Entry(root, width=20, borderwidth=5, font=('Arial', 18), textvariable=display)
entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
root.bind("<Key>", on_keypress)
# Number buttons
btnc = tk.Button(root, text='C', fg='black', bg='white', height=2, width=10 , command=lambda:clear())
btnc.grid(row=0, column=3, padx=5, pady=5)
btndel = tk.Button(root, text='s', fg='black', bg='white', height=2, width=10 , command=lambda:supprimer())
btndel.grid(row=0, column=2, padx=5, pady=5)
btn7 = tk.Button(root, text='7', fg='black', bg='white', height=2, width=10, command=lambda:click(str(7)))
btn7.grid(row=1, column=0, padx=5, pady=5)
btn8 = tk.Button(root, text='8', fg='black', bg='white', height=2, width=10, command=lambda:click('8'))
btn8.grid(row=1, column=1, padx=5, pady=5)
btn9 = tk.Button(root, text='9', fg='black', bg='white', height=2, width=10, command=lambda:click('9'))
btn9.grid(row=1, column=2, padx=5, pady=5)
btnplus = tk.Button(root, text='+', fg='black', bg='white', height=2, width=10, command=lambda:click('+'))
btnplus.grid(row=1, column=3, padx=5, pady=5)
btn4 = tk.Button(root, text='4', fg='black', bg='white', height=2, width=10 , command=lambda:click('4'))
btn4.grid(row=2, column=0, padx=5, pady=5)
btn5 = tk.Button(root, text='5', fg='black', bg='white', height=2, width=10, command=lambda:click('5'))
btn5.grid(row=2, column=1, padx=5, pady=5)
btn6 = tk.Button(root, text='6', fg='black', bg='white', height=2, width=10, command=lambda:click('6'))
btn6.grid(row=2, column=2, padx=5, pady=5)
btnm = tk.Button(root, text='-', fg='black', bg='white', height=2, width=10, command=lambda:click('-'))
btnm.grid(row=2, column=3, padx=5, pady=5)
btn1= tk.Button(root, text='1', fg='black', bg='white', height=2, width=10 , command=lambda:click('1'))
btn1.grid(row=3, column=0, padx=5, pady=5)
btn2 = tk.Button(root, text='2', fg='black', bg='white', height=2, width=10, command=lambda:click('2'))
btn2.grid(row=3, column=1, padx=5, pady=5)
btn3 = tk.Button(root, text='3', fg='black', bg='white', height=2, width=10, command=lambda:click('3'))
btn3.grid(row=3, column=2, padx=5, pady=5)
btnf = tk.Button(root, text='x', fg='black', bg='white', height=2, width=10, command=lambda:click('*'))
btnf.grid(row=3, column=3, padx=5, pady=5)
btn0 = tk.Button(root, text='0', fg='black', bg='white', height=2, width=10, command=lambda:click('0'))
btn0.grid(row=4, column=0, padx=5, pady=5)
btnd = tk.Button(root, text='.', fg='black', bg='white', height=2, width=10, command=lambda:click('.'))
btnd.grid(row=4, column=1, padx=5, pady=5)
btnd = tk.Button(root, text='/', fg='black', bg='white', height=2, width=10, command=lambda:click('/'))
btnd.grid(row=4, column=2, padx=5, pady=5)
btne = tk.Button(root, text='=', fg='black', bg='white', height=2, width=10, command=lambda:calc())
btne.grid(row=4, column=3, padx=5, pady=5)

# Run the app
root.mainloop()
