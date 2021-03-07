import sys
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import _support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    _support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
        Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    _support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
            top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("479x567+383+102")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1,  1)
        top.title("Phonebook")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.042, rely=0.035, height=31, width=109)
        self.Label1.configure(text='''Enter name:''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.271, rely=0.035, height=33, relwidth=0.388)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.042, rely=0.159, height=21, width=99)
        self.Label2.configure(text='''Enter number:''')

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.271, rely=0.159, height=23, relwidth=0.388)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.042, rely=0.265, height=38, width=103)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''search''')

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.292, rely=0.265, height=38, width=93)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Add''')

        self.TButton3 = ttk.Button(top)
        self.TButton3.place(relx=0.522, rely=0.265, height=38, width=103)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Edit Name''')

        self.TButton4 = ttk.Button(top)
        self.TButton4.place(relx=0.772, rely=0.265, height=38, width=93)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Edit Number''')

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.021, rely=0.476, height=279, width=452)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Tlabel''')

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.063, rely=0.37, height=19, width=92)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''display:''')
if __name__ == '__main__':
    vp_start_gui()

