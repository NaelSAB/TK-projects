from tkinter import *

window = Tk()
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)
window.title("Mile To Km Converter")

def calculate():
    miles = float(entry_text.get())
    km = miles * 1.609344
    label_km_num.config(text=f"{km:.2f}")


miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

entry_text = Entry(width=10)
entry_text.grid(column=1, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_km_num = Label(text="0")
label_km_num.grid(column=1, row=1)

label_km = Label(text="km")
label_km.grid(column=2, row=1)

button_calculate = Button(text="Calculate",command=calculate)
button_calculate.grid(column=1, row=2)

window.mainloop()

