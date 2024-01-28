import tkinter as tk
from tkinter import *
from tkinter import ttk
from Controller.mainfiles import \
    main_Act_Deact_sync,\
    main_Act_Deact,main_Activate,\
    main_Activate_sync,main_Deactivate,\
    main_am
from utils import Utils as u


class ParentInterface:
    def __init__(self,root) -> None:
        self.root = root
        self.root.resizable(False, False)
        self.root.title('JN CRM Solutions')
        self.root.configure(background="silver")
        self.create_widgets()
    
    def create_widget(self):
        self.header = ttk.Frame(self.root, padding="1 1 1 1")
        self.header.grid(column=0, row=0, sticky=(N, W, E, S))
        self.header.columnconfigure(2, weight=1)
        self.header.rowconfigure(1, weight=1)
        
        self.control = ttk.Frame(self.root, padding="3 3 12 12")
        self.control.grid(column=0, row=1, sticky=(N, W, E, S))
        self.control.columnconfigure(2, weight=1)
        self.control.rowconfigure(8, weight=1)
        
        self.footer = ttk.Frame(self.root, padding="1 1 1 1")
        self.footer.grid(column=0, row=2, sticky=(N, W, E, S))
        self.footer.columnconfigure(2, weight=1)
        self.footer.rowconfigure(1, weight=1)
        
        self.options = {'padx': 1, 'pady': 1}
        pass

    def exit_application(self):
        # Perform any cleanup or additional actions before exiting
        print("Exiting application.")
        self.root.quit()


class StartInterface(ParentInterface):
    def __init__(self, root) -> None:
        super().__init__(root)

    def ultramode(self):
        return UpdatedVersion.run_gui()   
        
    def normalmode(self):
        return OldSyncVersion.run_gui()  
    
    def create_widgets(self):
        super().create_widget()
        title = Label(self.header, text="JN CRM Solutions", bg='black', fg='white')
        title.pack(fill=X)
        # ___________________labels__________________
        lb1 = Label(self.control, text="CRM LISTS", fg='red',
                    bg='white', font=("Arial", 10))
        # lb1.place(x=40, y=170)
        lb1.grid(column=0, row=1, **self.options)
        # ___________________Buttons__________________
        ultrabtn = Button(self.control, text="Ultra Fast Mode",
                            justify='center', width=20, height=2, command=self.ultramode)
        ultrabtn.grid(column=0, row=2, **self.options)

        normalbtn = Button(self.control, text="Normal Mode",
                        justify='center', width=20, height=2, command=self.normalmode)
        normalbtn.grid(column=0, row=3, **self.options)
        # _____________________Footer_______________________
        footer = Label(self.footer, text="Developed by Dr. Joseph Nady",
                    fg='black', bg="silver", font=("Arial", 7))
        footer.pack(fill=X)

    @classmethod
    def run_start_gui(cls):
        root = Tk()
        app = cls(root)
        root.mainloop()

class VersionInterface(ParentInterface):
    def __init__(self,root) -> None:
        return super().__init__(root)
    
    def create_buttons(self):
        self.ActivatorBtn = Button(self.control, text="Accounts Activator",
                            justify='center', width=20, height=2, command=self.activate)
        self.ActivatorBtn.grid(column=0, row=2, **self.options)
        self.Act_Deact = Button(self.control, text="Accounts Activation \nand Deactiation",
                        justify='center', width=20, height=2, command=self.both)
        self.Act_Deact.grid(column=0, row=3, **self.options)
        self.DeactivatorBtn = Button(self.control, text="Accounts De-activator",
                                justify='center', width=20, height=2, command=self.deactivate)
        self.DeactivatorBtn.grid(column=0, row=4, **self.options)
        self.AmListManagement = Button(self.control, text="AM List Management",
                                       justify='center', width=20, height=2, command=self.am_list)
        self.AmListManagement.grid(column=0, row=5, **self.options)
        # DeactivatorBtn.place(x=20, y=320)
        # _____________________Footer_______________________
        self.foot = Label(self.footer, text="Developed by Dr. Joseph Nady",
                    fg='black', bg="silver", font=("Arial", 7))
        self.foot.pack(fill=X)


class UpdatedVersion(VersionInterface):
    def __init__(self, root) -> None:
        super().__init__(root)
        cores = int(u.cpu_count())
        self.usedcores = cores/2
        
    def activate(self):
        self.root.quit()
        return main_Activate(self.usedcores)
    
    def deactivate(self):
        self.root.quit()
        return main_Deactivate()

    def both(self):
        self.root.quit()
        return main_Act_Deact(self.usedcores)
    
    def am_list(self):
        self.root.quit()
        return main_am()

            
    def create_widgets(self):
        super().create_widget()
        title = Label(self.header, text="JN CRM Solutions Ultra", bg='black', fg='white')
        title.pack(fill=X)
        # ___________________labels__________________
        lb1 = Label(self.control, text="CRM LISTS", fg='red',
                    bg='white', font=("Arial", 10))
        # lb1.place(x=40, y=170)
        lb1.grid(column=0, row=1, **self.options)
        super().create_buttons()

    @classmethod
    def run_gui(cls):
        root = Tk()
        app = cls(root)
        root.mainloop()


class OldSyncVersion(VersionInterface):
    def __init__(self, root):
        super().__init__(root)

    def activate(self):
        self.root.quit()
        return main_Activate_sync()
    
    def deactivate(self):
        self.root.quit()
        return main_Deactivate()

    def both(self):
        self.root.quit()
        return main_Act_Deact_sync()

    def am_list(self):
        self.root.quit()
        return main_am()

    def create_widgets(self):
        super().create_widget()
        self.title = Label(self.header, text="JN CRM Solutions Normal", bg='black', fg='white')
        self.title.pack(fill=X)
        # ___________________labels__________________
        self.lb1 = Label(self.control, text="CRM LISTS", fg='red',
                    bg='white', font=("Arial", 10))
        self.lb1.grid(column=0, row=1, **self.options)
        super().create_buttons()
    
    @classmethod
    def run_gui(cls):
        root = Tk()
        app = cls(root)
        root.mainloop()
