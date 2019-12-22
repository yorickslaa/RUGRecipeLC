import string
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from tkinter import *  # import the graphical library
from tkinter import ttk
from tkinter import messagebox
from xlsxwriter import *
from openpyxl import *


def output():  # Pandas application to process and output data in Excel
    recipe_return = {'Recipe Name': ['Recipe 1', 'Recipe 2'],  # we need to change this to the scrape variables?
                     'Ingredient 1': ['Ingredient name 1', 'Ingredient name 2'],
                     'Ingredient 2': ['Ingredient name 1', 'Ingredient name 2']
                     }
    df = pd.DataFrame(recipe_return, columns=['Recipe Name', 'Ingredient 1', 'Ingredient 2'])
    writer = pd.ExcelWriter('recipe_overview.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Overview')
    writer.save()
    print(df)


def variation():  # planned to allow the radio buttons to decide on way of searching
    str(var.get())


class MainGUI:
    def __init__(self, master):  # creates the GUI interface
        self.master = master
        master.title("Recipe Suggestion")
        root.geometry('330x180')

        self.label_ingredient1 = Label(master, text="Ingredient 1", font=("arial", 10, "bold"))
        self.label_ingredient1.grid(row=0, column=0, padx=5, pady=5)

        self.ingredient_item1 = StringVar()
        self.ingredient_item1 = Entry(root, textvariable=self.ingredient_item1)
        self.ingredient_item1.grid(row=1, column=0, padx=6, pady=0)

        self.label_ingredient2 = Label(master, text="Ingredient 2", font=("arial", 10, "bold"))
        self.label_ingredient2.grid(row=2, column=0, padx=0, pady=0)

        self.ingredient_item2 = StringVar()
        self.ingredient_item2 = Entry(root, textvariable=self.ingredient_item2)
        self.ingredient_item2.grid(row=3, column=0, padx=6, pady=0)

        self.label_ingredient3 = Label(master, text="Ingredient 3", font=("arial", 10, "bold"))
        self.label_ingredient3.grid(row=4, column=0, padx=0, pady=0)

        self.ingredient_item3 = StringVar()
        self.ingredient_item3 = Entry(root, textvariable=self.ingredient_item3)
        self.ingredient_item3.grid(row=5, column=0, padx=6, pady=0)

        self.search_button = Button(root, text="search matching recipe", command=self.inquire)
        self.search_button.grid(row=5, column=1, padx=5, pady=0)

        self.misc1 = Radiobutton(root, text="use all entered ingredients", variable=var, value=1,
                                 command=variation).grid(row=6, column=0, padx=5)
        self.misc2 = Radiobutton(root, text="suggest an ingredient", variable=var, value=2,
                                 command=variation).grid(row=6, column=1)

    def inquire(self):  # action after search button got pressed
        if len(self.ingredient_item1.get()) == 0:
            messagebox.showinfo("Missing ingredient", "No information has been entered in all ingredient boxes, "
                                                      "you require at least 3 ingredients. You can let us suggest an "
                                                      "ingredient by clicking on 'suggest an ingredient'")
        elif len(self.ingredient_item2.get()) == 0:
            messagebox.showinfo("Missing ingredient", "No information has been entered in all ingredient boxes, "
                                                      "you require at least 3 ingredients, You can let us suggest an "
                                                      "ingredient by clicking on 'suggest an ingredient'")

        elif len(self.ingredient_item3.get()) == 0 and len(self.ingredient_item2.get()) == 0 or \
                len(self.ingredient_item1.get()) == 0:
            messagebox.showinfo("Missing ingredient", "No information has been entered in all ingredient boxes, "
                                                      "you require at least 3 ingredients, You can let us suggest an "
                                                      "ingredient by clicking on 'suggest an ingredient'")

        output()  # runs the output DEF which is comprised of all Pandas / XLSX writer

    def scraper(self):
        pass


root = Tk()
root.resizable(0, 0)  # does not allow resizing
label = Label(root)
var = IntVar()
interface_main = MainGUI(root)
root.mainloop()
