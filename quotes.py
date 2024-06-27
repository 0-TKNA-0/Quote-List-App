# Name: Brody Jeanes
# Student Number: 10568619

# Import the necessary module(s).
from tkinter import *
import tkinter.messagebox
from tkinter import font
import json

class ProgramGUI:

    def __init__(self): #Creates the constructor for the GUI
        self.quote = tkinter.Tk() #creates a window
        self.quote.title("Quote Catalogue") #titles the window
        self.quote.geometry('450x165') #expands the window to the siize
        self.quoteframe = LabelFrame(self.quote, padx=50, pady=10) #create a frame to store everything inside
        self.quoteText = tkinter.Label(self.quoteframe, font = 30) #create a label to store the quote in
        
        self.otherText = tkinter.Label(self.quoteframe) #create a label to store the year and author in
        self.quoteText.grid(row=0, column=1) #assigns the quote to a grid
        self.otherText.grid(row=1, column=1) #assigns the author and year to a grid
        self.quoteframe.pack(pady = 5)
        try: # This will create a loop which trys to open the data.txt file and load, then close the file. If there is no data an error message will be prompted.
            open_data = open("data.txt", "r") #opens the txr file
            self.data = json.load(open_data) #loads the data from the file
            open_data.close() #closes the file
        except:
            self.quote.destroy() #closes the main gui
            tkinter.messagebox.showerror(title="Error Opening File", message="File missing, please input a quote into the admin file.") #creates a error box closing the program   
            return
        self.current_quote = 0 #initialises the current quote counter
        #CREATES A BUNCH OF BUTTONS#
        self.skipbtn = tkinter.Button(self.quoteframe, text="Skip", command=lambda: self.rate_quote('skip'), width=10, height=1) #creates a button for skipping
        self.likesbtn = tkinter.Button(self.quoteframe, text="Likes", command=lambda: self.rate_quote('likes'), width=10, height=1) #creates a button for liking
        self.lovesbtn = tkinter.Button(self.quoteframe, text="Loves", command=lambda: self.rate_quote('loves'), width=10, height=1) #creates a button for loving

        
        self.skipbtn.grid(row=3, column=0, padx=10) #assigns the skip button to a grid
        self.likesbtn.grid(row=3, column=1, padx=10) #assigns the like button to a grid
        self.lovesbtn.grid(row=3, column=2, padx=10) #assigns the love button to a grid
        
        self.show_quote() #calls the show_quote function
    def show_quote(self): #used for updating and showing the current quote
        quote = self.data[self.current_quote]
        if 'year' in quote:
            misc = f"""- {quote['author']}, {quote['year']}"""
        else:
            misc = f"""- {quote['author']}"""

        quoted = f""" "{quote['quote']}" """
        self.quoteText = tkinter.Label(self.quoteframe, text=quoted, font = 30) #adds a quote to the label 
        self.otherText = tkinter.Label(self.quoteframe, text=misc) #adds the author and year to the label
        self.quoteText.grid(row=0, column=1) #adds the quote to a grid
        self.otherText.configure(font=('arial', 10, 'italic')) #makes the author font italic
        self.otherText.grid(row=1, column=1) #adds the author and year to a grid
    def rate_quote(self, rating): #used for rating each quote
        try:
            if rating == 'skip': #when the skip button is clicked, it will show a message box
                skipped = tkinter.messagebox.showinfo(title="Rating Skipped", message="You have skipped rating this quote.") #creates a message box to alert the user that the quote has been recorded
                self.current_quote = self.current_quote + 1 #adds one to the index to go to the next quote
                self.show_quote() #Calls the show_quote function
            else:
                current_data = self.data[self.current_quote]
                current_data[rating] = current_data[rating] + 1 #adds one to rating of the button that is clicked
                dump = json.dumps(self.data, indent=4) #dumps the data into a readable format
                open_data = open('data.txt', 'w') #opens the txt file in write mode
                open_data.write(dump) #writes the new liked, loved messages to txt file
                open_data.close() #closes the file
                self.rate = tkinter.messagebox.showinfo(title = "Rating Recorded", message = "Your rating has been recorded.") #creates a message box to alert the user that the quote has been recorded
        except IndexError:
            self.end = tkinter.messagebox.showinfo(title="End of Quotes", message="That was the last quote.\nThe program will now end.") #the program will show a message box when the last quote has been skipped
            self.quote.destroy() #closes the main gui, ending the program
            
# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()

tkinter.mainloop()