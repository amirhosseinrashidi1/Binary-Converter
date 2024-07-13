import tkinter as tk
import tkinter.scrolledtext as scrolledtext

def convert_to_binary(event=None):
    input_string = entry.get()
    try:
        number = int(input_string)
        binary_representation = bin(number)[2:]
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f'Binary representation of {number}: {binary_representation}\n')
    except ValueError:
        binary_representation = ''.join(format(ord(char), '08b') for char in input_string)
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f'Binary representation of "{input_string}": {binary_representation}\n')
    finally:
        result_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title('Binary Converter')

label = tk.Label(root, text='Enter an integer or string:')
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack()

convert_button = tk.Button(root, text='Convert', command=convert_to_binary)
convert_button.pack(pady=10)


result_text = scrolledtext.ScrolledText(root, height=10, width=50)
result_text.pack(pady=10)
result_text.config(state=tk.DISABLED)

root.bind('<Return>', convert_to_binary)

root.mainloop()
