"""
This script converts a full name into a full first name, and a surname.
It accounts for common "double barreled" surnames like "de Klerk".
The results will be stored in a new spreadsheet (provide a path to an empty sheet).
"""

import pandas as pd

#--------------------------- Please fill out --------------------------------#

# File that contains a column of full names (use the full path if the file is not in same directory as main.py)
input_file = 'example_input_file_path.xlsx'

# File that the output will be written to (use an empty spreadsheet to avoid data loss)
# (use the full path if the file is not in same directory as main.py)
output_file = 'example_output_file_path.xlsx'

# The index of the column that the full name is in 
# i.e. column A has an index of 1, B is 2 etc.
column_index = 3

#----------------------------------------------------------------------------#

# Read the input file
df = pd.read_excel(input_file)

names_list = df.iloc[:, column_index - 1].tolist()

# Split each name into a list of strings, delimited by space
split_names = [name.split() for name in names_list]

# List of common double surnames
double_surnames = ['da', 'de', 'del','di', 'do', 'dos', 'du', 'janse','la', 'le', 'los', 'van', 'von']

# If a name contains a double surname, all strings after the double surname are considered part of the surname
# else, only the last string is considered the surname

first_names = []
surnames = []

for name_parts in split_names:
    if any(part.lower() in double_surnames for part in name_parts): # Check if any part of the name is a double surname

        # Find the index of the double surname
        for i, part in enumerate(name_parts):
            if part.lower() in double_surnames:
                double_surname_index = i
                break
        
        # The first names are then the names before the double surname (exclusive)
        # the surnames are the strings after the double surname (inclusive)
        first_name = ' '.join(name_parts[:double_surname_index])
        surname = ' '.join(name_parts[double_surname_index:])
    else:
        # if no double surname, only the last string is a surname
        first_name = ' '.join(name_parts[:-1])
        surname = name_parts[-1]

    
    first_names.append(first_name)
    surnames.append(surname)

names_sheet_df = pd.DataFrame({"First names": first_names, "Surname": surnames})
names_sheet_df.to_excel("example_output_file_path.xlsx", index=False)