import tkinter as tk

class Applicatoin(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root,
            width=420, height=320,
            borderwidth=4, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()
    
    def create_widgets(self):
        # Close button
        quit_btn = tk.Button(self)
        quit_btn['text'] = 'Close'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')
        
        # Text box
        self.text_box = tk.Entry(self)
        self.text_box['width'] = 10
        self.text_box.pack()
        
        # Execute button
        submit_btn = tk.Button(self)
        submit_btn['text'] = 'Execute'
        submit_btn['command'] = self.input_handler
        submit_btn.pack()
        
        # output message
        self.message = tk.Message(self)
        self.message.pack()
    
    def input_handler(self):
        text = self.text_box.get()
        self.message['text'] = text + '!!'

root = tk.Tk()
root.title("Sample App")
root.geometry('400x300')
app = Applicatoin(root=root)


app.mainloop()
