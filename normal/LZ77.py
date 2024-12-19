def lz77_comprimir(entrada_string, tamanho_janela=20, tamanho_buffer_antecipacao=15):

    i = 0  
    saida = []  
    
    while i < len(entrada_string):
        comprimento_correspondencia = 0
        deslocamento_correspondencia = 0
        inicio_janela_busca = max(0, i - tamanho_janela)
        fim_buffer_antecipacao = min(i + tamanho_buffer_antecipacao, len(entrada_string))
        
        for j in range(inicio_janela_busca, i):
            k = 0
            while (k < (fim_buffer_antecipacao - i) and 
                   entrada_string[j + k] == entrada_string[i + k]):
                k += 1
            
            if k > comprimento_correspondencia:
                comprimento_correspondencia = k
                deslocamento_correspondencia = i - j
    
        simbolo_seguinte = entrada_string[i + comprimento_correspondencia] if (i + comprimento_correspondencia) < len(entrada_string) else None

        saida.append((deslocamento_correspondencia, comprimento_correspondencia, simbolo_seguinte))
        

        i += comprimento_correspondencia + 1
    
    return saida


def lz77_descomprimir(dados_comprimidos):
   
    saida = []
    
    for deslocamento, comprimento, simbolo in dados_comprimidos:
        inicio = len(saida) - deslocamento
        for i in range(comprimento):
            saida.append(saida[inicio + i])
        if simbolo is not None:
            saida.append(simbolo)
    
    return ''.join(saida)


def principal():

    texto_entrada = input("Digite o texto que deseja compactar: ")
    
    comprimido = lz77_comprimir(texto_entrada)
    print("\nDados comprimidos (LZ77):")
    print(comprimido)

    descomprimido = lz77_descomprimir(comprimido)
    print("\nTexto descomprimido:")
    print(descomprimido)

    if texto_entrada == descomprimido:
        print("\nA descompressão foi bem-sucedida! O texto original foi reconstruído corretamente.")
    else:
        print("\nErro: O texto descomprimido não corresponde ao texto original.")

if __name__ == "__main__":
    principal()
