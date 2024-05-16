import tkinter
from tkinter import *
from tkinter import messagebox
def calculate_interest():
  try:
    P = float(principal_entry.get())
    r = float(rate_entry.get()) / 100
    t = float(time_entry.get())
    n = 12
    A = P * (1 + r/n)**(n*t)
    result.insert(0,str(A))
  except:
    messagebox.showerror("error","please input correct data")
    clear_fields()
def clear_fields():
  principal_entry.delete(0, END)
  rate_entry.delete(0,END)
  time_entry.delete(0, END)
  result.delete(0,END)
root = Tk()
root.title("Compound Interest Calculator")
principal_label = Label(root, text="Principal amount:")
principal_label.grid(row=0, column=0, padx=10, pady=5)
principal_entry = Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=5)
rate_label = Label(root, text="Rate of interest (%):")
rate_label.grid(row=1, column=0, padx=10, pady=5)
rate_entry = Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=5)
time_label = Label(root, text="Number of years:")
time_label.grid(row=2, column=0, padx=10, pady=5)
time_entry = Entry(root)
time_entry.grid(row=2, column=1, padx=10, pady=5)
submit_button = Button(root, text="Submit", command=calculate_interest)
submit_button.grid(row=3, column=0, padx=10, pady=5)
clear_button =Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=3, column=1, padx=10, pady=5)
result_label=Label(root,text="Compound Interest")
result_label.grid(row=4, column=0, padx=10, pady=5)
result= Entry(root)
result.grid(row=4, column=1, columnspan=2, padx=20, pady=5)
root.mainloop() 