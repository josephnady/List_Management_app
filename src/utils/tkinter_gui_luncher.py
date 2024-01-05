from tkinter import Tk

'''
helper methods for rendering the views of tkinter
you can use (start) method to only render the view
or use (startWithReturnedApp) for rendering and return the app object
'''


class TkGuiStarter:

    def __init__(self, root):
        self.root = root

    @classmethod
    def start(cls):
        root = Tk()
        root.mainloop()

    @classmethod
    def startWithReturnedApp(cls):
        root = Tk()
        app = cls(root)
        root.mainloop()
        return app
