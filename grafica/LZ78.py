import tkinter as tk
from tkinter import messagebox, scrolledtext

def lz78_compress(input_string):

    dictionary = {}  
    output = []  
    buffer = "" 
    dict_index = 1  

    for char in input_string:
        buffer += char
        if buffer not in dictionary:

            index = dictionary[buffer[:-1]] if buffer[:-1] in dictionary else 0
            output.append((index, char))
            
            dictionary[buffer] = dict_index
            dict_index += 1
            buffer = ""

    if buffer:  
        index = dictionary[buffer[:-1]] if buffer[:-1] in dictionary else 0
        output.append((index, buffer[-1]))

    return output

def lz78_decompress(compressed_data):

    dictionary = [""]
    output = []

    for index, symbol in compressed_data:
        entry = dictionary[index] + symbol
        output.append(entry)
        dictionary.append(entry)

    return ''.join(output)

def compress_text():
    input_text = input_text_area.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Entrada Inválida", "O texto de entrada está vazio.")
        return

    try:
        compressed_data = lz78_compress(input_text)
        compressed_output_area.config(state=tk.NORMAL)
        compressed_output_area.delete("1.0", tk.END)
        compressed_output_area.insert(tk.END, str(compressed_data))
        compressed_output_area.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def decompress_text():
    compressed_text = compressed_output_area.get("1.0", tk.END).strip()
    if not compressed_text:
        messagebox.showwarning("Entrada Inválida", "Nenhum dado comprimido encontrado.")
        return
    
    try:
        compressed_data = eval(compressed_text)
        decompressed_data = lz78_decompress(compressed_data)
        decompressed_output_area.config(state=tk.NORMAL)
        decompressed_output_area.delete("1.0", tk.END)
        decompressed_output_area.insert(tk.END, decompressed_data)
        decompressed_output_area.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao descomprimir os dados: {e}")


window = tk.Tk()
window.title("Compressão e Descompressão LZ78")
window.geometry("700x600")
window.resizable(False, False)

input_label = tk.Label(window, text="Texto de Entrada:", font=("Arial", 12, "bold"))
input_label.pack(pady=5)
input_text_area = scrolledtext.ScrolledText(window, width=80, height=5, wrap=tk.WORD)
input_text_area.pack(pady=5)

compress_button = tk.Button(window, text="Comprimir", command=compress_text, font=("Arial", 10, "bold"), bg="lightblue")
compress_button.pack(pady=10)

compressed_label = tk.Label(window, text="Dados Comprimidos (LZ78):", font=("Arial", 12, "bold"))
compressed_label.pack(pady=5)
compressed_output_area = scrolledtext.ScrolledText(window, width=80, height=5, wrap=tk.WORD, state=tk.DISABLED)
compressed_output_area.pack(pady=5)

decompress_button = tk.Button(window, text="Descomprimir", command=decompress_text, font=("Arial", 10, "bold"), bg="lightgreen")
decompress_button.pack(pady=10)

decompressed_label = tk.Label(window, text="Texto Descomprimido:", font=("Arial", 12, "bold"))
decompressed_label.pack(pady=5)
decompressed_output_area = scrolledtext.ScrolledText(window, width=80, height=5, wrap=tk.WORD, state=tk.DISABLED)
decompressed_output_area.pack(pady=5)

footer = tk.Label(window, text="Implementação do LZ78 com Tkinter", font=("Arial", 10), fg="gray")
footer.pack(side=tk.BOTTOM, pady=10)

window.mainloop()
