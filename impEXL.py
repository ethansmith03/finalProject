# This code is for the importation of an excel file to be read and distributed upon our program.
# This snippet will be made to work with a file selection menu.

import pandas as pd

# This variable defines the file location at which the excel file is stored
fileLoc = r"C:/Users/ethan/OneDrive/Desktop/finalProj/ss.xlsx"

# This variable reads and then stores the entire excel file for later distribution.
fileRead = pd.read_excel(fileLoc)

# This line is print out the entire table.
print(fileRead)
print()

# Printing a specific column from our table stored in it's entirety. 
print(pd.DataFrame(fileRead, columns=["Num"]))
print()

# This variable stores the specific column chosen
column2 = fileRead['Num'].tolist()

# This for loop provides proof on concept for sorting and storing of data from a singular column

for x in column2:
    if x > 7:
        print(x)
print()

# This snippet provides proof of concept for singling out single rows
print(fileRead.loc[2])