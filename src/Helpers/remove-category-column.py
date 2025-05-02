import pandas as pd


def remove_first_column(input_file, output_file):
    # Ler o CSV ignorando a primeira coluna
    df = pd.read_csv(input_file)
    df = df.iloc[:, :-1]  # Remove a primeira coluna
    
    # Salvar no novo arquivo
    df.to_csv(output_file, index=False)
    print(f"CSV sem a primeira coluna salvo como: {output_file}")

# Exemplo de uso
remove_first_column("caracter_spy.csv", "caracter_spy.csv")