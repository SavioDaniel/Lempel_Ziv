def lz78_comprimir(entrada_string):
    dicionario = {}
    proximo_indice = 1
    dados_comprimidos = []

    i = 0
    while i < len(entrada_string):
        string_atual = entrada_string[i]
        if string_atual in dicionario:
            j = i + 1
            while j < len(entrada_string) and string_atual + entrada_string[j] in dicionario:
                string_atual += entrada_string[j]
                j += 1
            dados_comprimidos.append((dicionario[string_atual], entrada_string[i + len(string_atual):i + len(string_atual) + 1]))
            i = i + len(string_atual) + 1
        else:
            dados_comprimidos.append((0, string_atual))
            dicionario[string_atual] = proximo_indice
            proximo_indice += 1
            i += 1

    return dados_comprimidos


def lz78_descomprimir(dados_comprimidos):
    dicionario = {}
    dados_descomprimidos = []

    for indice, simbolo in dados_comprimidos:
        if indice == 0:
            dados_descomprimidos.append(simbolo)
            dicionario[simbolo] = len(dicionario) + 1
        else:
            dados_descomprimidos.append(dicionario[indice] + simbolo)
            dicionario[dicionario[indice] + simbolo] = len(dicionario) + 1

    return ''.join(dados_descomprimidos)

def principal():
    print("Digite o texto para ser comprimido:")
    texto_entrada = input()

    comprimido = lz78_comprimir(texto_entrada)
    print(f"Texto Comprimido: {comprimido}")

    descomprimido = lz78_descomprimir(comprimido)
    print(f"Texto Descomprimido: {descomprimido}")

if __name__ == "__main__":
    principal()






'''Entrada: "ABABABA"

Passo 1:
Símbolo: A
Não está no dicionário.
Adiciona ao dicionário:
Dicionário: {1: A}
Saída: (0, A)

Passo 2:
Símbolo: B
Não está no dicionário.
Adiciona ao dicionário:
Dicionário: {1: A, 2: B}
Saída: (0, B)

Passo 3:
Símbolo: A
Já está no dicionário, então busca pelo próximo símbolo: B
A sequência AB não está no dicionário.
Adiciona ao dicionário:
Dicionário: {1: A, 2: B, 3: AB}
Saída: (1, B) (pois A já estava no dicionário)

Passo 4:
Símbolo: A
Já está no dicionário.
A sequência ABA não está no dicionário.
Adiciona ao dicionário:
Dicionário: {1: A, 2: B, 3: AB, 4: ABA}
Saída: (3, A) (pois AB já estava no dicionário)'''