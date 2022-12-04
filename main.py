from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=200)
window.config(pady=10, padx=10)

# Entry
entry = Entry(width=10)
entry.grid(row=0, column=1)

# Label 1
label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

# Label 2
label_equal = Label(text="is Equal to")
label_equal.grid(row=1, column=0)

# Label 3
label_convert = Label(text="0")
label_convert.grid(row=1, column=1)

# Label 4
label_kilometer = Label(text="Km")
label_kilometer.grid(row=1, column=2)


# Button
def covert_miles():
    miles = int(entry.get())
    km = round(miles * 1.609, 1)
    label_convert.config(text=str(km))


button = Button(text="Calculate", command=covert_miles)
button.grid(row=2, column=1)


window.mainloop()
