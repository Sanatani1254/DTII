import tkinter as tk
import math
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x520")
root.resizable(False,False)

entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=5, relief="ridge")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

def insert(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def backspace():
    text = entry.get()
    if len(text) > 0:
        entry.delete(len(text)-1, tk.END)

def solve(eq):
    return eval(eq)

def calculate():
    try:
        eq = entry.get()
        r = solve(eq)
        clear()
        entry.insert(0, r)
    except:
        clear()
        entry.insert(0, "Enter a valid equation")

def on_square_root():
    try:
        result = math.sqrt(float(entry.get()))
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

def on_square():
    try:
        num = float(entry.get())
        result = num ** 2
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

def on_sin():
    try:
        result = math.sin(math.radians(float(entry.get())))
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

def on_cos():
    try:
        result = math.cos(math.radians(float(entry.get())))
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

def on_tan():
    try:
        result = math.tan(math.radians(float(entry.get())))
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

def on_log():
    try:
        result = math.log10(float(entry.get()))
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

def on_ln():
    try:
        result = math.log(float(entry.get()))
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

button_frame = tk.Frame(root)
button_frame.pack(fill="both", expand=True, padx=10, pady=10)


tk.Button(button_frame, text="√", font=("Arial", 14), width=5, command=on_square_root).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="x²", font=("Arial", 14), width=5, command=on_square).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="sin", font=("Arial", 14), width=5, command=on_sin).grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="cos", font=("Arial", 14), width=5, command=on_cos).grid(row=0, column=3, padx=5, pady=5)


tk.Button(button_frame, text="tan", font=("Arial", 14), width=5, command=on_tan).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="log", font=("Arial", 14), width=5, command=on_log).grid(row=1, column=1, padx=5, pady=5)
tk.Button(button_frame, text="ln", font=("Arial", 14), width=5, command=on_ln).grid(row=1, column=2, padx=5, pady=5)
tk.Button(button_frame, text="π", font=("Arial", 14), width=5, command=lambda: insert(str(math.pi))).grid(row=1, column=3, padx=5, pady=5)


tk.Button(button_frame, text="7", font=("Arial", 14), width=5, command=lambda: insert("7")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(button_frame, text="8", font=("Arial", 14), width=5, command=lambda: insert("8")).grid(row=2, column=1, padx=5, pady=5)
tk.Button(button_frame, text="9", font=("Arial", 14), width=5, command=lambda: insert("9")).grid(row=2, column=2, padx=5, pady=5)
tk.Button(button_frame, text="÷", font=("Arial", 14), width=5, command=lambda: insert("/")).grid(row=2, column=3, padx=5, pady=5)


tk.Button(button_frame, text="4", font=("Arial", 14), width=5, command=lambda: insert("4")).grid(row=3, column=0, padx=5, pady=5)
tk.Button(button_frame, text="5", font=("Arial", 14), width=5, command=lambda: insert("5")).grid(row=3, column=1, padx=5, pady=5)
tk.Button(button_frame, text="6", font=("Arial", 14), width=5, command=lambda: insert("6")).grid(row=3, column=2, padx=5, pady=5)
tk.Button(button_frame, text="×", font=("Arial", 14), width=5, command=lambda: insert("*")).grid(row=3, column=3, padx=5, pady=5)


tk.Button(button_frame, text="1", font=("Arial", 14), width=5, command=lambda: insert("1")).grid(row=4, column=0, padx=5, pady=5)
tk.Button(button_frame, text="2", font=("Arial", 14), width=5, command=lambda: insert("2")).grid(row=4, column=1, padx=5, pady=5)
tk.Button(button_frame, text="3", font=("Arial", 14), width=5, command=lambda: insert("3")).grid(row=4, column=2, padx=5, pady=5)
tk.Button(button_frame, text="-", font=("Arial", 14), width=5, command=lambda: insert("-")).grid(row=4, column=3, padx=5, pady=5)


tk.Button(button_frame, text="0", font=("Arial", 14), width=5, command=lambda: insert("0")).grid(row=5, column=0, padx=5, pady=5)
tk.Button(button_frame, text=".", font=("Arial", 14), width=5, command=lambda: insert(".")).grid(row=5, column=1, padx=5, pady=5)
tk.Button(button_frame, text="=", font=("Arial", 14), width=5, command=calculate, bg="green", fg="white").grid(row=5, column=2, padx=5, pady=5)
tk.Button(button_frame, text="+", font=("Arial", 14), width=5, command=lambda: insert("+")).grid(row=5, column=3, padx=5, pady=5)


tk.Button(button_frame, text="C", font=("Arial", 14), width=10, command=clear, bg="red", fg="white").grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
tk.Button(button_frame, text="Back", font=("Arial", 14), width=10, command=backspace, bg="orange").grid(row=6, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

root.mainloop()
