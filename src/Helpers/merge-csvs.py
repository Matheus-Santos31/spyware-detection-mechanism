import pandas as pd


def merge_csv(file1, file2, output_file):
    # Ler os dois CSVs
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Combinar os dois DataFrames
    df_merged = pd.concat([df1, df2], ignore_index=True)
    
    # Salvar no arquivo de saída
    df_merged.to_csv(output_file, index=False)
    print(f"CSV mesclado salvo como: {output_file}")

# Exemplo de uso
merge_csv("Obfuscated-MalMem2022-Benign.csv", "Obfuscated-MalMem2022-Spyware.csv", "Obfuscated-MalMem2022-Spyware&Benign.csv")