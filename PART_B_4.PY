import tkinter as tk
def button_click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(num))
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def clear():
    entry.delete(0, tk.END)
window = tk.Tk()
window.title("Simple Calculator")
entry = tk.Entry(window, width=25, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
for i in range(0, 10):
    button = tk.Button(window, text=str(i), width=6, command=lambda num=i: button_click(num))
    if (i % 3 == 0):
        if i == 0:
            button.grid(row=4, column=2, padx=3, pady=5)
        else:
            button.grid(row=(i - 1) // 3 + 1, column=(i - 4) % 3, padx=3, pady=5)
    else:
        button.grid(row=(i - 1) // 3 + 1, column=(i - 4) % 3, padx=3, pady=5)
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, width=6, command=lambda op=operator: button_click(op))
    button.grid(row=i + 1, column=4, padx=5, pady=5)
equal_button = tk.Button(window, text='=', width=6, command=calculate)
equal_button.grid(row=4, column=0, padx=4, pady=4)
clear_button = tk.Button(window, text='C', width=6, command=clear)
clear_button.grid(row=4, column=1, padx=5, pady=5)
window.mainloop()