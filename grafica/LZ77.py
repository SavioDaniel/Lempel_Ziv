import tkinter as tk
from tkinter import messagebox, scrolledtext

def lz77_compress(input_string, window_size=20, lookahead_buffer_size=15):
    i = 0  
    output = [] 
    
    while i < len(input_string):
        match_length = 0
        match_offset = 0
        search_window_start = max(0, i - window_size)
        lookahead_buffer_end = min(i + lookahead_buffer_size, len(input_string))
        
        for j in range(search_window_start, i):
            k = 0
            while (k < (lookahead_buffer_end - i) and 
                   input_string[j + k] == input_string[i + k]):
                k += 1
            
            if k > match_length:
                match_length = k
                match_offset = i - j
        
        next_symbol = input_string[i + match_length] if (i + match_length) < len(input_string) else None
        output.append((match_offset, match_length, next_symbol))
        i += match_length + 1
    
    return output

def lz77_decompress(compressed_data):
    output = []
    
    for offset, length, symbol in compressed_data:
        start = len(output) - offset
        for i in range(length):
            output.append(output[start + i])
        if symbol is not None:
            output.append(symbol)
    
    return ''.join(output)

def compress_text():
    input_text = input_text_area.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Entrada Inválida", "O texto de entrada está vazio.")
        return

    try:
        compressed_data = lz77_compress(input_text)
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
        decompressed_data = lz77_decompress(compressed_data)
        decompressed_output_area.config(state=tk.NORMAL)
        decompressed_output_area.delete("1.0", tk.END)
        decompressed_output_area.insert(tk.END, decompressed_data)
        decompressed_output_area.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao descomprimir os dados: {e}")

window = tk.Tk()
window.title("Compressão e Descompressão LZ77")
window.geometry("700x600")
window.resizable(False, False)

input_label = tk.Label(window, text="Texto de Entrada:", font=("Arial", 12, "bold"))
input_label.pack(pady=5)
input_text_area = scrolledtext.ScrolledText(window, width=80, height=5, wrap=tk.WORD)
input_text_area.pack(pady=5)

compress_button = tk.Button(window, text="Comprimir", command=compress_text, font=("Arial", 10, "bold"), bg="lightblue")
compress_button.pack(pady=10)

compressed_label = tk.Label(window, text="Dados Comprimidos (LZ77):", font=("Arial", 12, "bold"))
compressed_label.pack(pady=5)
compressed_output_area = scrolledtext.ScrolledText(window, width=80, height=5, wrap=tk.WORD, state=tk.DISABLED)
compressed_output_area.pack(pady=5)

decompress_button = tk.Button(window, text="Descomprimir", command=decompress_text, font=("Arial", 10, "bold"), bg="lightgreen")
decompress_button.pack(pady=10)

decompressed_label = tk.Label(window, text="Texto Descomprimido:", font=("Arial", 12, "bold"))
decompressed_label.pack(pady=5)
decompressed_output_area = scrolledtext.ScrolledText(window, width=80, height=5, wrap=tk.WORD, state=tk.DISABLED)
decompressed_output_area.pack(pady=5)

footer = tk.Label(window, text="Implementação do LZ77 com Tkinter", font=("Arial", 10), fg="gray")
footer.pack(side=tk.BOTTOM, pady=10)

window.mainloop()
