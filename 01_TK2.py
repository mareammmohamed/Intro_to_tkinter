import tkinter as tk
from tkinter import ttk

class HelloView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.name = tk.StringVar()
        self.hello_string = tk.StringVar(value="Hello World")

        # إنشاء مكونات الواجهة
        name_label = tk.Label(self, text="Name:")
        name_entry = tk.Entry(self, textvariable=self.name)
        ch_button = ttk.Button(self, text="Change", command=self.on_change)
        hello_label = tk.Label(
            self, textvariable=self.hello_string, 
            font=("TkDefaultFont", 64), wraplength=600
        )

        # ترتيب العناصر باستخدام grid
        name_label.grid(row=0, column=0, sticky=tk.W)
        name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
        ch_button.grid(row=0, column=2, sticky=tk.E)
        hello_label.grid(row=1, column=0, columnspan=3)

        self.columnconfigure(1, weight=1)

    def on_change(self):
        if self.name.get().strip():
            self.hello_string.set(f"Hello {self.name.get()}")
        else:
            self.hello_string.set("Hello World")

class MyApplication(tk.Tk):
    """ تطبيق Tkinter لعرض رسالة ترحيب مخصصة """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Hello Tkinter")
        self.geometry("800x600")
        self.resizable(width=False, height=False)

        # إضافة الواجهة
        self.view = HelloView(self)
        self.view.grid(sticky=(tk.W, tk.E, tk.N, tk.S))

        self.columnconfigure(0, weight=1)

if __name__ == "__main__":
    app = MyApplication()
    app.mainloop()
