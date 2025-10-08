import tkinter as tk

root = tk.Tk()
root.geometry("400x400")


# function to validate mark entry
def only_numbers(char):
    return char.isdigit()


number_validation = root.register(only_numbers)

# # text box to enter marks
t2 = tk.Entry(root, validate="key", validatecommand=(number_validation, "%S"))
t2.pack()

root.mainloop()
