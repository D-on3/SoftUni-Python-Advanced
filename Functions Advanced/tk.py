import tkinter as tk
from tkinter.ttk import Frame , Label , Style
from tkinter import Tk

class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.elements = {"1": 1 , "2" : 2 , "3" : 3, "4" : 4 , "5": 5 ,"6": 6 ,"7" : 7 , "8": 8 , "9": 9 ,"0":0 ,
                         "+":None , "-": None}
        self.check = []
        self.counter = 1



    def run(self):
        for key,value in self.elements.items():
            self.button_key = tk.Button(self,text= f"{key}")

            if not len(self.check) >= 3:
                self.button_key.grid( row= self.counter, column = self.counter)
                self.check.append("|")

            else:
                self.check = []
                self.counter += 1



        self.mainloop()



def main():

    root = Tk()
    root.geometry("300x280+300+300")
    app = Calculator()
    root.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
