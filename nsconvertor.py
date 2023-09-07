import tkinter as tk
from tkinter import ttk
import pyperclip

def mur_method(num, base):
    global result
    dec_val, pos = 0, 0
    num_str = str(num)
    for digit in reversed(num_str):
        if digit.isdigit():
            digit_value = int(digit)
        else:
            digit_value = ord(digit.upper()) - ord('A') + 10
        dec_val += digit_value * (base ** pos)
        pos += 1
    return dec_val


def most_method(num, base):
    global result
    while num > 0:
        rem = num % base
        if rem >= 10:
            rem_char = chr(ord('A') + rem - 10)
        else:
            rem_char = str(rem)
        result = rem_char + result
        num //= base
    return result


def convert_number():
    global result
    num = entry_number.get()
    from_base = int(entry_from_base.get())
    to_base = int(entry_to_base.get())

    if from_base == 10:
        result = most_method(int(num), to_base)
    else:
        dec_num = mur_method(num, from_base)
        if to_base == 10:
            result = dec_num
        else:
            result = most_method(dec_num, to_base)

    result_label.config(text=result)

def copy_num():
    global result
    pyperclip.copy(result)

result = ""
root = tk.Tk()
root.title("Конвертер систем счисления")

label_number = ttk.Label(root, text="Число:")
label_number.grid(row=0, column=0, padx=10, pady=10)

entry_number = ttk.Entry(root)
entry_number.grid(row=0, column=1, padx=10, pady=10)

label_from_base = ttk.Label(root, text="Из какой системы счисления:")
label_from_base.grid(row=1, column=0, padx=10, pady=10)

entry_from_base = ttk.Entry(root)
entry_from_base.grid(row=1, column=1, padx=10, pady=10)

label_to_base = ttk.Label(root, text="В какую систему счисления:")
label_to_base.grid(row=2, column=0, padx=10, pady=10)

entry_to_base = ttk.Entry(root)
entry_to_base.grid(row=2, column=1, padx=10, pady=10)

copy_button = ttk.Button(root, text="Копировать", command=copy_num)
copy_button.grid(row=3, column=0, padx=10, pady=10)

convert_button = ttk.Button(root, text="Перевести", command=convert_number)
convert_button.grid(row=3, column=1, padx=10, pady=10)

result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

root.mainloop()
