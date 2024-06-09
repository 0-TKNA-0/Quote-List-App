# Name: Brody Jeanes
# Student Number: 10568619

# Import the necessary modules.
import json #used for storing the data into a file, opening, loading, etc.
import textwrap #used for the textwrap.shorten to truncate sentences

def input_int(prompt): # This function repeatedly prompts for input until an integer of at least 1 is entered.
    while True:
        try:
            User = int(input(prompt)) #prompts the user for a integer input
            if User == '' or User <= 0: #checks if the prompt meets the valid criteria. 
                print("Invalid Input") 
                continue
            else:
                return User
                break
        except ValueError: #if the user puts letters or symbols in, then the valueerror will output invalid input
            print("Invalid Input")
            continue
        
def input_something(prompt): # This function repeatedly prompts for input until something other than whitespace is entered.
    while True:
        User = input(prompt) #prompts the user for a input
        if User == '': #checks if the prompt meets the valid criteria.
            if "year" in prompt.lower(): #if the key 'year' is in the users response (numbers) then it saves it, but if there is no input, '', then it saves it as unknown
                User = "Unknown" #defines the year key as unknown
                return User
            else:
                print("Invalid Input")
                continue
        else:
            return User
            break
        
def save_data(data_list): # This function opens "data.txt" in write mode and writes data_list to it in JSON format.
    data_list = json.dumps(data, indent=4) #provides the format in which the data is saved in.
    open_data = open("data.txt", "w") #opens the file in write mode
    open_data.write(data_list) #writes the saved data to the file
    open_data.close() #closes the file
    
try: # This will create a loop which trys to open the data.txt file and load, then close the file. If there is no data then a empty list will be created.
    open_data = open("data.txt", "r") #opens the file in read mode
    data = json.load(open_data) #loads the data from the file
    open_data.close() #closes the file
except:
    data = [] #creates a empty list if nothing is stored in the file, or if the file doesnt exist it will create a txt file called data.txt

print('Welcome to the "Quote Catalogue" Admin Program.') # This is the title screen when the program is launched

while True: # This creats a loop for the program to run infinitly until it is quit by the user.
        print("\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.") # This is the screen that shows you the types of inputs that you can perform
        choice = input("> ").lower() #asks for the users input and saves it in .lower() format
        
        if choice == "a": # Allows the user to add a new quote.
            inputQuote = input_something("Enter the Quote: ") # The users input for entering a quote
            inputAuthor = input_something("Enter the Author's name: ") # The users input for entering a author
            inputYear = input("Enter the Year (Leave blank if unknown): ") # The users input for entering a year
            print("Quote Added!")
            if inputYear == "": # verifies if the users input for year is whitespace
                inputYear = "Unknown" #replaces the whitespace with unknown
            save_diction = {"quote":inputQuote,"author":inputAuthor,"year":inputYear,"likes":0,"loves":0} #creates a dictionary with saved variables
            if inputYear == "Unknown": #checks to see if the year key = unknown
                del save_diction["year"] #deletes the year key
            data.append(save_diction) #appends the dictionary to a list
            save_data(save_diction) #calls the save_data function

        elif choice == "l": # Allows the user to list the current quotes stored in data.txt.
            if not data: #checks to see if there is a valid list in the text file
                print("No Quotes Saved")
            else:
                print("List of Quotes:")
                counter = 1 #creates a counter starting at 1
                for item in data: 
                    aQuote = textwrap.shorten(item["quote"], width=40, placeholder="...") #shortens the displayed quotes over 40 characters and replaces it with ...
                    unknownYear = item.get("year", "Unknown")
                    if unknownYear == "Unknown": #if the key 'year' is called unknown then it will print without the year.
                        print(f"""   {counter}) "{aQuote}" - {item['author']}""")
                        counter = counter + 1 #adds one more to the counter
                    else:
                        print(f"""   {counter}) "{aQuote}" - {item['author']}, {unknownYear}""")
                        counter = counter + 1 #adds one more to the counter
                
        elif choice == "s": # Allows the user to search the current quotes stored in data.txt.
            if not data: #checks to see if there is a valid list in the text file
                print("No Quotes Saved")
            else:
                search = input_something("Enter a search term: ").lower() #asks for an input then saves it as .lower()
                for item in data:
                    if search in item["quote"].lower() or search in item["author"].lower():
                        unknownYear = item.get("year", "Unknown")
                        itemNum = data.index(item) + 1 #adds 1 to the already known index of each dictionary
                        aQuote = textwrap.shorten(item["quote"], width=40, placeholder="...") #shortens the displayed quotes over 40 characters and replaces it with ...
                        print(f"""{itemNum}) "{aQuote}" \n     - {item['author']}, {unknownYear}""")
                    
        elif choice == "v": # Allows the user to view the current quotes stored in data.txt.
            try:
                if not data: #checks to see if there is a valid list in the text file
                    print("No Quotes Saved")
                else:
                    quoteNum = int(input_int("Enter the quote number to view: "))
                    vQuote = data[quoteNum - 1]
                    unknownYear = vQuote.get("year", "Unknown")
                    print(f"""{quoteNum}) "{vQuote['quote']}"\n     - {vQuote['author']}, {unknownYear}\n""")
                    print(f"""This quote has recieved {vQuote['likes']} and {vQuote['loves']} loves.""")
            except IndexError:
                print("Value out of range")
            
        elif choice == "d": # Allows the user to delete any of the current quotes stored in data.txt.
            try:
                if not data: #checks to see if there is a valid list in the text file
                    print("No Quotes Saved")
                else:
                    quoteNum = int(input_int("Enter the quote number to delete: ")) #calls the input_int function when prompting for an input
                    del data[quoteNum - 1] #deletes the selected quote
                    data_list = 1
                    save_data(data_list) #calls the save_data function
                    print("Quote successfully deleted!")
            except IndexError:
                print("Value out of range")
                
        elif choice == "q": # Allows the user to quit the program.
            print("Goodbye!")
            break #stops the program

        else: # If an invalid input is inputted then this message will be presented and the loop will begin again
            print("Invalid Choice, please try again!")
