from tkinter import *
from tkinter import ttk

from src.controller.mainfiles import \
    main_Act_Deact_sync, \
    main_Act_Deact, main_Activate, \
    main_Activate_sync, main_Deactivate
from src.utils.utils import Utils as u


def ultra_mode():
    return MyApplication.run_gui()


def normal_mode():
    return MyApplication_sync.run_gui()


# start my app
class StartMyApp:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.title('JN CRM Solutions')
        self.root.configure(background="silver")
        self.create_widgets()

    def create_widgets(self):
        header = ttk.Frame(self.root, padding="1 1 1 1")
        header.grid(column=0, row=0, sticky=(N, W, E, S))
        header.columnconfigure(2, weight=1)
        header.rowconfigure(1, weight=1)

        control = ttk.Frame(self.root, padding="3 3 12 12")
        control.grid(column=0, row=1, sticky=(N, W, E, S))
        control.columnconfigure(2, weight=1)
        control.rowconfigure(8, weight=1)

        footer = ttk.Frame(self.root, padding="1 1 1 1")
        footer.grid(column=0, row=2, sticky=(N, W, E, S))
        footer.columnconfigure(2, weight=1)
        footer.rowconfigure(1, weight=1)

        options = {'padx': 1, 'pady': 1}

        title = Label(header, text="JN CRM Solutions", bg='black', fg='white')
        title.pack(fill=X)

        # ___________________labels__________________

        lb1 = Label(control, text="CRM LISTS", fg='red',
                    bg='white', font=("Arial", 10))
        # lb1.place(x=40, y=170)
        lb1.grid(column=0, row=1, **options)

        # ___________________Buttons__________________

        # lists
        ultrabtn = Button(control, text="Ultra Fast Mode",
                          justify='center', width=20, height=2, command=ultra_mode)
        # ActivatorBtn.place(x=20, y=220)
        ultrabtn.grid(column=0, row=2, **options)

        normalbtn = Button(control, text="Normal Mode",
                           justify='center', width=20, height=2, command=normal_mode)
        # Act_Deact.place(x=20, y=270)
        normalbtn.grid(column=0, row=3, **options)

        # _____________________Footer_______________________
        footer = Label(footer, text="Developed by Dr. Joseph Nady",
                       fg='black', bg="silver", font=("Arial", 7))
        # footer.place(x=150, y=480)
        footer.pack(fill=X)

        # footer.grid(column=0,row=0,columnspan=2)

        def exit_application(self):
            # Perform any cleanup or additional actions before exiting
            print("Exiting application.")
            self.root.quit()

    @classmethod
    def run_start_gui(cls):
        root = Tk()
        app = cls(root)
        root.mainloop()


class MyApplication:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.title('JN CRM Solutions')
        self.root.configure(background="silver")
        self.create_widgets()
        cores = int(u.cpu_count())
        self.usedcores = cores / 2

    def activate(self):
        self.root.quit()
        return main_Activate(self.usedcores)

    def deactivate(self):
        self.root.quit()
        return main_Deactivate()

    def both(self):
        self.root.quit()
        return main_Act_Deact(self.usedcores)

    def create_widgets(self):
        header = ttk.Frame(self.root, padding="1 1 1 1")
        header.grid(column=0, row=0, sticky=(N, W, E, S))
        header.columnconfigure(2, weight=1)
        header.rowconfigure(1, weight=1)

        control = ttk.Frame(self.root, padding="3 3 12 12")
        control.grid(column=0, row=1, sticky=(N, W, E, S))
        control.columnconfigure(2, weight=1)
        control.rowconfigure(8, weight=1)

        footer = ttk.Frame(self.root, padding="1 1 1 1")
        footer.grid(column=0, row=2, sticky=(N, W, E, S))
        footer.columnconfigure(2, weight=1)
        footer.rowconfigure(1, weight=1)

        options = {'padx': 1, 'pady': 1}

        title = Label(header, text="JN CRM Solutions Ultra", bg='black', fg='white')
        title.pack(fill=X)

        # ___________________labels__________________

        lb1 = Label(control, text="CRM LISTS", fg='red',
                    bg='white', font=("Arial", 10))
        # lb1.place(x=40, y=170)
        lb1.grid(column=0, row=1, **options)

        # ___________________Entry__________________

        # ___________________Buttons__________________

        # lists
        ActivatorBtn = Button(control, text="Accounts Activator",
                              justify='center', width=20, height=2, command=self.activate)
        # ActivatorBtn.place(x=20, y=220)
        ActivatorBtn.grid(column=0, row=2, **options)

        Act_Deact = Button(control, text="Accounts Activation \nand Deactiation",
                           justify='center', width=20, height=2, command=self.both)
        # Act_Deact.place(x=20, y=270)
        Act_Deact.grid(column=0, row=3, **options)

        DeactivatorBtn = Button(control, text="Accounts De-activator",
                                justify='center', width=20, height=2, command=self.deactivate)
        # DeactivatorBtn.place(x=20, y=320)
        DeactivatorBtn.grid(column=0, row=4, **options)

        # _____________________Footer_______________________
        footer = Label(footer, text="Developed by Dr. Joseph Nady",
                       fg='black', bg="silver", font=("Arial", 7))
        # footer.place(x=150, y=480)
        footer.pack(fill=X)

        # footer.grid(column=0,row=0,columnspan=2)

        def exit_application(self):
            # Perform any cleanup or additional actions before exiting
            print("Exiting application.")
            self.root.quit()

    @DeprecationWarning
    @classmethod
    def run_gui(cls):
        root = Tk()
        app = cls(root)
        root.mainloop()


