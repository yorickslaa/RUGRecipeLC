import string
from bs4 import BeautifulSoup
from tkinter import *  # import the graphical library
from tkinter import ttk
from tkinter import messagebox


class MainGUI:
    def __init__(self, master):
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
                                 command=self.variation).grid(row=6, column=0, padx=5)
        self.misc2 = Radiobutton(root, text="suggest an ingredient", variable=var, value=2,
                                 command=self.variation).grid(row=6, column=1)

    def inquire(self):  # action after search button got pressed
        if len(self.ingredient_item1.get()) == 0:
            messagebox.showinfo("Missing ingredient", "No information has been entered in all ingredient boxes, "
                                                      "you require at least 3 ingredients. You can let us suggest an "
                                                      "ingredient by clicking on 'suggest an ingredient'")
        elif len(self.ingredient_item2.get()) == 0:
            messagebox.showinfo("Missing ingredient", "No information has been entered in all ingredient boxes, "
                                                      "you require at least 3 ingredients, You can let us suggest an "
                                                      "ingredient by clicking on 'suggest an ingredient'")

        elif len(self.ingredient_item3.get()) == 0:
            messagebox.showinfo("Missing ingredient", "No information has been entered in all ingredient boxes, "
                                                      "you require at least 3 ingredients, You can let us suggest an "
                                                      "ingredient by clicking on 'suggest an ingredient'")

    @staticmethod
    def variation():
        selection = str(var.get())


root = Tk()
root.resizable(0, 0)  # does not allow resizing
label = Label(root)
var = IntVar()
interface_main = MainGUI(root)
root.mainloop()
