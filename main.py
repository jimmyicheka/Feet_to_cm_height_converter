from tkinter import*


def scale_used(value):
    cm_result_label.config(text=f"{value}")
    cm = float(value)
    feet = cm / 30.48
    feet_result_label.config(text=f"{feet}")


my_window = Tk()
my_window.title("CM_to_Feet_Height_Converter")
my_window.geometry("350x300")
my_window.config(padx=25, pady=25)


scale = Scale(from_=250, to=0, command=scale_used)
scale.grid(column=0, row=0, padx=20, pady=20)

cm_result_label = Label(text="0")
cm_result_label.grid(column=1, row=0)

cm_label = Label(text="Centimeter")
cm_label.grid(column=2, row=0, padx=10, pady=10)

feet_result_label = Label(text="0")
feet_result_label.grid(column=1, row=1)

feet_label = Label(text="Feet")
feet_label.grid(column=2, row=1, padx=10, pady=10)

my_window.mainloop()