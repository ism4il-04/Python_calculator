import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Python Calculator")

# Create display
display = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 18))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Run the app
root.mainloop()
