'''
### Welcome to cell.py ###
Creates Cell class

To do:
    1) Change button shape
    2) Add in surroandings a check to see if the surroanding cells have been left-clicked
    3) see the relation of @property with getters and setters
    4) Add flag instead of ?
'''

from tkinter import Button
import random
import settings as sett

class Cell():
    # Class attribute with the created cells
    all = []
    # Class attribute with the number of mines left
    mines_left = sett.NUMBER_MINES
    # Class constructor
    def __init__(self, x, y, mined = False):
        # Instance attributes
        self.button = None
        self.left_clicked = False
        self.right_clicked = False
        self.mined = mined
        self.x = x
        self.y = y
        
        # Append Cell object to the list
        Cell.all.append(self)
    
    # What will be printed when we print an object of the class
    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
    
    # Create button intance method
    def create_button(self, location):
        btn = Button(
            location,
            width = 12,
            height = 4,
            bg = 'grey'
            )
        # Assign events to the buttons
        btn.bind('<Button-1>', self.left_click) #FIRST ACTION AND THEN FUNCTION
        btn.bind('<Button-3>', self.right_click)
        # Now the cell will behave as a tkinter.Button object
        self.button = btn
      
    # Define left click actions
    def left_click(self, event):
        
        if self.mined:
            self.button.configure(bg = 'red')
            #self.explosion()
        else:
            # Change left_clicked attribute
            self.left_clicked = True
            # Show cell
            self.button.configure(
                text = self.surrounding_mines, 
                bg = 'white')
            # Show surrounding cell if the self cell has no surrounding mines
            self.show_surrounding_mines()
            
            # Show surrounding cells when the amount of surrounding flagged cells 
            # is equal to the surrounding_mines
            self.speedy()
                        
    
    # Implement recursion to check surrounding_mines == 0
    def show_surrounding_mines(self):
        if self.surrounding_mines == 0:
            for cell in self.surrounding_cells:
                if cell.left_clicked == False:
                    # Left click on the surrounding cells
                    # Giving a value to the argument event is necessary
                    cell.left_click(event = None)
    #
    def main_left_click_actions(self):
        if self.mined:
            self.button.configure(bg = 'red')
            #self.explosion()
        else:
            # Change left_clicked attribute
            self.left_clicked = True
            # Show cell
            self.button.configure(
                text = self.surrounding_mines, 
                bg = 'white')
                    
    # Show surrounding cells when the amount of surrounding flagged cells 
    # is equal to the surrounding_mines
    def speedy(self):
        # Calculate the surrounding right clicked cells
        right_cliked_around = sum([cell.right_clicked
                                        for cell in self.surrounding_cells])
        
        # Left click on the intact ones
        if self.left_clicked and right_cliked_around == self.surrounding_mines:
            for cell in self.surrounding_cells:
                if not cell.left_clicked and not cell.right_clicked:
                    cell.main_left_click_actions()
                    
        
    
    # Define right click actions
    def right_click(self, event):
        # Reduced number of mines
        Cell.mines_left -= 1
        # Allow to unflag a cell
        if self.right_clicked:
            self.right_clicked = False
            self.button.config(
                 bg = 'grey',
                 text = ''
                 )
        # Flag cell
        elif not self.left_clicked:
            self.right_clicked = True
            self.button.config(
                bg = 'green',
                text = 'Mine?'
                )
         
    
    # Left click on a bomb
    def explosion(self):
        # Unasign events to the buttons
        self.btn.unbind('<Button-1>')
        self.btn.unbind('<Button-3>')
        #
            
    # Calculate surrounding cells
    @property # Makes class methods an instance attribute just like self.mined
    def surrounding_cells(self):
        
        def in_bounds(coordinates):
            return all(i >= 0 and i < sett.GRID_SIZE for i in coordinates)
        
        cells = [] # [(0,1), (1,2)] ~ [Cell(0,1), Cell(1,2)]
        for i in range(-1,2):
            for j in range(-1,2):
                neighbour = (self.x + i, self.y + j)
                cells.append(neighbour)
        cells = [Cell.cell_by_axis(i) for i in cells 
                 if in_bounds(i) and i != (self.x, self.y)]
        return cells
    
    # Calculate number of mines in the surrounding
    @property # Makes class methods an instance attribute just like self.mined
    def surrounding_mines(self):
        mines = sum([cell.mined for cell in self.surrounding_cells])
        return mines
    
    
    # This decorator allows to put a function into a class where it logically
    # belongs while indicating it does not require access to the class
    @staticmethod
    def deploy_mines():
        '''
        ### FUNCTION ###
        Choose 9 random cells and change its mined state to True
        '''
        mined_cells = random.sample(Cell.all, sett.NUMBER_MINES)
        for cell in mined_cells:
            cell.mined = True
            
    # Return a cell object 
    @staticmethod
    def cell_by_axis(coordinates):
        for cell in Cell.all:
            if cell.x == coordinates[0] and cell.y == coordinates[1]:
                return cell





