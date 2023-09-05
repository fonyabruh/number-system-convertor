import tkinter as tk
from tkinter import ttk


def mur_method(num, base):
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
    result = ""
    while num > 0:
        remainder = num % base
        if remainder >= 10:
            remainder_char = chr(ord('A') + remainder - 10)
        else:
            remainder_char = str(remainder)
        result = remainder_char + result
        num //= base
    return result


def convert_number():
    num = entry_number.get()
    from_base = int(entry_from_base.get())
    to_base = int(entry_to_base.get())

    if from_base == 10:
        result = most_method(int(num), to_base)
    else:
        decimal_num = mur_method(num, from_base)
        if to_base == 10:
            result = decimal_num
        else:
            result = most_method(decimal_num, to_base)

    result_label.config(text=result)


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

convert_button = ttk.Button(root, text="Перевести", command=convert_number)
convert_button.grid(row=3, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

root.mainloop()
