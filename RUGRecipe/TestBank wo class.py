import pandas as pd
from tkinter import *
import webbrowser


def launch(search_command, database="recipes.csv"):  # looks for scraped recipe and retrieves best option
    file = open(database)
    recipes_df = pd.read_csv(file, header=[0])

    my_ingredients = [listbox_overview]
    to_cook = launch(my_ingredients)
    print(to_cook)

    my_result = {}
    my_present = 0
    my_absent = 1000

    for index, row in recipes_df.iterrows():
        present = 0
        absent = 0

        for i in search_command:

            if i in row[1]:
                present += 1
            else:
                absent += 1

        if absent < my_absent:
            my_result.clear()
            my_result.update({row[0]: row[2]})
            my_absent = absent
        elif absent == my_absent:
            my_result.update({row[0]: row[2]})
        else:
            my_present += 1

        if len(my_result) >= 10:  # if there 10 recipes in the results, stop adding more
            break

    return my_result
    #  webbrowser.open("google.com", new=0, autoraise=True)


def adding():  # allows user to add an ingredient to the list
    listbox_overview.insert(END, temp.get())
    entry_box_ingredient.delete(0, END)


def clearing():  # allows user to remove one ingredient
    listbox_overview.delete(0, END)


def clear_select():  # allows user to clear all ingredients
    listbox_overview.delete(ANCHOR)


# Basic elements & conditions
root = Tk()
root.title("Recipe Suggestion")
root.geometry('560x380')
root.resizable(False, False)

# create a variable containing the ingredient string to add it to the listbox_overview
temp = StringVar()

# Labels GUI
label_ingredient = Label(root, text="Ingredient 3", font=("arial", 10, "bold"))
label_overview = Label(root, text="Ingredients:", font=("arial", 10, "bold"))
label_suggested = Label(root, text="Suggested recipes:", font=("arial", 10, "bold"))

# Listbox GUI
listbox_overview = Listbox(root, width=40, height=15, selectmode='single')
listbox_recipes = Listbox(root, width=43, height=15, selectmode='single')

# Buttons GUI
button_add = Button(root, text="add ingredient", command=adding)
button_access = Button(root, text="Search recipes", command=launch, height=1, width=35)
button_clear = Button(root, text="remove all ingredients", command=clearing)
button_remove = Button(root, text="remove selected ingredient", command=clear_select)

# Entry box GUI
entry_box_ingredient = Entry(root, textvariable=temp, width=40)

# Placement of elements on roster / canvas
# Labels
label_ingredient.place(x=10, y=130)
label_overview.place(x=10, y=10)
label_suggested.place(x=275, y=10)

# Entry box
entry_box_ingredient.place(x=10, y=305)

# Buttons
button_add.place(x=275, y=300)
button_remove.place(x=380, y=300)
button_clear.place(x=10, y=340)
button_access.place(x=275, y=340)

# List boxes
listbox_overview.place(x=10, y=40)
listbox_recipes.place(x=275, y=40)

# loop the program, note: this must be the final line of our coding!
root.mainloop()


