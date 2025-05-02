import pandas as pd


def process_csv(input_file, output_file):
    # Ler o CSV e pegar apenas a primeira coluna
    df = pd.read_csv(input_file, usecols=[0], names=["Class"], header=0)
    
    # Aplicar a condição para substituir valores
    df["Class"] = df["Class"].apply(lambda content: 0 if "Benign" in str(content) else 1)
    
    # Salvar no arquivo de saída
    df.to_csv(output_file, index=False)
    print(f"CSV processado salvo como: {output_file}")

# Exemplo de uso
process_csv("Obfuscated-MalMem2022-Spyware&Benign.csv", "Class_spyware.csv")