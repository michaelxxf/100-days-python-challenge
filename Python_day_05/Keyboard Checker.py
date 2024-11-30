import tkinter as tk

def on_key_press(event):
    label.config(text=f"Key Pressed: {event.keysym}")

root = tk.Tk()
root.title("Keyboard Button Checker")
root.geometry("300x200")

label = tk.Label(root, text="Press any key", font=("Helvetica", 16))
label.pack(expand=True)

root.bind("<KeyPress>", on_key_press)

root.mainloop()