class MyApplication_sync:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.title('JN CRM Solutions')
        self.root.configure(background="silver")
        self.create_widgets()

    def activate(self):
        self.root.quit()
        return main_Activate_sync()

    def deactivate(self):
        self.root.quit()
        return main_Deactivate()

    def both(self):
        self.root.quit()
        return main_Act_Deact_sync()

    def create_widgets(self):
        header = ttk.Frame(self.root, padding="1 1 1 1")
        header.grid(column=0, row=0, sticky=(N, W, E, S))
        header.columnconfigure(2, weight=1)
        header.rowconfigure(1, weight=1)

        control = ttk.Frame(self.root, padding="3 3 12 12")
        control.grid(column=0, row=1, sticky=(N, W, E, S))
        control.columnconfigure(2, weight=1)
        control.rowconfigure(8, weight=1)

        footer = ttk.Frame(self.root, padding="1 1 1 1")
        footer.grid(column=0, row=2, sticky=(N, W, E, S))
        footer.columnconfigure(2, weight=1)
        footer.rowconfigure(1, weight=1)

        options = {'padx': 1, 'pady': 1}

        title = Label(header, text="JN CRM Solutions Normal", bg='black', fg='white')
        title.pack(fill=X)

        # ___________________labels__________________

        lb1 = Label(control, text="CRM LISTS", fg='red',
                    bg='white', font=("Arial", 10))
        # lb1.place(x=40, y=170)
        lb1.grid(column=0, row=1, **options)

        # ___________________Entry__________________

        # ___________________Buttons__________________

        # lists
        ActivatorBtn = Button(control, text="Accounts Activator",
                              justify='center', width=20, height=2, command=self.activate)
        # ActivatorBtn.place(x=20, y=220)
        ActivatorBtn.grid(column=0, row=2, **options)

        Act_Deact = Button(control, text="Accounts Activation \nand Deactiation",
                           justify='center', width=20, height=2, command=self.both)
        # Act_Deact.place(x=20, y=270)
        Act_Deact.grid(column=0, row=3, **options)

        DeactivatorBtn = Button(control, text="Accounts De-activator",
                                justify='center', width=20, height=2, command=self.deactivate)
        # DeactivatorBtn.place(x=20, y=320)
        DeactivatorBtn.grid(column=0, row=4, **options)

        # _____________________Footer_______________________
        footer = Label(footer, text="Developed by Dr. Joseph Nady",
                       fg='black', bg="silver", font=("Arial", 7))
        # footer.place(x=150, y=480)
        footer.pack(fill=X)

        # footer.grid(column=0,row=0,columnspan=2)

        def exit_application(self):
            # Perform any cleanup or additional actions before exiting
            # print("Exiting application.")
            self.root.quit()

    @classmethod
    def run_gui(cls):
        root = Tk()
        app = cls(root)
        root.mainloop()
