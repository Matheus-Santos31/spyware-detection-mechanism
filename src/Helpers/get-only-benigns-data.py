import csv

# Defina o nome do arquivo de entrada e saída
input_filename = 'Obfuscated-MalMem2022.csv'
output_filename = 'Obfuscated-MalMem2022-Benign.csv'


# Defina a condição que deseja verificar na coluna "x"
def condicao_linha(content: str):
    # Aqui você pode personalizar a condição. Exemplo: se o valor na coluna "x" for maior que 10.
    return content.__contains__("Benign")

# Abrir o arquivo CSV de entrada
with open(input_filename, mode='r', newline='', encoding='utf-8') as infile:
    csvreader = csv.DictReader(infile)  # Usar DictReader para acessar as colunas pelo nome
    header = csvreader.fieldnames  # Obter o cabeçalho

    # Filtrar as linhas com base na condição
    linhas_filtradas = [linha for linha in csvreader if condicao_linha(linha['Category'])]

# Escrever as linhas filtradas no novo arquivo CSV
with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
    csvwriter = csv.DictWriter(outfile, fieldnames=header)
    csvwriter.writeheader()  # Escrever o cabeçalho
    csvwriter.writerows(linhas_filtradas[:10020])  # Escrever as linhas filtradas

print(f'Novo arquivo CSV gerado: {output_filename}')