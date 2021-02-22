# Layout managers: Pack, Place and Grid

# Pack: packs each of the widgets from the top to the bottom. Placement can be changed by adding side=("left", "right", "top", "bottom")

# Place: All about prices positioning by providing coordinates (x,y values). Placement can be changed by using the .place() and providing x,y values like e.g.: my_label.place(10)
# Downside of Place is that it's so specific and we would have to place each widget at a specific coordinate to have the placement of every widget be logical.

# Grid: Divides your program in columns and rows by providing a column and a row number like this: my_label.grid(column=0, row=0) which places your widget in the top left corner. The grid system is relative to other components. So if you have no other components on screen and add .grid(column=5, row=5) than your widget will still be placed in the top left corner of the screen. The easiest way of working with the grid, is starting with the widget you want at the top left.

# Grid and Pack can't be mixed up in the same program.

# Add padding around components. Directly modify the widgets e.g. for padding around the window we could do something like: window.config(padx=20, pady=20)