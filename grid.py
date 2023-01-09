'''
### Welcome to grid.py ###
Creates grid of minesweeper game

To do: change dimensions according to number of cells
Add function documentation
add refresh button
'''

# Imports
import tkinter as tk
import settings as sett
from cell import Cell
import images

def main():
    
    # Window instance
    window = tk.Tk()
    # Change title
    window.title('Minesweeper game')
    # Change dimensions
    window.geometry(f'{sett.WIDTH}x{sett.HEIGHT}')
    # Impede height and width resizability
    window.resizable(False, False)
    # Change background color
    window.configure(bg = 'white')
    
    # Create frames
    top_frame = tk.Frame(
        window,                 # where the frame object is located
        bg = 'red',           # change background color
        width = sett.WIDTH,
        height = sett.HEIGHT * 0.25       
    )
    main_frame = tk.Frame(
        window,                  # where the frame object is located
        bg = 'green',            # change background color
        width = sett.WIDTH,
        height = sett.HEIGHT * 0.75  
    )
        
    # Locate the frames in the window
    top_frame.place(relx = 0, rely = 0)
    main_frame.place(x = 0, y = sett.HEIGHT * 0.25)
    
    # Cells grid
    for i in range(sett.GRID_SIZE):
        for j in range(sett.GRID_SIZE):
            # Instanciate cell object
            cell = Cell(i,j)
            # Locate it in the main frame
            # and make it behave like tk.Button object
            cell.create_button(main_frame)
            # Assign cell to the grid of the main frame
            cell.button.grid(column = i, row = j)
       
    # Randomize mines
    Cell.deploy_mines()
    
    # Smiley button
    from PIL import Image
    from PIL import ImageTk
    img = Image.open("flag.png")
    img = img.resize((50,50))
    photoImg =  ImageTk.PhotoImage(img)
    smiley = tk.Button(
        top_frame,
        width = 40,
        height = 40,
        image = photoImg,
        command = print(9)
         ).place(relx=0.5, rely=0.5, anchor='center')
    
    # Close window
    window.mainloop()

if __name__ == '__main__':
    main()
