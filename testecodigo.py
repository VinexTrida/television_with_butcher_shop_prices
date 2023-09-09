import time
import threading

def buscar_codigo_por_string(arquivo, string_busca, nome):
    with open(arquivo, 'r') as arquivo_texto:
        for linha in arquivo_texto:
            if string_busca in linha:
                codigo = linha[10:15]
                codigo_numerico = int(''.join(filter(str.isdigit, codigo)))
                valor_dividido_por_100 = codigo_numerico / 100

                with open("precos.txt", "a") as arquivo_saida:
                    arquivo_saida.write(f"{nome}={valor_dividido_por_100:.2f}\n")

                return codigo_numerico

    return None

nomes_desejados = [
    "ALCATRA C/OSSO BOVINO kg",
    "MOCOTO BOVINO kg",
    "ALCATRA C/MAMINHA kg",
    "MUSCULO BOVINO C/OSSO kg",
    "CARNE MOIDA 1",
    "MUSCULO BOVINO S/OSSO kg",
    "CARNE MOIDA DE 2",
    "PALETA BOVINA 7 C/OSSO kg",
    "CARNE P/ESTROGONOFE BOV",
    "PALETA BOVINA S/OSSO kg",
    "CONTRA FILE BOVINO kg",
    "PATINHO BOVINO kg",
    "COSTELA BOVINA C/OSSO kg",
    "PEITO BOVINO C/OSSO kg",
    "COXAO FORA BOVINO kg",
    "PEITO BOVINO S/OSSO kg",
    "COXAO MOLE BOVINO kg",
    "RABADA BOVINA kg",
    "DOBRADINHA BOVINA kg",
    "TATU BOVINO kg",
    "FIGADO BOVINO kg",
    "BISTECA SUINA C/PELE kg",
    "FILE DUPLO BOVINO kg",
    "COSTELA SUINA C/PELE kg",
    "FILE SIMPLES BOVINO kg",
    "PERNIL SUINO C/PELE kg",
    "LINGUA BOVINA kg",
    "COXA + SOBRE",
    "LOMBO BOVINO C/OSSO kg",
    "FRANGO AVE SERRA CONGELADO kg",
    "LOMBO BOVINO S/OSSO kg",
    "GALINHA VELHA AVE SERRA kg",
    "MIOLO ALCATRA BOV  kg",
    "PEITO FRANGO C/OSSO LAR kg"
]

arquivo_dados = "itensmgv.txt"

def execute_process():
    while True:
        with open("precos.txt", "w") as arquivo_saida:
            arquivo_saida.write("")

        for nome in nomes_desejados:
            codigo_encontrado = buscar_codigo_por_string(arquivo_dados, nome, nome)  # Passando "nome" como argumento
            if codigo_encontrado is not None:
                print(f"Os números entre a 10ª e a 15ª posição do código associados a '{nome}' são: {codigo_encontrado}")
            else:
                print(f"String de busca '{nome}' não encontrada no arquivo.")

        with open("precos.txt", "r") as arquivo_entrada:
            conteudo = arquivo_entrada.read()

        conteudo_formatado = conteudo.replace('.', ',')

        with open("precos.txt", "w") as arquivo_saida:
            arquivo_saida.write(conteudo_formatado)

        time.sleep(60)

process_thread = threading.Thread(target=execute_process)
process_thread.daemon = True
process_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Programa encerrado manualmente.")
