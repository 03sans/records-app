#pandas: py library used for data manipulation and analysis
#provides high level data structure and functions designed to make data analysis fast and easy in python
#one of the core data structures in pandas is the dataframe, ehich allows to store and manipulate structured data in a tabular format

#DataFrame Data Structure: a 2D labeled data structure with columns of potentially different types (table or spreadsheet like similar
# to SQL table or excel spreadsheet) 

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [20,22,24],
        'City': ['New York', 'Toronto', 'Tokyo']}
df = pd.DataFrame(data)

