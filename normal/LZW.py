def lzw_comprimir(string_entrada):
    dicionario = {chr(i): i for i in range(256)}  
    resultado = []
    string_atual = ""
    
    for simbolo in string_entrada:
        if string_atual + simbolo in dicionario:
            string_atual += simbolo
        else:
            resultado.append(dicionario[string_atual])
            dicionario[string_atual + simbolo] = len(dicionario)
            string_atual = simbolo
    
    if string_atual:
        resultado.append(dicionario[string_atual])
    
    return resultado


string_entrada = input("Digite a palavra para compressão: ")
comprimido = lzw_comprimir(string_entrada)
print("Comprimido:", comprimido)

