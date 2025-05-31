import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.current = ""
        
        self.display = ttk.Entry(root, justify="right", font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', '(', ')'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(root, text=button, command=cmd).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
    
    def click(self, key):
        if key == '=':
            try:
                result = eval(self.current)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.current = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.current = ""
        elif key == 'C':
            self.current = ""
            self.display.delete(0, tk.END)
        elif key == '√':
            try:
                result = math.sqrt(float(self.current))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.current = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.current = ""
        else:
            self.current += key
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop() 