import  tkinter as tk



class Calculator(tk.Tk):

    def __init__(self):
        #App window
        self.window = tk.Tk()
        # App size
        self.window.geometry("400x400")
        self.window.resizable(0,0)

        self.window.title("Some Calc")




    def run(self):
        self.window.mainloop()



if __name__ == '__main__':
    calc = Calculator()
    calc.run()