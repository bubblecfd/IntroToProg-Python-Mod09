# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Tao Ye,6.9.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
strFileName = 'EmployeeData.txt'
lstTable = []
strChoice = ""

# Load data from file into a list of employee objects when script starts
lstFileData = Fp.read_data_from_file(strFileName)
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))

# Show the current list
Eio.print_current_list_items(lstTable)

# Show user a menu of options
while True:
    Eio.print_menu_items()
    strChoice = Eio.input_menu_options()

    if (strChoice.strip() == '1'):      # Show current list of employees
        Eio.print_current_list_items(lstTable)

    elif (strChoice.strip() == '2'):    # Add new employee
        lstTable.append(Eio.input_employee_data())
        Eio.print_current_list_items(lstTable)

    elif (strChoice.strip() == '3'):    # save the data to the file
        if (Fp.save_data_to_file(strFileName, lstTable)):
            print("Data saved to file.")

    elif (strChoice.strip() == '4'):    # Exit the program
        input("Press the [Enter] key to return to exit.")
        break
    else:
        print("Invalid choice; try again...")
# Main Body of Script  ---------------------------------------------------- #
