from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=200)
window.config(pady=10, padx=10)

# Entry
entry = Entry(width=10)
entry.grid(row=0, column=1)

# Label 1
label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

# Label 2
label_2 = Label(text="is Equal to")
label_2.grid(row=1, column=0)

# Label 3
label_3 = Label(text="0")
label_3.grid(row=1, column=1)

# Label 4
label_4 = Label(text="Km")
label_4.grid(row=1, column=2)


# Button
def covert_miles():
    miles = int(entry.get())
    km = round(miles * 1.609, 1)
    label_3.config(text=str(km))


button = Button(text="Calculate", command=covert_miles)
button.grid(row=2, column=1)


window.mainloop()
