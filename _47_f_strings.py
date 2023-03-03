# Formatted String Literals. Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression} .

import math

name = "Roshan"
fname = "Dattu"
surname = "Nikam"

a = f"my name is {name}. my father name is {fname}. my surname is {surname}.i got {45+45+0.40} marks in board exam  "
print(a)