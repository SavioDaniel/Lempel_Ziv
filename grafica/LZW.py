import tkinter as tk
from tkinter import messagebox, scrolledtext

def lzw_compress(input_string):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    current_string = ""
    compressed_data = []

    for symbol in input_string:
        current_string_plus_symbol = current_string + symbol
        if current_string_plus_symbol in dictionary:
            current_string = current_string_plus_symbol
        else:
            compressed_data.append(dictionary[current_string])
            dictionary[current_string_plus_symbol] = next_code
            next_code += 1
            current_string = symbol

    if current_string:
        compressed_data.append(dictionary[current_string])

    return compressed_data

def lzw_decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    current_string = chr(compressed_data[0])
    decompressed_data = [current_string]

    for code in compressed_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = current_string + current_string[0]
        else:
            raise ValueError("Erro na descompressão: código inválido")

        decompressed_data.append(entry)
        dictionary[next_code] = current_string + entry[0]
        next_code += 1
        current_string = entry

    return ''.join(decompressed_data)

def compress_text():
    input_text = input_text_area.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Entrada Inválida", "O texto de entrada está vazio.")
        return

    try:
        compressed_data = lzw_compress(input_text)
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
        decompressed_data = lzw_decompress(compressed_data)
        decompressed_output_area.config(state=tk.NORMAL)
        decompressed_output_area.delete("1.0", tk.END)
        decompressed_output_area.insert(tk.END, decompressed_data)
        decompressed_output_area.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao descomprimir os dados: {e}")

window = tk.Tk()
window.title("Compressão e Descompressão LZW")
window.geometry("700x600")
window.resizable(False, False)

input_label = tk.Label(window, text="Texto de Entrada:", font=("Arial", 12, "bold"))
input_label.pack(pady=5)
input_text_area = scrolledtext.ScrolledText(window, width=80, height=5, wrap=tk.WORD)
input_text_area.pack(pady=5)

compress_button = tk.Button(window, text="Comprimir", command=compress_text, font=("Arial", 10, "bold"), bg="lightblue")
compress_button.pack(pady=10)

compressed_label = tk.Label(window, text="Dados Comprimidos (LZW):", font=("Arial", 12, "bold"))
compressed_label.pack(pady=5)
compressed_output_area = scrolledtext.ScrolledText(window, width=80, height=5, wrap=tk.WORD, state=tk.DISABLED)
compressed_output_area.pack(pady=5)

decompress_button = tk.Button(window, text="Descomprimir", command=decompress_text, font=("Arial", 10, "bold"), bg="lightgreen")
decompress_button.pack(pady=10)

decompressed_label = tk.Label(window, text="Texto Descomprimido:", font=("Arial", 12, "bold"))
decompressed_label.pack(pady=5)
decompressed_output_area = scrolledtext.ScrolledText(window, width=80, height=5, wrap=tk.WORD, state=tk.DISABLED)
decompressed_output_area.pack(pady=5)

footer = tk.Label(window, text="Implementação do LZW com Tkinter", font=("Arial", 10), fg="gray")
footer.pack(side=tk.BOTTOM, pady=10)

window.mainloop()
