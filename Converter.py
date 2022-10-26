# MichaelFish199

from win32clipboard import OpenClipboard, GetClipboardData, CloseClipboard
from re import compile, finditer
from pandas import DataFrame

# Get clipboard data
OpenClipboard()
text = GetClipboardData()
CloseClipboard()

# Searching for characters in format xi, yi
char_pattern = compile(r'\Di')
char_matches = list(finditer(char_pattern, text))

# Searching for numbers in format 111111.1
num_pattern = compile(r'\d{1,6}[,.]\d')
num_matches = list(finditer(num_pattern, text))

# Creating dictionary 
data = {}
j = 0
for char in char_matches:
    lst = []
    for _ in range(int(len(num_matches) / len(char_matches))):
        lst.append(float(num_matches[j].group()))
        j += 1
    data[char.group()] = lst
    
# Converting to dataframe
df = DataFrame(data)

# Creates a new csv file in current working directory
df.to_csv('data.csv', index=0, sep="\t", decimal=',')
