import sys
import pyperclip

def embellish(array):
    all_numbers = True
    for elem in array:
        if not is_number(elem):
            all_numbers = False
            break

    result = ""
    for i, elem in enumerate(array):
        processed_elem = ""
        if all_numbers:
            processed_elem = elem
        else:
            processed_elem = "'" + elem + "'"

        if i == 0:
            processed_elem = "  " + processed_elem
        else:
            processed_elem = ", " + processed_elem

        result += "\n" + processed_elem
    return result

def to_collection(string):
    return string.split("\r\n")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

input_val = pyperclip.paste()

pyperclip.copy(embellish(to_collection(input_val)))
