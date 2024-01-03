from tkinter import *

class DeactGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x300+950+100')
        self.root.resizable(False, False)
        self.root.title('Deactivation')
        self.root.configure(background="silver")
        self.create_widgets2()


    def exit_application(self):
        # Perform any cleanup or additional actions before exiting
        print("Exiting application.")
        self.root.quit()
        inputs = [self.line_entry.get(),self.terr_entry.get()]
        return inputs

    def create_widgets2(self):   
        title = Label(self.root, text="Accounts Deactivor",
                  bg='white', fg='red', font=("Arial", 20))
        title.pack(fill=X)
        # ___________________labels__________________

        lblhead1 = Label(self.root, text="Note: \n\n1-Copy both LINE and TERRITORY NAME from crm\n2-Paste it the below textboxs.",
                        fg="black", bg="silver", justify="left", font=("Arial", 9))
        lblhead1.place(x=12, y=60)


        lb4 = Label(self.root, text="Line:", fg='red')
        lb4.place(x=10, y=160)

        lb5 = Label(self.root, text="Territory:", fg='red')
        lb5.place(x=10, y=200)

        # ___________________Entry__________________

        self.line_entry = Entry(self.root, width=30)
        self.line_entry.place(x=100, y=160)

        self.terr_entry = Entry(self.root, width=30)
        self.terr_entry.place(x=100, y=200)

        # ___________________Buttons__________________

        exitbtn = Button(self.root, text="LOGIN", justify='center',
                        width=20, height=1, command=self.exit_application)
        exitbtn.place(x=70, y=240)

        # _____________________Footer_______________________
        footer = Label(self.root, text="Developed by Dr. Joseph Nady",
                    bg="silver", fg='black', font=("Arial", 7))
        footer.place(x=70, y=330)

    @classmethod
    def deact_gui(cls):
        root = Tk()
        app = cls(root)
        root.mainloop()
        results = app.exit_application()
        return results