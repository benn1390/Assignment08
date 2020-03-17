#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# RBennett, 2020-March-12, Added code per assignment 08 instructions
#------------------------------------------#

# -- DATA -- #
strChoice = ''
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
objFile = None

class CD:
    """Data Class (Object Instances) - Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        none.
    """
    
    # Constructor
    def __init__(self, cd_id, cd_title, cd_artist):
        
        # Attributes
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
    
    # Properties
    @property
    def cd_id(self):
        return self.__cd_id
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = int(value)
    
    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = value
    
    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = value

# -- PROCESSING -- #
class FileIO:
    """Processing Class (Methods) - Processes data to and from file:

    properties:
        none.

    methods:
        load_inventory(file_name): -> (a list of CD objects)
        save_inventory(file_name, lst_Inventory): -> None
        add_inventory(cd_instance, lst_Inventory): -> None
        delete_inventory(ID, lst_Inventory): -> None

    """
    
    # Methods
    @staticmethod
    def load_inventory(file_name, lst_Inventory):
        """Function to manage data ingestion from file to a list of objects

        Reads the data from file identified by file_name into a list of objects
        One line in the file represents one object in list.
        
        Includes error handling to cover situations when the file to be loaded does not exist (FileNotFoundError)

        Args:
            file_name (string): name of file used to read the data from
            list_Inventory (list): list of class objects that holds the data during runtime

        Returns:
            list_Inventory (list): list of class objects that holds the data during runtime
        
        """
        
        try:
            objFile = open(file_name, 'r')
            lst_Inventory.clear()
            for line in objFile:
                data = line.strip().split(',')
                inventory = CD(data[0],data[1],data[2])
                lst_Inventory.append(inventory)
            objFile.close()
        except FileNotFoundError:
            pass
        return lst_Inventory
    
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to output current inventory to file
        
        Writes currently loaded data to .txt file

        Args:
            file_name (string): name of file used to read the data from
            list_Inventory: list of class objects that holds the data during runtime

        Returns:
            None.

        """
        
        objFile = open(file_name, 'w')
        for row in lst_Inventory:
            lstValues = [cd_instance.cd_id, cd_instance.cd_title, cd_instance.cd_artist]
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
        
    @staticmethod
    def add_inventory(cd_instance, lst_Inventory):
        """Function to add new cd to inventory

        Args:
            cd_instance (class object): class object containing cd info
            list_Inventory: list of class objects that holds the data during runtime

        Returns:
            list_Inventory: list of class objects that holds the data during runtime
        
        """
        
        lst_Inventory.append(cd_instance)   
        return lst_Inventory
    
    @staticmethod     
    def delete_inventory(ID, lst_Inventory):
        """Function to delete class object from list if present

        Args:
            ID (string): string containing ID to be deleted
            list_Inventory: list of class objects that holds the data during runtime

        Returns:
            list_Inventory: list of class objects that holds the data during runtime
        
        """
        intID = int(ID)
        intRowNr = -1
        blnCDRemoved = False
        for row in lst_Inventory:
            intRowNr += 1
            if int(cd_instance.cd_id) == intID:
                del lst_Inventory[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
    

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Processing Class (Methods) -  

    properties:
        none.
        
    methods:
        print_menu(): -> None.
        menu_choice(): -> Choice.
        show_inventory(table): -> None.
        add_inventory(): -> strID, strTitle, strArtist.
        delete_inventory(): -> strIDDel.
    
    """
    
    # Methods
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
    
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x
        
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def show_inventory(lst_Inventory):
        """Displays current inventory table

        Args:
            list: list of class objects that holds the data during runtime

        Returns:
            None.
            
        """
        
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_Inventory:
            print('{}\t{} (by:{})'.format(cd_instance.cd_id, cd_instance.cd_title, cd_instance.cd_artist))
        print('======================================')
    
    @staticmethod
    def add_inventory():
        """Gets user input including ID, title and artist 
        
        Includes error handling to cover situations when the user does not provide a numeric value for ID (ValueError)

        Args:
            None.

        Returns:
            ID (string): a string of the users input for CD ID number
            Title (string): a string of the users input for CD title
            Artist (string): a string of the users input for CD artist

        """
        strID = input('Enter ID: ').strip()
        while ValueError:
            try: 
                int(strID)
                break
            except ValueError:
                strID = input('Error: ID must be numeric. Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist
    
    @staticmethod
    def delete_inventory():
        """Gets user input on which CD they wish to delete.
        
        Includes error handling to cover situations when the user does not provide a numeric value for ID (ValueError)

        Args:
            None.

        Returns:
            ID (string): a string of the users input for CD ID number

        """
        strIDDel = input('Which ID would you like to delete?: ').strip()
        while ValueError:
            try: 
                int(strIDDel)
                break
            except ValueError:
                strIDDel = input('Error: ID must be numeric. Enter ID: ').strip()
        return strIDDel

# -- Main Body of Script -- #

# 1. When program starts, read in the currently saved Inventory
lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)

# Display menu to user
while True:
    
    # show user current inventory
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # let user exit program
    if strChoice == 'x':
        break
    
    # let user display inventory
    if strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue
    
    # let user add data to the inventory
    elif strChoice == 'a':
        strID, strTitle, strArtist = IO.add_inventory()
        cd_instance = CD(strID, strTitle, strArtist)
        FileIO.add_inventory(cd_instance, lstOfCDObjects)
        continue
    
    # let user delete inventory
    if strChoice == 'd':
        strIDDel = IO.delete_inventory()
        FileIO.delete_inventory(strIDDel, lstOfCDObjects)
        continue
    
    # let user save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue 
    
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue
    
    # Catch all error
    else:
        print('General Error')
    
    
    

