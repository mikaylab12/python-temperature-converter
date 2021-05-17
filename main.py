# importing tkinter
from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.geometry("600x600")
root.config(bg="lightgray")

# celsius label and entry
celsius_frame = Frame(root, width=220, height=150, background="gray")
celsius_frame.place(x=10, y=10)
celsius_label = Label(celsius_frame, text="Celsius to Fahrenheit")
celsius_label.place(x=20, y=20)
celsius_entry = Entry(celsius_frame, state="readonly")
celsius_entry.place(x=20, y=120)
# celsius_entry = Entry(celsius_frame, state="readonly")
# celsius_entry.place(x=20, y=120)

# fahrenheit label and entry
fahrenheit_frame = Frame(root, width=220, height=150, background="gray")
fahrenheit_frame.place(x=350, y=10)
fahrenheit_label = Label(fahrenheit_frame, text="Fahrenheit to Celsius")
fahrenheit_label.place(x=20, y=20)
fahrenheit_entry = Entry(fahrenheit_frame, state="readonly")
fahrenheit_entry.place(x=20, y=120)

# label where result will be shown in
convert_label = Label(root, background="pink", width=15)
convert_label.place(x=230, y=290)


# activate celsius frame
def activate_celsius():
    celsius_entry.config(state="normal")
    fahrenheit_entry.config(state="readonly")
    celsius_frame.config(bg="pink")
    fahrenheit_frame.config(bg="gray")


# activate fahrenheit frame
# it will highlight the fahrenheit frame and allow for an entry to be made only in that frame.
def activate_fahrenheit():
    fahrenheit_entry.config(state="normal")
    celsius_entry.config(state="readonly")
    fahrenheit_frame.config(bg="pink")
    celsius_frame.config(bg="gray")


# function to convert
def convert_temp():
    if celsius_entry.get() == "":
        fahrenheit = float(fahrenheit_entry.get())
        converting_fahrenheit = ((fahrenheit - 32) * 5 / 9)
        convert_label.config(text=converting_fahrenheit)
    elif fahrenheit_entry.get() == "":
        celsius = float(celsius_entry.get())
        converting_celsius = (celsius * 9 / 5 + 32)
        convert_label.config(text=converting_celsius)


# function for clearing numbers
def clear_numbers():
    celsius_entry.delete(0, END)
    fahrenheit_entry.delete(0, END)
    convert_label.config(text="")

# exit program
def exit_program():
    return root.destroy()


# activate degrees C to degrees F
activate_c_to_f = Button(root, text="Activate Celsius to Fahrenheit", command=activate_celsius)
activate_c_to_f.place(x=10, y=180)
# activate degrees F to degrees C
activate_f_to_c = Button(root, text="Activate Fahrenheit to Celsius", command=activate_fahrenheit)
activate_f_to_c.place(x=350, y=180)
# convert button
covert_button = Button(root, text="Calculate conversion", command=convert_temp)
covert_button.place(x=210, y=250)
# clear button and function
clear_button = Button(root, text="Clear", command=clear_numbers)
clear_button.place(x=165, y=330)
# exit button
exit_button = Button(root, text="Exit", command=exit_program)
exit_button.place(x=350, y=330)

root.mainloop()
